"""
8-15. Printing Models:

• Put the functions for the example printing_models.py in a separate file
    called printing_functions.py.

• Write an import statement at the top of printing_models.py,

• Modify the file to use the imported functions.
"""

from printing_functions import print_models, show_completed_models


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)