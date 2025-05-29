"""
9-11. Imported Admin:

• Start with your work from Exercise 9-8 (page 173).

• Store the classes User, Privileges, and Admin in one module.

• Create a separate file, make an Admin instance, and call
    show_privileges() to show that everything is working correctly.

"""
from privileges import Admin
admin = Admin('michael',
                   'jackson',
                   25,
                   'u.s.a.',
                   5.9,
                   136
                   )
admin.admin_info()
admin.privileges.show_privileges()