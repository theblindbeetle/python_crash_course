"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
    However, to avoid confusion, let’s call it a glossary.

•  Think of five programming words you’ve learned about in the previous
    chapters. Use these words as the keys in your glossary, and store their
    meanings as values.

•  Print each word and its meaning as neatly formatted output. You might
    print the word followed by a colon and then its meaning, or print the word
    on one line and then print its meaning indented on a second line. Use the
    newline character (\n) to insert a blank line between each word-meaning
    pair in your output.
"""

glossary = {
    'comprehension list': 'Is a way of creating a new list while looping through it.',
    'loop': 'It is a cycle, that is used to go through elements (or objects) with multiple values within it.',
    'if': 'It is a tests that validates whether a condition is accomplished or not.',
}

print(f"Comprehension lists:\n\t{glossary['comprehension list']}")
print(f"\nloop:\n\t{glossary['loop']}")
print(f"\nif:\n\t{glossary['if']}")