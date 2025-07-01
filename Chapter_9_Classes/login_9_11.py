"""Module containing information for creating users"""

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
        """Increment internal counter by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Set internal counter by 0"""
        self.login_attempts = 0


class Admin(User):
    """User with elevated privileges"""

    def __init__(self, first_name, last_name, email, gender, *privileges):
        """Construct Admin"""
        super().__init__(first_name, last_name, email, gender)
        self.privileges = Privileges(privileges)

    def add_privilege(self, new_priv):
        """Add priv only through admin stuff"""
        if(new_priv != "can install virus"):
            self.privileges.add_privilege(new_priv)
        else:
            print("Admin restricts you from viruses. Abort adding..")


class Privileges:
    """Contains privileges"""

    def __init__(self, privileges):
        """Construct privileges object with one param with type List"""
        self.privileges = list(privileges)

    def show_privileges(self):
        """Print list"""
        print(f"Admin's privileges: {self.privileges}")

    def add_privilege(self, new_priv):
        """Add to the list of privileges"""
        if(new_priv != "can play god"):
            self.privileges.append(new_priv)
        else:
            print("You cant play God. Abort adding..")
