"""
2-7. Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip()
"""
person = "\n ludwikl. \t\tzamenhof "
print(f"'{person}' ::: no strip")
print(f"'{person.rstrip()}' ::: right strip")
print(f"'{person.lstrip()}' ::: left strip")
print(f"'{person.strip()}' ::: general strip")
