Of course, here's the homework assignment based on the materials and instructions you provided.

# Python Homework: From Lists to Dictionaries

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

-----

## The Problem with Parallel Lists

So far, we've used separate lists to keep track of our weapon data: one for names, one for strengths, and one for durabilities.

```python
weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]
weapon_durabilities = [20, 50, 25]
```

This works, but it can be risky. What if you add a new weapon but forget to add its strength? The lists would become out of sync, and your program would have bugs.

A much better way is to group all the information for a single weapon into one place. We can do this by using a **list of dictionaries**. Each dictionary in the list will represent one weapon, holding all of its properties (name, strength, durability) together. This keeps our data organized and reliable.

Let's refactor our code to use this improved structure!

## Initial Setup

Start with the following code in your Python file. It shows the old way of printing and begins setting up our new `weapons` list.

```python
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]
weapon_durabilities = [20, 50, 25]

n_weapon_names = len(weapon_names)

print("# Iterating over weapon names, durabilities, and strengths using `for ... in range(...)")
for i in range(n_weapon_names):
    no = i + 1
    weapon_strength = weapon_strengths[i]
    weapon_name = weapon_names[i]
    weapon_durability = weapon_durabilities[i]
    print(str(no) + ". " + weapon_name + " (durability: " + str(weapon_durability) + ", strength: " + str(weapon_strength) + ")")

weapons = []

spear = {
    "name": "Spear",
    "durability": 20,
    "strength": 4,
}

weapons.append(spear)

# Your code for the next steps will go here
```

-----

## Step 1: Creating the Full List of Dictionaries

### Problem

Right now, the `weapons` list only contains the "Spear" dictionary. Your task is to create dictionaries for "Mjolnir" and "Sword" and add them to the `weapons` list.

  * Create a dictionary for "Mjolnir" with a durability of 50 and a strength of 25.
  * Append the Mjolnir dictionary to the `weapons` list.
  * Create a dictionary for "Sword" with a durability of 25 and a strength of 7.
  * Append the Sword dictionary to the `weapons` list.

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  * Follow the pattern used for the `spear` dictionary. Create a new variable for each weapon's dictionary.
  * A dictionary is created with curly braces `{}` and key-value pairs like `"name": "Mjolnir"`.
  * Use the `weapons.append()` method to add each new dictionary to the `weapons` list.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
mjolnir = {
    "name": "Mjolnir",
    "durability": 50,
    "strength": 25,
}

weapons.append(mjolnir)

sword = {
    "name": "Sword",
    "durability": 25,
    "strength": 7,
}

weapons.append(sword)
```

</details>

-----

## Step 2: Displaying the New Structure

### Problem

Now that your `weapons` list is complete, let's see what it looks like. Print the `divider`, a title, and then the entire `weapons` list.

Your output for this step should be:

```
... (previous output) ...

------------
# Combining the power of lists and dictionaries:
[{'name': 'Spear', 'durability': 20, 'strength': 4}, {'name': 'Mjolnir', 'durability': 50, 'strength': 25}, {'name': 'Sword', 'durability': 25, 'strength': 7}]
```

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * Use the `print()` function to display the `divider` variable first.
  * Then, `print()` the title string.
  * Finally, `print()` the `weapons` variable directly to see its contents.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
print(divider)

print("# Combining the power of lists and dictionaries:")

print(weapons)
```

</details>

-----

## Step 3: Looping with `for ... in`

### Problem

Printing the whole list is useful for debugging, but not very readable for a user. Let's iterate through the `weapons` list using a `for ... in` loop to print the details of each weapon on separate lines.

Your output for this step should be:

```
... (previous output) ...

------------
# Iterating over weapons using `for ... in weapons` loop:
name: Spear
durability: 20
strength: 4

name: Mjolnir
durability: 50
strength: 25

name: Sword
durability: 25
strength: 7
```

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * Your loop will look like `for weapon in weapons:`. Inside the loop, the `weapon` variable will be a dictionary on each iteration.
  * To get a value from the dictionary, use its key in square brackets, like `weapon["name"]` or `weapon["strength"]`.
  * Remember to convert numeric values to strings with `str()` before combining them with other text for printing.
  * Use an empty `print()` at the end of the loop to create a blank line between weapons.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
print(divider)

print("# Iterating over weapons using `for ... in weapons` loop:")

for weapon in weapons:
    weapon_name = weapon["name"]
    weapon_durability = weapon["durability"]
    weapon_strength = weapon["strength"]
    print("name: " + weapon_name)
    print("durability: " + str(weapon_durability))
    print("strength: " + str(weapon_strength))
    print()
```

</details>

-----

## Step 4: Looping with `for ... in range(...)`

### Problem

Now, let's print the weapon data again, but this time as a numbered list. Use a `for ... in range(...)` loop to achieve this.

Your output for this step should be:

