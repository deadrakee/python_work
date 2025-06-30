### 9-7. Admin:

class User:
    """Representation of a user"""

    def __init__(
            self, first_name, last_name,
            email, gender):
        """Construct user"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.login_attempts = 0


    def describe_user(self):
        """print all info for a user"""
        print(
            f"\nUser info:\n\t{self.first_name}"
            f"\n\t{self.last_name}"
            f"\n\t{self.email}"
            f"\n\t{self.gender}")
        

    def greet_user(self):
        """Prints hello message"""
        print(f"\nGreetings {self.first_name} {self.last_name}!")


    def increment_login_attempts(self):
        """Increment internal conter by 1"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Set internal conter by 0"""
        self.login_attempts = 0


class Admin(User):
    """User with elevated privileges"""

    def __init__(self, first_name, last_name, email, gender, privileges):
        """Constrct Admin"""
        super().__init__(first_name, last_name, email, gender)
        self.privileges = privileges


    def show_privileges(self):
        """Print list"""
        print(f"\nAdmin's privileges: {self.privileges}")


admin_privileges = ["can add post", "can delete post", "can ban user"]

my_user = Admin("Stefan", "Mechkata", "stef@bosch.com", "male", admin_privileges)
my_user.describe_user()
my_user.show_privileges()