"""
9-12. Multiple Modules:

• Store the User class in one module,
    • and store the Privileges
    • and Admin classes in a separate module.

• In a separate file, create an Admin instance and call
    show_privileges() to show that everything is still working correctly.
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