```
... (previous output) ...

------------
# Iterating over weapons using `for ... in range(...)` loop:
1. Spear (durability: 20, strength: 4)
2. Mjolnir (durability: 50, strength: 25)
3. Sword (durability: 25, strength: 7)
```

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * First, get the number of items in the `weapons` list using `len()`.
  * Your loop will be `for i in range(n_weapons):`.
  * Inside the loop, use the index `i` to get the weapon dictionary: `weapon = weapons[i]`.
  * Then, you can access the values like `weapon["name"]`.
  * The number for the list can be `i + 1`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
print(divider)

n_weapons = len(weapons)

print("# Iterating over weapons using `for ... in range(...)` loop:")

for i in range(n_weapons):
    no = i + 1
    weapon = weapons[i]
    weapon_name = weapon["name"]
    weapon_durability = weapon["durability"]
    weapon_strength = weapon["strength"]
    print(str(no) + ". " + weapon_name + " (durability: " + str(weapon_durability) + ", strength: " + str(weapon_strength) + ")")
```

</details>

-----

## Step 5: Creating a Reusable Function

### Problem

The numbered list format is very useful. Let's make it reusable by putting the code from Step 4 into a function.

1.  Define a function called `print_weapons` that takes one argument (the list of weapons).
2.  Move the `for ... in range(...)` loop from the previous step inside this function.
3.  Call the new `print_weapons` function, passing your `weapons` list to it.

The output should be the same as in Step 4.

### Hint

<details>
<summary>Stuck on Step 5? Click for a hint!</summary>

  * Your function definition will be `def print_weapons(weapons_list):`.
  * The code inside the function will be the same as your solution for Step 4, but it should use the parameter `weapons_list` instead of the global `weapons` variable.
  * To call it, simply write `print_weapons(weapons)`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 5? Click to reveal!</summary>

```python
print(divider)

print("# Defining a function to show all our weapons")

def print_weapons(weapons):
    n_weapons = len(weapons)
    for i in range(n_weapons):
        no = i + 1
        weapon = weapons[i]
        weapon_name = weapon["name"]
        weapon_durability = weapon["durability"]
        weapon_strength = weapon["strength"]
        print(str(no) + ". " + weapon_name + " (durability: " + str(weapon_durability) + ", strength: " + str(weapon_strength) + ")")

print_weapons(weapons)
```

</details>

-----

## Step 6: Modifying Data - Increasing Strength

### Problem

Now for the fun part! Let's make our weapons stronger. Use a `for ... in` loop to iterate through the `weapons` list and multiply the strength of each weapon by 10. After the loop, call `print_weapons()` to see the updated stats.

Your output for this step should be:

```
... (previous output) ...

------------
# Making all the weapons ten times stronger using `for ... in weapons`
1. Spear (durability: 20, strength: 40)
2. Mjolnir (durability: 50, strength: 250)
3. Sword (durability: 25, strength: 70)
```

### Hint

<details>
<summary>Stuck on Step 6? Click for a hint!</summary>

  * Use a `for weapon in weapons:` loop.
  * Inside the loop, you will modify the value directly in the dictionary: `weapon["strength"] = weapon["strength"] * 10`.
  * Because dictionaries are mutable, this change will affect the original `weapons` list.
  * Don't forget to call `print_weapons(weapons)` after the loop finishes.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 6? Click to reveal!</summary>

```python
print(divider)

print("# Making all the weapons ten times stronger using `for ... in weapons`")

for weapon in weapons:
    weapon["strength"] = weapon["strength"] * 10

print_weapons(weapons)
```

</details>

-----

## Step 7: Modifying Data - Increasing Durability

### Problem

Finally, let's make our weapons more durable. Use a `for ... in range(...)` loop to iterate through the `weapons` list and multiply the durability of each weapon by 2. After the loop, call `print_weapons()` to see the final stats.

Your output for this step should be:

```
... (previous output) ...

------------
# Making all our weapons twice as durable using `for ... in range(...)`
1. Spear (durability: 40, strength: 40)
2. Mjolnir (durability: 100, strength: 250)
3. Sword (durability: 50, strength: 70)
```

### Hint

<details>
<summary>Stuck on Step 7? Click for a hint!</summary>

  * Use a `for i in range(len(weapons)):` loop.
  * Inside the loop, first get the weapon dictionary with `weapon = weapons[i]`.
  * Then, update its durability: `weapon["durability"] = weapon["durability"] * 2`.
  * Call `print_weapons(weapons)` at the end to display the results.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 7? Click to reveal!</summary>

```python
print(divider)

print("# Making all our weapons twice as durable using `for ... in range(...)`")

n_weapons = len(weapons)

for i in range(n_weapons):
    weapon = weapons[i]
    weapon["durability"] = weapon["durability"] * 2

print_weapons(weapons)
```

</details>

-----

## You Finished!

You've successfully refactored your code to use a more organized and powerful data structure. You've practiced:

  * Creating dictionaries to hold related data.
  * Building a list of dictionaries.
  * Accessing and modifying data within dictionaries that are inside a list.
  * Using both `for ... in` and `for ... in range(...)` loops to iterate over and manipulate this structure.
  * Placing repetitive code into a reusable function.

This approach is much more scalable and is used everywhere in professional programming. Well done!