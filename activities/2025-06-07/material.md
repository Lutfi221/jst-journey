Python Learning Materials: Lists & Dictionaries
Welcome! Before you start building the mini-projects, this document will be your guide to understanding two of the most powerful tools in Python: Lists and Dictionaries. Master these, and you'll be able to build all sorts of amazing programs, including Hangman.

Module 1: Deep Dive into Lists
Imagine you want to keep track of all the planets in our solar system, or all the scores you've ever gotten in a game. Instead of creating a new variable for each one (planet1 = "Mercury", planet2 = "Venus"), you can hold them all in a single container called a list.

A list is an ordered collection of items. "Ordered" simply means that the items stay in the same position you put them in.

Creating a List
You create a list by placing items inside square brackets [], separated by commas.

```python
# A list of strings
planets = ["Mercury", "Venus", "Earth", "Mars"]

# A list of numbers (integers)
high_scores = [250, 199, 150, 99]

# A list can even contain different data types
mixed_list = ["Budi", 17, "Jakarta", True]

# An empty list
empty_list = []

print(planets)
print(high_scores)
```

Accessing Items by Index
Because lists are ordered, every item has a position, called an index. In Python, indexing starts at 0.

To get an item, you use the list's name followed by the index in square brackets.


```python
fruits = ["Apple", "Banana", "Cherry", "Durian"]

# Get the first item (index 0)
first_fruit = fruits[0]
print("The first fruit is:", first_fruit) # Output: The first fruit is: Apple

# Get the third item (index 2)
third_fruit = fruits[2]
print("The third fruit is:", third_fruit) # Output: The third fruit is: Cherry

```python

You can also use negative indexes to count from the end of the list. -1 refers to the last item, -2 to the second-to-last, and so on.

```python
# Get the last fruit
last_fruit = fruits[-1]
print("The last fruit is:", last_fruit) # Output: The last fruit is: Durian
```

Checking if an Item is in a List
A very common task is to check if a value exists in a list. The in keyword makes this easy. It returns True or False.

```python
guest_list = ["Ani", "Budi", "Eko", "Wati"]

# Check if "Eko" is on the list
if "Eko" in guest_list:
    print("Yes, Eko is on the guest list.")
else:
    print("No, Eko is not on the guest list.")

# Check for a name that isn't there
if "Siti" in guest_list:
    print("Yes, Siti is on the guest list.")
else:
    print("No, Siti is not on the guest list.")
```

This will be extremely useful for Hangman to check if a guessed letter is in the secret word!

Getting the Length of a List
To find out how many items are in a list, use the len() function.

```python
numbers = [10, 20, 30, 40, 50, 60]
item_count = len(numbers)
print("The list has", item_count, "items.") # Output: The list has 6 items.
```

Adding and Removing Items
Lists are dynamic, meaning you can change them after you create them.

Adding with .append()
The .append() method adds an item to the end of the list.
```
tasks = ["Clean room", "Do homework"]
print("Tasks before:", tasks)

tasks.append("Feed the cat")
print("Tasks after:", tasks) # Output: Tasks after: ['Clean room', 'Do homework', 'Feed the cat']
```

Removing with .remove()
The .remove() method removes the first matching value from a list.

```python
tools = ["Hammer", "Screwdriver", "Wrench", "Screwdriver"]
print("Tools before:", tools)

tools.remove("Screwdriver") # This will only remove the first "Screwdriver"
print("Tools after:", tools) # Output: Tools after: ['Hammer', 'Wrench', 'Screwdriver']
```

Important: If you try to .remove() an item that doesn't exist, your program will crash with an error. It's always a good idea to check if item in list: before removing it.

Looping Through a List
You can easily perform an action on every item in a list using a for loop.

```python
# Printing every member of a team
team_members = ["Pikachu", "Charmander", "Squirtle"]

print("My team consists of:")
for member in team_members:
    print("- " + member)
```

Module 2: Understanding Dictionaries
Now, let's look at another type of container: a dictionary.

While a list is an ordered set of items, a dictionary is an unordered collection of key: value pairs. Think of it like a real dictionary: you look up a word (the key) to find its definition (the value). The order of entries doesn't matter.

Creating a Dictionary
You create a dictionary using curly braces {}. Each entry consists of a key, a colon :, and a value.

```python
# A dictionary to store a student's information
student = {
    "name": "Budi",
    "age": 15,
    "city": "Jakarta",
    "is_active": True
}

# A dictionary for monster stats
monster = {
    "name": "Goblin",
    "hp": 50,
    "attack": 8,
    "weakness": "Fire"
}

# An empty dictionary
empty_dict = {}

print(student)
print(monster)
```

Keys are usually strings, but they can be numbers. Values can be any data type (string, number, boolean, or even another list or dictionary!).

Accessing Values Using Keys
You don't use indexes with dictionaries. Instead, you use the key in square brackets to get its corresponding value.

```python
player_profile = {
    "username": "Gamer123",
    "level": 25,
    "guild": "The Avengers"
}

# Get the player's username
player_name = player_profile["username"]
print("Player's name is:", player_name) # Output: Player's name is: Gamer123

# Get the player's level
level = player_profile["level"]
print("Player's level is:", level) # Output: Player's level is: 25
```

Important: If you try to access a key that doesn't exist, your program will crash.

Adding or Updating Entries
Adding a new key:value pair or updating an existing one is easy.

```python
# Starting with a simple user profile
user_settings = {
    "theme": "dark",
    "language": "English"
}

# Add a new setting
user_settings["notifications"] = "on"
print("Settings after adding:", user_settings)

# Update an existing setting
user_settings["theme"] = "light"
print("Settings after updating:", user_settings)
```

Checking if a Key Exists
Just like with lists, you can use the in keyword to check if a key exists in a dictionary before you try to access it. This helps avoid errors.

```python
car = {
    "brand": "Toyota",
    "model": "Avanza"
}

if "brand" in car:
    print("This car's brand is:", car["brand"])

if "year" in car:
    print("This car's year is:", car["year"])
else:
    print("The 'year' key was not found in the dictionary.")
```

Looping Through a Dictionary
You can loop through a dictionary in a few ways.

Looping Through Keys
By default, a for loop over a dictionary gives you its keys.

```python
capitals = {
    "Indonesia": "Jakarta",
    "Japan": "Tokyo",
    "France": "Paris"
}

print("Countries:")
for country in capitals:
    print(country)
```

Looping Through Values with .values()
If you only need the values, use the .values() method.

```python
print("\nCapitals:")
for city in capitals.values():
    print(city)

Looping Through Keys and Values with .items()
The most common way is to get both the key and the value at the same time using the .items() method.

print("\nCountries and their Capitals:")
for country, city in capitals.items():
    print(f"The capital of {country} is {city}.")
```

You are now equipped with the fundamental knowledge of lists and dictionaries! Proceed to the mini-projects to put this knowledge into practice.