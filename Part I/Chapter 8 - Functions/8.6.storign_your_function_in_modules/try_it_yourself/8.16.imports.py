"""
8-16. Imports:

• Using a program you wrote that has one function in it store that function in a
    separate file.

• Import the function into your main program file, and call the function using
each of these approaches:
----------------------------------------------
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
----------------------------------------------
"""
# import imports_pets # 1st way
# from imports_pets import describe_pet # 2nd way
# from imports_pets import describe_pet as dp # 3rd way
# import imports_pets as ip # 4th way
from imports_pets import * # 5th way

# # 1st way
# imports_pets.describe_pet('hamster', 'peter pettigrew')
# imports_pets.describe_pet(pet_name='peter pettigrew', animal_type='hamster')

# # 2nd way
# describe_pet('hamster', 'peter pettigrew')
# describe_pet(pet_name='peter pettigrew', animal_type='hamster')

# # 3rd way
# dp('hamster', 'peter pettigrew')
# dp(pet_name='peter pettigrew', animal_type='hamster')

# # 4th way
# ip.describe_pet('hamster', 'peter pettigrew')
# ip.describe_pet(pet_name='peter pettigrew', animal_type='hamster')

# 5th way
describe_pet('hamster', 'peter pettigrew')
describe_pet(pet_name='peter pettigrew', animal_type='hamster')