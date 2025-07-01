### 9-11. Imported Admin:

from login_9_11 import Admin

my_user = Admin("Boyan", "Sabchev", "bs@bosch.com", "male",
                "can delete sys32", "install drivers", "watch twitch")

my_user.describe_user()
my_user.privileges.show_privileges()