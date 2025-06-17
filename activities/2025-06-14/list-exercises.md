# Python Homework: Mastering Lists

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

-----

## Initial Setup

For this homework, you'll be working with lists to manage weapon data. Start with the following basic Python code in your file.

```python
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]
```

-----

## Step 1: Basic List Information

### Problem

Your first task is to get some basic information about your lists. First, find out how many weapons are in your arsenal and print this count. Then, print the entire `weapon_names` list and the entire `weapon_strengths` list.

Your output for this step should be:

```
number of weapons: 3
weapon names: ['Spear', 'Mjolnir', 'Sword']
weapon strengths: [4, 10, 7]
```

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  * Use the `len()` function to get the number of items in a list.
  * Use the `print()` function to display the lists directly.
  * You'll need to convert the number from `len()` into a string using `str()` to combine it with other text for printing.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]

n_weapons = len(weapon_names)
print("number of weapons: " + str(n_weapons))

print("weapon names: " + str(weapon_names))

print("weapon strengths: " + str(weapon_strengths))
```

</details>

-----

## Step 2: Accessing Items by Index

### Problem

Now, let's retrieve individual items from the lists. Access and print the first and second weapon names. Then, access and print the first and second weapon strengths. Use the `divider` variable to separate this block of output.

Your output for this step should look like this:

```
number of weapons: 3
weapon names: ['Spear', 'Mjolnir', 'Sword']
weapon strengths: [4, 10, 7]

------------
first weapon name: Spear
second weapon name: Mjolnir
first weapon strength: 4
second weapon strength: 10
```

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * Remember that list indices start at `0`. The first item is at index `0`, the second at index `1`, and so on.
  * Use the syntax `list_name[index]` to get an item from a list.
  * Store the retrieved items in new variables before printing them.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]

n_weapons = len(weapon_names)
print("number of weapons: " + str(n_weapons))

print("weapon names: " + str(weapon_names))

print("weapon strengths: " + str(weapon_strengths))

first_weapon_name = weapon_names[0]
second_weapon_name = weapon_names[1]

print(divider)
print("first weapon name: " + first_weapon_name)
print("second weapon name: " + second_weapon_name)

first_weapon_strength = weapon_strengths[0]
second_weapon_strength = weapon_strengths[1]

print("first weapon strength: " + str(first_weapon_strength))
print("second weapon strength: " + str(second_weapon_strength))
```

</details>

-----

## Step 3: Looping Through Weapon Names

### Problem

Let's iterate over the `weapon_names` list.

1.  First, use a `for ... in` loop to print each weapon name on a new line.
2.  Second, use a `for ... in range(...)` loop to print a numbered list of the weapon names.

Your output for this step should look like this:

```
... (previous output) ...

------------
# Iterating over weapon names using `for ... in weapon_names` loop:
Spear
Mjolnir
Sword

------------
# Iterating over weapon names using `for ... in range(...)` loop:
1. Spear
2. Mjolnir
3. Sword
```

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * For the first loop, the syntax is `for weapon_name in weapon_names:`.
  * For the second loop, you'll need to loop through a range of numbers from `0` to the length of the list: `for i in range(len(weapon_names)):`. Inside this loop, you'll use `i` to access the item: `weapon_names[i]`.
  * To get the number for the list (1, 2, 3), you can use the loop variable `i` and add 1 to it.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]

n_weapons = len(weapon_names)
print("number of weapons: " + str(n_weapons))

print("weapon names: " + str(weapon_names))

print("weapon strengths: " + str(weapon_strengths))

first_weapon_name = weapon_names[0]
second_weapon_name = weapon_names[1]

print(divider)
print("first weapon name: " + first_weapon_name)
print("second weapon name: " + second_weapon_name)

first_weapon_strength = weapon_strengths[0]
second_weapon_strength = weapon_strengths[1]

print("first weapon strength: " + str(first_weapon_strength))
print("second weapon strength: " + str(second_weapon_strength))

print(divider)

print("# Iterating over weapon names using `for ... in weapon_names` loop:")

for weapon_name in weapon_names:
    print(weapon_name)

print(divider)

print("# Iterating over weapon names using `for ... in range(...)` loop:")

n_weapon_names = len(weapon_names)

