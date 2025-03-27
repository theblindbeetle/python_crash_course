"""
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy food:")
for my_food in my_foods:
    print(f"\n{my_food}")
print(("\nFriends' food:").upper())
for his_food in friend_foods:
    print(f"\n{his_food}")