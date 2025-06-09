# Python Homework: Building a Battle Simulator

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

-----

## Final Goal

When you're finished, you will have built a simple command-line battle simulator. The program will ask for stats for a hero and a villain, and then simulate a turn-based fight until one of them is defeated. A sample session will look like this:

```
What is the main character's name? thor
What is the main character's weapon? hammer
What is the main character's weapon strength? 8
What is the main character's health? (0-100) 80
What is the villain's name? loki
What is the villain's weapon? dagger
What is the villain's weapon strength? 10
What is the villain's health? (0-100) 75
Meet thor.
He carries a hammer.
It has a strength of 8.
He has 80 health.

Meet loki.
He carries a dagger.
It has a strength of 10.
He has 75 health.

The battle begins!
thor attacks loki!
loki: ###################################################################
loki attacks thor!
thor: ######################################################################
... (battle continues) ...
thor attacks loki!
loki: ###########
loki attacks thor!
thor: 
thor is dead!
The battle is over!
```

-----

## Step 1: Gathering Character Data

### Problem

Let's start by defining our combatants. Your script needs to ask the user for the stats of both a hero and a villain and store them.

Your script should:

1.  Create two empty dictionaries, one named `hero` and one named `villain`.
2.  Ask the user for the hero's name, weapon, weapon strength, and health. Store each piece of information in the `hero` dictionary with appropriate keys (e.g., "name", "weapon", "weapon\_strength", "health").
3.  Do the same for the villain, storing the information in the `villain` dictionary.

When you run your code for this step, it should just prompt you for all the character information and then finish.

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  * An empty dictionary is created with `{}`.
  * Use the `input()` function to ask the user for information.
  * To add a new key-value pair to a dictionary, you use the syntax `my_dictionary["new_key"] = value`.
  * Remember that the values for "weapon\_strength" and "health" should be numbers. The `input()` function returns a string, so you'll need to convert it using `int()`.
  * You can use a `question_prefix` variable to avoid retyping "What is the main character's" and "What is the villain's".

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
question_prefix = "What is the main character's"

hero = {}

