"""
5-2. More Conditional Tests:
You don’t have to limit the number of tests you create to ten.
If you want to try more comparisons, write more tests
and add them to conditional_tests.py.
Have at least one True and one False result for each of the following:

•  Tests for equality and inequality with strings
•  Tests using the lower() method
•  Numerical tests involving equality and inequality, greater than and less than,
    greater than or equal to, and less than or equal to
•  Tests using the `and` keyword and the `or` keyword
•  Test whether an item is in a list
•  Test whether an item is not in a list
"""
i = 0
# Tests for equality and inequality with strings

str_1 = "Hello world!"
str_2 = "Hello world!"
str_3 = "Hello pyhoneer!"
i += 1
print(f"\nOUTPUT TEST {i}")
print(str_1 == str_2)
print(str_1 == str_3)

# Tests using the lower() method
str_2 = "hello world!"
i += 1
print(f"\nOUTPUT TEST {i}")
print(str_1.lower() == str_2)
print(str_1 == str_2)

# Numerical tests involving equality √(==) and inequality(!=), greater than (>) and less than(<),
# greater than or equal to (>=), and less than or equal to (<=)
i += 1
print(f"\nOUTPUT TEST {i}")
expected_goals = 50
print(f"2025 Co. yearly goals accomplished: {expected_goals == 50}")
print(f"2024 Co. yearly goals accomplished: {expected_goals == 60}")
age = 99
print(f"You're a centenarian: {age != 100}")
age = 100
print(f"You're a centenarian: {age != 100}")

age = 23
print(f"You're an adult in Mississippi: {age > 20}")
print(f"You're underage in Mississippi: {age < 21}")

product_1 = 45
print(f"Enough product units on the shelves:{product_1 >= 45}")
print(f"You need more product units in the warehouse:{product_1 <= 10}")

# Tests using the `and` keyword and the `or` keyword
i += 1
print(f"\nOUTPUT TEST {i}")
coins_score = 50
user_coins = 52
capture_score = 1005
user_captures = 300


if coins_score < user_coins or capture_score < user_captures:
    print(f"You set a new record!\n\tCOINS: {user_coins}/{coins_score}"
          f"\n\tCAPTURES: {user_captures}/{capture_score}")

user_coins = 60
user_captures = 1300
if coins_score < user_coins and capture_score < user_captures:
    print(f"YOU SET THE BEST RECORD!!!!!!!\n\tCOINS: {user_coins}/{coins_score}"
          f"\n\tCAPTURES: {user_captures}/{capture_score}")

# Test whether an item is in a list
i += 1
print(f"\nOUTPUT TEST {i}")
items = ['dog','bear']
item = 'dog'
if item in items:
    print(f"{item} is in the list.")

# Test whether an item is not in a list
i += 1
print(f"\nOUTPUT TEST {i}")
items = ['dog','bear']
item = 'cat'
if item not in items:
    print(f"{item} is not in the list.")