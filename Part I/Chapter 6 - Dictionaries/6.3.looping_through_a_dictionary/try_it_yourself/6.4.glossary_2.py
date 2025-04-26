"""
6-4. Glossary 2:
Now that you know how to loop through a dictionary,
    • Clean up the code from Exercise 6-3 (page 99) by replacing your series of
    print() calls with a loop that runs through the dictionary’s keys and values.
    • When you’re sure that your loop works, add five more Python terms to your
    glossary.
    • When you run your program again, these new words and meanings should
    automatically be included in the output.
"""

glossary = {
    'comprehension list': 'it is a way of creating a new list while looping through it.',
    'loop': 'it is a cycle, that is used to go through elements (or objects) with multiple values within it.',
    'if': 'it is a tests that validates whether a condition is accomplished or not.',
    'dictionary': 'it is an object that can contain multiple key-value paris.',
    'variable': 'it is the label that points to some data stored by Python.',
    'list': 'it is a type of data that contains a series of elements that can be same or different type'
}

# print(f"comprehension lists:\n\t{glossary['comprehension list']}")
# print(f"\nloop:\n\t{glossary['loop']}")
# print(f"\nif:\n\t{glossary['if']}")

# Step 1.
for key, value in glossary.items():
    print(f"{key.title()}: \n\t{value.lower()}")