for i in range(n_weapon_names):
    no = i + 1
    weapon_name = weapon_names[i]
    print(str(no) + ". " + weapon_name)
```

</details>

-----

## Step 4: Looping Through Weapon Strengths

### Problem

Now, do the exact same thing as the previous step, but for the `weapon_strengths` list.

1.  Use a `for ... in` loop to print each strength.
2.  Use a `for ... in range(...)` loop to print a numbered list of the strengths.

Your output for this step should look like this:

```
... (previous output) ...

------------
# Iterating over weapon strengths using `for ... in weapon_strengths` loop:
4
10
7

------------
# Iterating over weapon strengths using `for ... in range(...)` loop:
1. 4
2. 10
3. 7
```

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * This is very similar to the last step. Apply the same loop patterns to the `weapon_strengths` list.
  * Remember that the items in `weapon_strengths` are numbers, so you must use `str()` to print them with other text.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]

# ... (code from previous steps) ...

print("# Iterating over weapon strengths using `for ... in weapon_strengths` loop:")

for weapon_strength in weapon_strengths:
    print(weapon_strength)

print(divider)

print("# Iterating over weapon strengths using `for ... in range(...)` loop:")

n_weapon_strengths = len(weapon_strengths)

for i in range(n_weapon_strengths):
    no = i + 1
    weapon_strength = weapon_strengths[i]
    print(str(no) + ". " + str(weapon_strength))
```

</details>

-----

## Step 5: Combining Lists in a Loop

### Problem

Now let's display the data together. Use a single `for ... in range(...)` loop to iterate through both the `weapon_names` and `weapon_strengths` lists simultaneously, printing a combined, numbered list of each weapon and its corresponding strength.

Your output for this step should be:

```
... (previous output) ...

------------
# Iterating over both weapon names and strengths using `for ... in range(...)` loop:
1. Spear (4)
2. Mjolnir (10)
3. Sword (7)
```

### Hint

<details>
<summary>Stuck on Step 5? Click for a hint!</summary>

  * You will use a `for i in range(...)` loop.
  * Inside the loop, you can use the same index `i` to get the item from `weapon_names` (e.g., `weapon_names[i]`) and the corresponding item from `weapon_strengths` (e.g., `weapon_strengths[i]`).
  * Combine these values into a single string for printing.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 5? Click to reveal!</summary>

```python
# ... (code from previous steps) ...

print(divider)

print("# Iterating over both weapon names and strengths using `for ... in range(...)` loop:")

n_weapons = len(weapon_names)

for i in range(n_weapons):
    no = i + 1
    weapon_name = weapon_names[i]
    weapon_strength = weapon_strengths[i]
    print(str(no) + ". " + weapon_name + " (" + str(weapon_strength) + ")")
```

</details>

-----

## Step 6: Adding a Third List

### Problem

Let's add more data.

1.  Create a new list called `weapon_durabilities` with the values `[20, 50, 25]`.
2.  Print the entire `weapon_durabilities` list.
3.  Just like before, iterate over the new list first with a `for ... in` loop and then with a `for ... in range(...)` loop.

Your output for this step should be:

```
... (previous output) ...

------------
weapon durabilities: [20, 50, 25]

------------
# Iterating over weapon durabilities using `for ... in weapon_durabilities` loop:
20
50
25

------------
# Iterating over weapon durabilities using `for ... in range(...)` loop:
1. 20
2. 50
3. 25
```

### Hint

<details>
<summary>Stuck on Step 6? Click for a hint!</summary>

  * Define the new list just as you did the others.
  * Apply the same two looping patterns you have already practiced to this new list.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 6? Click to reveal!</summary>

```python
# ... (code from previous steps) ...

print(divider)

weapon_durabilities = [20, 50, 25]

print("weapon durabilities: " + str(weapon_durabilities))

print(divider)

print("# Iterating over weapon durabilities using `for ... in weapon_durabilities` loop:")

for weapon_durability in weapon_durabilities:
    print(weapon_durability)

print(divider)

print("# Iterating over weapon durabilities using `for ... in range(...)` loop:")

n_weapon_durabilities = len(weapon_durabilities)

for i in range(n_weapon_durabilities):
    no = i + 1
    weapon_durability = weapon_durabilities[i]
    print(str(no) + ". " + str(weapon_durability))
```

</details>

-----

