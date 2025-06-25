### 9-3. Users:

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

        
user1 = User("Krasi", "R1", "goshev@gmail.com", "alfa")
user2 = User("Viktor", "Bojkov", "hakera@bosch.com", "male")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()