"""
9-16. Python Module of the Week:

• One excellent resource for exploring the Python standard library
    is a site called Python Module of the Week.

• Go to https://pymotw.com/ and look at the table of contents.

• Find a module that looks interesting to you and read about it,
    perhaps starting with the random module.
"""

import textwrap
from textwrap_example import sample_text

def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0

class Wrapping:

    def __init__(self, text):
        """initialize the parameters in the class."""
        self.text = text

    def filler(self):
        """receives a text and produces a formatted text output."""
        print(textwrap.fill(self.text, width=50))

    def dedenter(self):
        """receives a text and deletes the default indentation."""
        dedented_text = textwrap.dedent(self.text)
        print('Dedented:')
        print(dedented_text)

    def dedenter_filler(self):
        """Combines methods fill() and dedent()"""
        dedented_text = textwrap.dedent(self.text).strip()
        for width in [45, 60]:
            print('{} Columns:\n'.format(width))
            print(textwrap.fill(dedented_text, width=width))
            print()

    def blocks_indenter(self):
        """Indent blocks and adds a prefix"""
        dedented_text = textwrap.dedent(self.text)
        wrapped = textwrap.fill(dedented_text, width=50)
        wrapped += '\n\nSecond paragraph after a blank line.'
        final = textwrap.indent(wrapped, '> ')

        print('Quoted block:\n')
        print(final)

    def new_line_prefix_indent(self):
        """
        To control which lines receive the new prefix, pass a callable as
        the predicate argument to indent(). The callable will be invoked for
        each line of text in turn and the prefix will be added for lines
        where the return value is true.
        This example adds the prefix EVEN to lines that contain an even
        number of characters.
        NOTE: this method uses the static-method `should_indent`.
        """
        dedented_text = textwrap.dedent(self.text)
        wrapped = textwrap.fill(dedented_text, width=50)
        final = textwrap.indent(wrapped, 'EVEN ',
                                predicate=should_indent)

        print('\nQuoted block:\n')
        print(final)

    def indent_hanger(self):
        """Controls first line indent as subsequent indents."""
        dedented_text = textwrap.dedent(self.text).strip()
        print(textwrap.fill(dedented_text,
                            initial_indent='',
                            subsequent_indent=' ' * 4,
                            width=50,
                            ))

    def truncate_text(self):
        """
        Whitespaces, tabs, newlines and series of multiple spaces will be
        standardized to a one space. The text will be truncated to a
        length less-than or equal-to what is requested between word boundaries
        so that no partial words are included.
        """
        dedented_text = textwrap.dedent(self.text)
        original = textwrap.fill(dedented_text, width=50)

        print('Original:\n')
        print(original)

        shortened = textwrap.shorten(original, 100)
        shortened_wrapped = textwrap.fill(shortened, width=50)

        print('\nShortened:\n')
        print(shortened_wrapped)

text_wrapper = Wrapping(sample_text)
text_wrapper.truncate_text()