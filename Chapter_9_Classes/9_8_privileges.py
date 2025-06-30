### 9-8. Privileges:

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

    def __init__(self, first_name, last_name, email, gender, *privileges):
        """Constrct Admin"""
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



admin_privileges = ["can add post", "can delete post", "can ban user"]
my_user = Admin("Stefan", "Mechkata", "stef@bosch.com", "male", "can add post", "can delete post", "can ban user")

my_user.describe_user()
my_user.privileges.show_privileges()

# Add aditional ability to Admin by modifying internal stuff of Privileges class
print("\n\n-------\nAdding by touching internal Preference stuff:")
my_user.privileges.privileges.append("can play god")
my_user.privileges.show_privileges()

# Add aditional element by limiting internal modification of Privilege, but still
# modifying internal Admin stuff. At least some verification is added
print("\n\n--------\nAdding by Preference API:")
my_user.privileges.add_privilege("can play god")
my_user.privileges.add_privilege("can install drivers")
my_user.privileges.show_privileges()

# Add element by the top class without knowing whats inside. Verification is done on all levels
print("\n\n--------\nAdding by User top level:")
my_user.add_privilege("can install virus")
my_user.add_privilege("can play god")
my_user.add_privilege("can exchange matrix")
my_user.privileges.show_privileges()