## Step 7: Looping Over All Three Lists

### Problem

Finally, let's bring it all together. Use one `for ... in range(...)` loop to iterate through all three lists (`weapon_names`, `weapon_durabilities`, and `weapon_strengths`) and print a formatted string showing all the data for each weapon.

Your final output should be:

```
... (previous output) ...

------------
# Iterating over weapon names, durabilities, and strengths using `for ... in range(...)
1. Spear (durability: 20, strength: 4)
2. Mjolnir (durability: 50, strength: 10)
3. Sword (durability: 25, strength: 7)
```

### Hint

<details>
<summary>Stuck on Step 7? Click for a hint!</summary>

  * This is an extension of Step 5.
  * Inside your `for i in range(...)` loop, you will now access items from all three lists using the same index `i`: `weapon_names[i]`, `weapon_durabilities[i]`, and `weapon_strengths[i]`.
  * Construct the final, formatted string and print it.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 7? Click to reveal!</summary>

```python
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]

n_weapons = len(weapon_names)
print("number of weapons: " + str(n_weapons))

print("weapon names: " + str(weapon_names))

print("weapon strengths: " + str(weapon_strengths))

first_weapon_name = weapon_names[0]
second_weapon_name = weapon_names[1]

print(divider)
print("first weapon name: " + first_weapon_name)
print("second weapon name: " + second_weapon_name)

first_weapon_strength = weapon_strengths[0]
second_weapon_strength = weapon_strengths[1]

print("first weapon strength: " + str(first_weapon_strength))
print("second weapon strength: " + str(second_weapon_strength))

print(divider)

print("# Iterating over weapon names using `for ... in weapon_names` loop:")

for weapon_name in weapon_names:
    print(weapon_name)

print(divider)

print("# Iterating over weapon names using `for ... in range(...)` loop:")

n_weapon_names = len(weapon_names)

for i in range(n_weapon_names):
    no = i + 1
    weapon_name = weapon_names[i]
    print(str(no) + ". " + weapon_name)

print(divider)

print("# Iterating over weapon strengths using `for ... in weapon_strengths` loop:")

for weapon_strength in weapon_strengths:
    print(weapon_strength)

print(divider)

print("# Iterating over weapon strengths using `for ... in range(...)` loop:")

n_weapon_strengths = len(weapon_strengths)

for i in range(n_weapon_strengths):
    no = i + 1
    weapon_strength = weapon_strengths[i]
    print(str(no) + ". " + str(weapon_strength))

print(divider)

print("# Iterating over both weapon names and strengths using `for ... in range(...)` loop:")

n_weapons = len(weapon_names)

for i in range(n_weapons):
    no = i + 1
    weapon_name = weapon_names[i]
    weapon_strength = weapon_strengths[i]
    print(str(no) + ". " + weapon_name + " (" + str(weapon_strength) + ")")

print(divider)

weapon_durabilities = [20, 50, 25]

print("weapon durabilities: " + str(weapon_durabilities))

print(divider)

print("# Iterating over weapon durabilities using `for ... in weapon_durabilities` loop:")

for weapon_durability in weapon_durabilities:
    print(weapon_durability)

print(divider)

print("# Iterating over weapon durabilities using `for ... in range(...)` loop:")

n_weapon_durabilities = len(weapon_durabilities)

for i in range(n_weapon_durabilities):
    no = i + 1
    weapon_durability = weapon_durabilities[i]
    print(str(no) + ". " + str(weapon_durability))

print(divider)

print("# Iterating over weapon names, durabilities, and strengths using `for ... in range(...)")
for i in range(n_weapon_durabilities):
    no = i + 1
    weapon_strength = weapon_strengths[i]
    weapon_name = weapon_names[i]
    weapon_durability = weapon_durabilities[i]
    print(str(no) + ". " + weapon_name + " (durability: " + str(weapon_durability) + ", strength: " + str(weapon_strength) + ")")
```

</details>

-----

## You Finished!

You've practiced:

  * Creating and initializing lists.
  * Getting the size of a list with `len()`.
  * Accessing list items by their numerical index.
  * Using a `for ... in` loop to iterate through each item directly.
  * Using a `for ... in range(len(...))` loop to iterate using an index.
  * Iterating over multiple lists in parallel to combine their data.

## Well done!