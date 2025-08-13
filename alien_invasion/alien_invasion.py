import sys
import pathlib
import pygame
import pygame.display
import pygame.event
import pygame.sprite
import pygame.time
import pygame.mouse

from time import sleep
from random import randint

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import ShipBullet, AlienBullet
from alien import Alien
from button import Button

class AlienInvasion:
    """Class containing all game assets"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self._screen_mode()
        pygame.display.set_caption("Alien Invasion")
        
        # Create game stats and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(ai_game=self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Last row aliens can fire bullets
        self.armed_aliens = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.eb_spawn_cd = self.settings.eb_spawn_cd

        self._create_fleet()
        self.game_active = False

        # Make buttons
        self.button_play = Button(self, "PLAY")
        self.button_easy = Button(self, "EASY")
        self.button_hard = Button(self, "HARD")


    def run_game(self):
        """Start the main loop"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_enemy_bullets()
                self._update_aliens()
                self._spawn_enemy_bullet()
            self._update_screen()
            # Next line aligns that the loop runs 60 times per second
            # 60 frames are rendered in a single second (60FPS)
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_click(mouse_pos)


    def _check_mouse_click(self, mouse_pos):
        """Check if mouse click is on any button"""
        play_clicked = self.button_play.rect.collidepoint(mouse_pos)
        easy_clicked = self.button_easy.rect.collidepoint(mouse_pos)
        hard_clicked = self.button_hard.rect.collidepoint(mouse_pos)

        # Start game with specific settings depending on the button clicked
        if play_clicked and not self.game_active:
            self._start_game()
        elif easy_clicked and not self.game_active:
            self._start_game()
            self.settings.init_easy_settings()
        elif hard_clicked and not self.game_active:
            self._start_game()
            self.settings.init_hard_settings()


    def _check_keydown_events(self, event):
        """Process the keydowns"""
        if event.key == pygame.K_RIGHT:
            self.ship.r_direction.start_moving()
        elif event.key == pygame.K_LEFT:
            self.ship.l_direction.start_moving()
        elif event.key == pygame.K_ESCAPE:
            self._quit_game()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()
        elif event.key == pygame.K_1:
            self.settings.alien_speed = 1000
        elif event.key == pygame.K_2:
            for alien in self.armed_aliens:
                print(f"{alien.row}-{alien.col}", end="  ")
            print()


    def _check_keyup_events(self, event):
        """Process key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.r_direction.stop_moving()
        elif event.key == pygame.K_LEFT:
            self.ship.l_direction.stop_moving()


    def _start_game(self):
        """Set conditions for a new game"""
        # Restore game stats and settings
        self.game_active = True
        self.stats.reset_stats()
        self.sb._prep_images()
        self.settings.init_dynamic_settings()

        # Clear the screen
        self.aliens.empty()
        self.armed_aliens.empty()
        self.bullets.empty()
        self.enemy_bullets.empty()

        # Create new fleet and center ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide cursor
        pygame.mouse.set_visible(False)

            
    def _fire_bullet(self):
        """Create new instance of a bullet"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = ShipBullet(self, self.ship.rect)
            self.bullets.add(new_bullet)


    def _fire_enemy_bullet(self, alien_rect):
        """Create new alien bullet"""
        new_bullet = AlienBullet(self, alien_rect)
        self.enemy_bullets.add(new_bullet)


    def _spawn_enemy_bullet(self):
        """Create a new bullet from a random armed alien when timer elapses"""
        if self.eb_spawn_cd == 0:
            if len(self.armed_aliens):
                # Get a random alien on last row
                aliens_count = len(self.armed_aliens) - 1
                index = randint(0, aliens_count)
                chosen_alien = list(self.armed_aliens)[index]

                # Create a bullet based on its location
                self._fire_enemy_bullet(chosen_alien.rect)

                # Start cooldown timer
                self.eb_spawn_cd = self.settings.eb_spawn_cd

        # Decrement timer counter
        if self.eb_spawn_cd > 0:
            self.eb_spawn_cd -= 1


    def _update_enemy_bullets(self):
        """Manage enemy bullets on and of screen"""
        # Update enemy bullets and detect ship collisions
        self.enemy_bullets.update()

        # Delete bullets that have dissapeared
        for enemy_bullet in self.enemy_bullets.copy():
            if enemy_bullet.rect.top >= self.screen.get_rect().bottom:
                self.enemy_bullets.remove(enemy_bullet)

        # Look for enemy bullet-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.enemy_bullets):
            self._ship_hit()


    def _update_bullets(self):
        """Manage bullets on and of screen. Detect object hit"""
        # Update bullet positions
        self.bullets.update()

        # Delete bullets that have dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
        """Respond to collisions between bullets and aliens."""
        # Delete both of them when they overlap
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, not self.settings.bullet_invincible, True)
        
        if collisions:
            for alien_list in collisions.values():
                # Increase score for killed aliens
                self.stats.score += self.settings.alien_points * len(alien_list)
                for alien in alien_list:
                    # Enable shooting ofthe alien behind the killed one
                    self._re_arm_alien(alien)
            # Update the score and highscore image
            self.sb.prepare_score()
            self.sb.check_new_highscore()

        # When all aliens are killed, remove the remaining bullets and create a faster new fleet
        if not self.aliens:
            self._start_new_level()


    def _start_new_level(self):
        """Generate a faster new fleet and update level"""
        # Destroy existing bullets and create new fleet
        self.bullets.empty()
        self.enemy_bullets.empty()
        self.armed_aliens.empty()

        self._create_fleet()
        self.settings._speedup_game()

        # Level up
        self.stats.level += 1
        self.sb.prep_level()


    def _re_arm_alien(self, killed_alien):
        """When alien is shot, allow the one above to shoot"""
        suitable_aliens = []

        # List all aliens from the same column
        for alien in self.aliens.sprites():
            if alien.col == killed_alien.col:
                suitable_aliens.append(alien)

        # If they are not all killed, enable the lowes one
        if suitable_aliens:
            last_row = suitable_aliens[len(suitable_aliens)-1]
            self.armed_aliens.add(last_row)


    def _update_aliens(self):
        """Checks fleet collisions and escapes and update position"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()


    def _ship_hit(self):
        """Respond when alien collides with the ship"""
        if self.stats.ships_remaining > 1:
            # Move ship to default position
            self.ship.center_ship()

            # Clear the screen
            self.aliens.empty()
            self.armed_aliens.empty()
            self.bullets.empty()
            self.enemy_bullets.empty()

            # Create new fleet and pause game for half a second
            self._create_fleet()
            sleep(0.5)

            # Keypresses are stored during the pause. Clear all to avoid inital bullets 
            pygame.event.clear()

            # Clear move commands during the pause
            self.ship.r_direction.stop_moving()
            self.ship.l_direction.stop_moving()
        else:
            # No more lives. Game is stopped
            self.game_active = False
            pygame.mouse.set_visible(True)

        # Remove life and update indicator on status bar
        self.stats.ships_remaining -= 1
        self.sb.prep_lives()


    def _check_aliens_bottom(self):
        """Detects when aliens reach out of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        # Keep row and column numbering
        row, col = 0, 0
        
        while current_y < (self.settings.screen_height - 5*alien_height):
            # A new row is started, so reset column counter
            col = 0
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y, row, col)
                # Move current x to the end of the current alien + blank space
                current_x += 2*alien_width
                # Update column counter
                col += 1
            # Finished a row, reset x value and increment y value
            current_x = alien_width
            current_y += 2*alien_height
            # Advance to next row
            row += 1
        
        # Store fleet dimensions
        self.fleet_row_count = row
        self.fleet_col_count = col

        # Arm last row
        for alien in self.aliens.sprites():
            if alien.row == self.fleet_row_count-1:
                self.armed_aliens.add(alien)


    def _create_alien(self, x_position, y_position, row, col):
        """Create a single alien and place it in the row"""
        new_alien = Alien(self)

        # Place new alien in the grid
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.y = y_position
        new_alien.rect.y = y_position

        # Store the row and column number as a tuple
        new_alien.row, new_alien.col = row, col

        self.aliens.add(new_alien)          


    def _check_fleet_edges(self):
        """Checks if any alien has reached the end of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.y += self.settings.fleet_drop_speed
            alien.rect.y = alien.y
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Recolor the bg during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Draw all bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw enemy bullets
        for enemy_bullet in self.enemy_bullets.sprites():
            enemy_bullet.draw_bullet()

        # Draw the ship
        self.ship.blitme()

        # Draw fleet
        self.aliens.draw(self.screen)

        # Draw the score in the corner
        self.sb.draw_score()

        # Draw all buttons
        if not self.game_active:
            self.button_play.draw()
            self.button_easy.draw()
            self.button_hard.draw()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


    def _screen_mode(self):
        """Run in window or fullscreen mode depending on Settings"""
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
            

    def _quit_game(self):
        """Store highscore and exit program"""
        hs_path = pathlib.Path("highscore.txt")
        hs_path.write_text(str(self.stats.high_score))
        sys.exit()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()