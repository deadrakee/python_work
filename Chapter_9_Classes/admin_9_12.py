"""Module for creation of priviledged users"""

from user_9_12 import *

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
