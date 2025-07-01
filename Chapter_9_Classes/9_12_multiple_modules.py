### 9-12. Multiple Modules:

import admin_9_12 as au

my_user = au.Admin("Miro", "Mirov", "miro@bosch.com", "male",
                   "can do everything", "can reinstall BIOS", "can install linux")

my_user.privileges.show_privileges()
my_user.add_privilege("can play god")
my_user.add_privilege("can fix stuff")
my_user.privileges.show_privileges()
