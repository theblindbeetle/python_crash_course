# Chapter 3: Introducing Lists
### Lists allow you to store sets of information in one place, whether you have just a few items or millions of items. Lists are one of Python’s most powerful features readily accessible to new programmers, and they tie together many important concepts in programming.

---
## What Is a List?
A list is a collection of items in a particular order.<br>
Lists can include the letters of the alphabet, the digits from 0-9,or the names of your family.<br>
You can put anything you want into a list, and the items don't need to be related. 
A list commonly contain more than one element, so, it's a good idea to make the name plural, such as <i>letters</i>, <i>digits</i>, or <i>names</i>.<br>
<br>
In Python square brackets ([]) indicate a list, and individual elements in the list are separated by commas.<br>
Here's a example of a list that contain a few kind of bicycles.
```commandline
# REFER: bicycle.py
>>> bicycles = ['treck', 'cannondale', 'redline', 'specialized']
>>> print(bicycles)
```
When you print a list in Python, it returns a representation of that list including the square brackets.
```commandline
['trek', 'cannondale', 'redline', 'specialized']
```
But you don't want your used to see this.

### Accessing Elements in a List
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
Since lists are ordered elements, you can tell python which position (or index) you desired to access.<br>
When you ask for just one element it is returned without square brackets.
```commandline
>>> bicycles = ['treck', 'cannondale', 'redline', 'specialized']
>>> print(bicycles[0])
trek
```
This is what you want your user to see. A clean, neatly formatted output.<br>
Also, you can combine with the <i>String</i> methods from Chapter 2 on any element of the list.<br>
You can use, for example, the `title()` method:
```commandline
>>> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>>> print(bicycles[0].title())
Trek
```
This is the same output as the previous, but capitalized, which, if required, can improve the output formatting.

### Index Position Start at 0, Not 1
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
Python consider the first element in a list to be at position 0, not 1. The second item in the list is 1.<br>
The following example asks for the bicycles at index 1 and index 2:

```commandline
>>> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>>> print(bicycles[1].title())
Cannondale
>>> print(bicycles[2].upper())
REDLINE
```
Python has a special syntax where, by asking for the element at index -1, it returns the last element in the list:
```commandline
>>> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>>> print(bicycles[-1])
specialized
```
The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end, and so forth.

### Using Individual Values from a List
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
The values from a list can be use individually as any other variable.
You can use f-string to create a message based on a value from a list.
For example:
```commandline
>>> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>>> message = f"My first bycicle was a {bicycles[-1].title()}."
My first bycicle was a Specialized. 
```

---
## Changing, Adding, and Removing Elements
Most of the list are dynamic, that means you can build it and then modify it (by adding or removing elements) while the program runs its course.<br>
For example you can have a game in which a player has to shoot aliens out of the sky. So, you will require the following actions:
1. Store the initial set of aliens in a list.
2. Remove an alien from the list each time one is shot down.
3. Each time a new alien appears on the screen, you add it to the list.

So, your list of aliens will increase and decrease in length throughout the course of the game.

### Modifying Elements in a List
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
The syntax of modifying is similar to the one of accessing an element in a list.<br>
Just call the list and element (in brackets) you want to modify and assign the new value.
```commandline
# REFER: motorcycles.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```
The output is:
```commandline
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```
Any value of the list can be changed, not just the first one.

### Adding Elements to a List
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
You might want to add a new element to a list for many reasons. For
example, you might want to make new aliens appear in a game, add new
data to a visualization, or add new registered users to a website you’ve
built. Python provides several ways to add new data to existing lists

#### Appending Elements to the End of a List
Appending elements is the easiest way to add elements into a list.
```commandline
# REFER: motorcycles2.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
```
The `apend()` adds 'ducati' to the end of the list without affecting any of the other elements.
```commandline
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

With the `append()` method is easy to build lists dynamically.<br>
You can create an empty list and add items when it is required.
```commandline
# REFER: motorcycles3.py
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
```
it outputs:
```commandline
['honda', 'yamaha', 'suzuki']
```

#### Inserting Elements into a List
You can also insert a new element at any position of the list by pointing to the index.<br>
if you point to the index 0, it will be added in the first position of the list:
```commandline
# REFER: motorcycles4.py
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
```
Call the list created (motorcycles), add the method (motorcycles.insert()) and add the parameters '__index' and '__value' to the method (motorcycles.insert(0, 'ducati')).<br>
the output is:
```commandline
['ducati', 'honda', 'yamaha', 'suzuki']
```

### Removing Elements from a List
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
An item can be removed accoding to its position in the list or according to its value.

#### Removing an Item Using the del Statement
If you know the position of the item you want to remove, you can use `del` statement:

```commandline
# REFER: motorcycles5.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```
This action removes the item on the position 0, The data left in the list is:
```commandline
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```
You can remove any element from the list by knowing its position. Following statement deletes the third element (position 2)
```commandline
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[2]
print(motorcycles)
```

#### Removing an Item Using the pop() Method
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
The `pop()` method removes the last element from the list, but it let you use that item after removing it.<br>
The term 'pop' comes from thinking on a stack of items and popping one item off the top of the stack, considering in this analogy the top of the stack as the end of the list.