hero["name"] = input(question_prefix + " name? ")
hero["weapon"] = input(question_prefix + " weapon? ")
hero["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
hero["health"] = int(input(question_prefix + " health? (0-100) "))

question_prefix = "What is the villain's"

villain = {}

villain["name"] = input(question_prefix + " name? ")
villain["weapon"] = input(question_prefix + " weapon? ")
villain["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
villain["health"] = int(input(question_prefix + " health? (0-100) "))
```

</details>

-----

## Step 2: A Function to Introduce Characters

### Problem

Now that you have the character data, let's create a way to introduce them to the player.

Your script should:

1.  At the very top, add the line `from time import sleep`.
2.  Define a function called `introduce_character` that takes one argument, which will be a character's dictionary.
3.  Inside the function, print the character's details in a narrative style, with a one-second pause between each line. For example:
      * "Meet [name]."
      * "He carries a [weapon]."
      * "It has a strength of [weapon\_strength]."
      * "He has [health] health."
4.  After the data gathering code from Step 1, call `introduce_character()` once for the `hero` dictionary and once for the `villain` dictionary.

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * Your function definition will look like `def introduce_character(character):`. The name `character` is a parameter that will hold the dictionary you pass in.
  * Inside the function, you'll access the values from the dictionary using their keys, like `character["name"]`.
  * Remember to convert numeric values like `weapon_strength` and `health` to strings using `str()` before you can concatenate them with other strings for printing.
  * The `sleep(1)` command will cause the program to pause for 1 second.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
from time import sleep


def introduce_character(character):
    print("Meet " + character["name"] + ".")
    sleep(1)
    print("He carries a " + character["weapon"] + ".")
    sleep(1)
    print("It has a strength of " + str(character["weapon_strength"]) + ".")
    sleep(1)
    print("He has " + str(character["health"]) + " health.")
    sleep(1)
    print()

question_prefix = "What is the main character's"

hero = {}

hero["name"] = input(question_prefix + " name? ")
hero["weapon"] = input(question_prefix + " weapon? ")
hero["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
hero["health"] = int(input(question_prefix + " health? (0-100) "))

question_prefix = "What is the villain's"

villain = {}

villain["name"] = input(question_prefix + " name? ")
villain["weapon"] = input(question_prefix + " weapon? ")
villain["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
villain["health"] = int(input(question_prefix + " health? (0-100) "))

introduce_character(hero)
introduce_character(villain)
```

</details>

-----

## Step 3: The Attack and Health Display

### Problem

It's time for the battle to begin! You'll need a function to show health and a loop to handle the attacks.

Your script should:

1.  Define a new function called `show_health` that takes a character dictionary as an argument. Inside, it should print the character's name followed by a "health bar" made of `#` symbols. The number of `#`s should equal the character's health.
2.  After the code that introduces the characters, print "The battle begins!".
3.  Start an infinite `while True:` loop.
4.  Inside the loop, simulate the hero's attack:
      * Subtract the hero's `weapon_strength` from the villain's `health`.
      * Print a message saying the hero attacks the villain.
      * Call your new `show_health` function to display the villain's updated health.
      * Pause for one second using `sleep(1)`.

For now, this loop will run forever. We'll fix that in the next step.

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * For the `show_health` function, you can "multiply" a string. For example, `_ = "#" * 10` will result in `##########`.
  * The battle logic goes inside a `while True:` loop.
  * To update the villain's health, use an assignment statement like `villain["health"] = villain["health"] - hero["weapon_strength"]`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
from time import sleep


def introduce_character(character):
    print("Meet " + character["name"] + ".")
    sleep(1)
    print("He carries a " + character["weapon"] + ".")
    sleep(1)
    print("It has a strength of " + str(character["weapon_strength"]) + ".")
    sleep(1)
    print("He has " + str(character["health"]) + " health.")
    sleep(1)
    print()

def show_health(character):
    print(character["name"] + ": " + "#" * character["health"])

question_prefix = "What is the main character's"

hero = {}

hero["name"] = input(question_prefix + " name? ")
hero["weapon"] = input(question_prefix + " weapon? ")
hero["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
hero["health"] = int(input(question_prefix + " health? (0-100) "))

question_prefix = "What is the villain's"

villain = {}

villain["name"] = input(question_prefix + " name? ")
villain["weapon"] = input(question_prefix + " weapon? ")
villain["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
villain["health"] = int(input(question_prefix + " health? (0-100) "))

introduce_character(hero)
introduce_character(villain)

print("The battle begins!")

while True:
    # Hero attacks villain
    villain["health"] = villain["health"] - hero["weapon_strength"]
    print(hero["name"] + " attacks " + villain["name"] + "!")
    show_health(villain)
    sleep(1)
```

</details>

-----

## Step 4: The Full Battle and Winning Conditions

### Problem

Let's complete the battle logic. The loop needs to handle the villain's turn and check if anyone has been defeated.

Your script should:

1.  Inside the `while` loop, right after the hero's attack sequence, add an `if` statement to check if the `villain`'s health is less than or equal to 0. If it is, print that the villain is dead and use `break` to exit the loop.
2.  If the villain is still alive, add the logic for the villain's attack turn (subtract villain's strength from hero's health, print message, show hero's health, pause).
3.  After the villain's attack, add another `if` statement to check if the `hero`'s health is less than or equal to 0. If it is, print that the hero is dead and `break` the loop.
4.  Finally, after the `while` loop has finished, print "The battle is over!".

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * You'll need an `if` statement with the condition `villain["health"] <= 0`. Inside this `if` block, you will have a `print()` and then `break`.
  * The code for the villain's attack will be very similar to the code for the hero's attack, just with the `hero` and `villain` variables swapped.
  * Make sure the final `print("The battle is over!")` is outside and after the `while` loop (i.e., not indented).

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
from time import sleep


def introduce_character(character):
    print("Meet " + character["name"] + ".")
    sleep(1)
    print("He carries a " + character["weapon"] + ".")
    sleep(1)
    print("It has a strength of " + str(character["weapon_strength"]) + ".")
    sleep(1)
    print("He has " + str(character["health"]) + " health.")
    sleep(1)
    print()
    
def show_health(character):
    print(character["name"] + ": " + "#" * character["health"])

question_prefix = "What is the main character's"

hero = {}

hero["name"] = input(question_prefix + " name? ")
hero["weapon"] = input(question_prefix + " weapon? ")
hero["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
hero["health"] = int(input(question_prefix + " health? (0-100) "))

question_prefix = "What is the villain's"

villain = {}

villain["name"] = input(question_prefix + " name? ")
villain["weapon"] = input(question_prefix + " weapon? ")
villain["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
villain["health"] = int(input(question_prefix + " health? (0-100) "))

introduce_character(hero)
introduce_character(villain)

print("The battle begins!")

while True:
    # Hero attacks villain
    villain["health"] = villain["health"] - hero["weapon_strength"]
    print(hero["name"] + " attacks " + villain["name"] + "!")
    show_health(villain)
    sleep(1)
    
    if villain["health"] <= 0:
        print(villain["name"] + " is dead!")
        break
    
    # Villain attacks hero
    hero["health"] = hero["health"] - villain["weapon_strength"]
    print(villain["name"] + " attacks " + hero["name"] + "!")
    show_health(hero)
    sleep(1)
    
    if hero["health"] <= 0:
        print(hero["name"] + " is dead!")
        break

print("The battle is over!")
```

</details>

-----

## You Finished!

You've created a dynamic battle simulator! You have practiced:

  * Using dictionaries (`{}`) to store structured data.
  * Getting user input with `input()` and converting data types with `int()`.
  * Defining and calling functions with parameters (`def`).
  * Importing modules and using functions from them (`from time import sleep`).
  * Controlling program flow with a `while` loop and `if` statements.
  * Using `break` to exit a loop based on a condition.
  * Using string multiplication for simple visuals.

Great job!