```commandline
# REFER: motorcycles6.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```
* First we define the list.
* We print the list.
* Then we popped the last element of the list (suzuki), and assign it to the variable `popped_motorcycle`.
* We print the list after popping the element.
* We print the popped element.

Here is the output:
```commandline
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```
Here is an example of usage of the `pop()` method:<br>
1. You work in a store which have a warehouse with products with expiration date.<br>
2. You need to have stock so that it doesn't run out. <br>
3. When you bring new more products to the warehouse you put the at the first position of the list (position 0)
4. When you pop a product is the one with more time in the warehouse
```commandline
products = ['corn_id_100','corn_id_99','corn_id_98']
print(products)

products.insert(0, 'corn_id_101')
print(products)

popped_product = products.pop()
print(products)
print(f"The product taken off the warehous is: {popped_product}") 
```
The output is:
```commandline
['corn_id_100', 'corn_id_99', 'corn_id_98']
['corn_id_101', 'corn_id_100', 'corn_id_99', 'corn_id_98']
['corn_id_101', 'corn_id_100', 'corn_id_99']
The product taken off the warehous is: corn_id_98
```

#### Popping Items from any Position in a List
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
Also, you can use the `pop()` method specifying what element you want to pop.<br>
Using the 
1. You work in a store which have a warehouse with products with expiration date.<br>
2. You need to have stock so that it doesn't run out. <br>
3. When you bring new more products to the warehouse you put the at the last position of the list (append())
4. When you pop a product is the one with more time in the warehouse

```commandline
products = ['corn_id_98', 'corn_id_99', 'corn_id_100']
print(products)

products.append('corn_id_101')
print(products)

popped_product = products.pop(0)
print(products)
print(f"The product taken off the warehous is: {popped_product}") 
```
Notice the order of the products is inverse compare with the previous example.<br>
Both examples have the same purpose and behavior, but different ways of adding values and taking the off.<br>
Here is the output:
```commandline
['corn_id_98', 'corn_id_99', 'corn_id_100']
['corn_id_98', 'corn_id_99', 'corn_id_100', 'corn_id_101']
['corn_id_99', 'corn_id_100', 'corn_id_101']
The product taken off the warehous is: corn_id_98
```

#### Removing an Item by Value
You may not be able to know the position of the item, so you can remove an element from the list if you know its value.
```commandline
# REFER: motorcycles7.py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
```
This is pretty straight forward, and the output is:
```commandline
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```
You can also use the `remove()` method to work with a value that is being remove from the list.
```commandline
# REFER: motorcycles8.py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
```
As using the `remove()` method also require to define the value to remove from the list, we can use that value (in this case from the variable `too_expensive`) to work with it.<br>
Here's the output:
```commandline
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

A Ducati is too expensive for me.
```

## Organizing a List
Python provides a number of different ways to organize your lists, depending on the situation.

### Storing a List Permanently with the sort() Method
In the following example you'll see a list alphabetically disordered.<br>
This way sorts the list by changing its order permanently.
```commandline
# REFER: cars.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```
the output after using the method is an ordered list:
```commandline
['audi', 'bmw', 'subaru', 'toyota']
```
you can also sort the list backwards:
```commandline
# REFER: cars2.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```
the output:
```commandline
['toyota', 'subaru', 'bmw', 'audi']
```

### Sorting a List Temporarily with the sorted() Function
Using this method just shows the list sorted, but it doesn't modify it.
```commandline
# REFER: cars3.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Original list:{cars}")
print(f"Sorted list:{sorted(cars)}")
print(f"Original list:{cars}")
```
the output:
```commandline
Original list:['bmw', 'audi', 'toyota', 'subaru']
Sorted list:['audi', 'bmw', 'subaru', 'toyota']
Original list:['bmw', 'audi', 'toyota', 'subaru']
```
The list still exist in the original order, even when sorted() has been used.
This method also accepts `reverse=True`
> NOTE: when not all the values are in lowercase, it is mor complicated to sort alphabetically.

### Printing a List in Reverse Order
The method reverse() does not order alphabetically backwards, it just backwards the current order of the list.
```commandline
# REFER: cars4.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Original list:{cars}")
cars.reverse()
print(f"Reversed list:{cars}")
```
the output:
```commandline
Original list:['bmw', 'audi', 'toyota', 'subaru']
Reversed list:['subaru', 'toyota', 'audi', 'bmw']
```
Important to mention that this method modifies permanently the order of the list. But if required, reverse it again would change it to the original order.

### Finding the Lenght of a List
The method len(), with a list returns the number of items in that list.
```commandline
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
```

## Avoiding Index Errors When Working with Lists
A common error is when work with lists for the first time is like you have a list with three items, and you ask for the fourth one:
```commandline
# REFER: motorcycles3.4.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
```
This results in error:
```commandline
Traceback (most recent call last):
  File "motorcycles.py", line 2, in <module>
    print(motorcycles[3])
          ~~~~~~~~~~~^^^
IndexError: list index out of range
```
Python tries to get the item in the index 3, but there are just up to 2 ([0, 1, 2]).<br>
Keep in mind that whenever you want to access the last item you can use [-1].
```commandline
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])
```
the output:
```commandline
suzuki
```
The only way to get an error with this approach is that the list is empty
```commandline
motorcycles = []
print(motorcycles[-1])
```
the output:
```commandline
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range
```

> NOTE: When an index error occurs you can have a good hint by printing the list.

