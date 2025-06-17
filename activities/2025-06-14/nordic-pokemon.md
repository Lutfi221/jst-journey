# Python Homework: Building Nordic Pokemon

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

-----

## Final Goal

When you're finished, you will have built a command-line battle game where the user can choose weapons and control the fight, or let the computer take over. A sample session will look like this:

```
Welcome to Nordic Pokemon!
Do you want the hero be played by computer? (y/n) y
Do you want the villain be played by computer? (y/n) n
Hero weapons:

1. Spear (4)
2. Mjolnir (10)
3. Sword (7)

Choose 1-3:
 > 2
Villain weapons:

1. Halbur (10)
2. Scepter (8)
3. Axe (6)

Choose 1-3:
 > 2
The battle begins!
Hero Thor deals 10 damage
Villain attack styles:
1. Heavy
2. Light
Choose villain attack style (1-2): 1
Villain Loki deals 48 damage
HERO    : ##########################################
VILLAIN : ######################################################################
Hero Thor deals 30 damage
Villain attack styles:
1. Heavy
2. Light
Choose villain attack style (1-2): 2
Villain Loki deals 16 damage
HERO    : ##########################
VILLAIN : ########################################
Hero Thor deals 50 damage
Villain attack styles:
1. Heavy
2. Light
Choose villain attack style (1-2): 1
Villain Loki deals 40 damage
HERO    :
VILLAIN :
Hero Thor is dead!
```

-----

## Initial Setup

For this homework, you'll be building the Nordic Pokemon game. Start with the following basic Python code. You'll add to it in each step.

```python
import random

print("Welcome to Nordic Pokemon!")

```

-----

## Step 1: Character and Weapon Setup

### Problem

First, let's create our hero and villain and let the player choose their weapons.

Your script should:

1.  Create a dictionary for the `hero` with keys for "name", "health", "weapon", and "weapon\_strength". Set some default values.
2.  Print a menu of weapons for the hero, showing the strength of each.
3.  Ask the player to choose a weapon and update the `hero` dictionary with the name and strength of the chosen weapon.
4.  Do the same for a `villain` dictionary.
5.  After both have chosen, print "The battle begins!".

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  * Create a dictionary using curly braces `{}`. For example: `hero = {"name": "Thor", "health": 90, ...}`.
  * Use a multiline string (`"""..."""`) to print the weapon menu easily.
  * Use `input()` to get the player's choice. Remember to convert it to an integer using `int()` so you can compare it with numbers.
  * Use an `if/elif` block to check the user's choice and update the dictionary keys. For example: `if hero_weapon_choice == 1: hero["weapon"] = "Spear"`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
import random

print("Welcome to Nordic Pokemon!")

hero = {
    "name": "Thor",
    "health": 90,
    "weapon": "Fists",
    "weapon_strength": 2,
}

print(
    """Hero weapons:

1. Spear (4)
2. Mjolnir (10)
3. Sword (7)

Choose 1-3:"""
)

hero_weapon_choice = int(input(" > "))

if hero_weapon_choice == 1:
    hero["weapon"] = "Spear"
    hero["weapon_strength"] = 4
elif hero_weapon_choice == 2:
    hero["weapon"] = "Mjolnir"
    hero["weapon_strength"] = 10
elif hero_weapon_choice == 3:
    hero["weapon"] = "Sword"
    hero["weapon_strength"] = 7

villain = {
    "name": "Loki",
    "health": 80,
    "weapon": "Fists",
    "weapon_strength": 1,
}

print(
    """Villain weapons:

1. Halbur (10)
2. Scepter (8)
3. Axe (6)

Choose 1-3:"""
)

villain_weapon_choice = int(input(" > "))

if villain_weapon_choice == 1:
    villain["weapon"] = "Halbur"
    villain["weapon_strength"] = 10
elif villain_weapon_choice == 2:
    villain["weapon"] = "Scepter"
    villain["weapon_strength"] = 8
elif villain_weapon_choice == 3:
    villain["weapon"] = "Axe"
    villain["weapon_strength"] = 6

print("The battle begins!")
```

</details>

-----

## Step 2: Health Bars and the Battle Loop

### Problem

Now it's time for battle! Let's create a function to visualize health and start the main fight loop.

Your script should:

1.  Define a function called `print_health_bars` that takes `hero_health` and `villain_health` as arguments. This function will print a health bar (made of `#` symbols) for both the hero and the villain.
2.  Start an infinite `while True:` loop after the "The battle begins!" message.
3.  Inside the loop, for now, just simulate the hero's attack:
      * The damage dealt is simply the hero's `weapon_strength`.
      * Print a message saying how much damage the hero deals.
      * Subtract this damage from the villain's health.
      * Call your new `print_health_bars` function to display the updated health of both characters.

This loop will run forever, with the hero constantly attacking. We'll add more to it in the next steps.

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * Your function definition will be `def print_health_bars(hero_health, villain_health):`.
  * Inside the function, you can create the health bar string by multiplying the '\#' character by the health value. For example: `hero_bar = "#" * hero_health`.
  * Inside the `while True:` loop, you'll need to update the villain's health: `villain["health"] = villain["health"] - hero["weapon_strength"]`.
  * When you call your health bar function, pass the health values from the dictionaries: `print_health_bars(hero["health"], villain["health"])`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
import random

print("Welcome to Nordic Pokemon!")

hero = {
    "name": "Thor",
    "health": 90,
    "weapon": "Fists",
    "weapon_strength": 2,
}

print(
    """Hero weapons:

1. Spear (4)
2. Mjolnir (10)
3. Sword (7)

Choose 1-3:"""
)

hero_weapon_choice = int(input(" > "))

if hero_weapon_choice == 1:
    hero["weapon"] = "Spear"
    hero["weapon_strength"] = 4
elif hero_weapon_choice == 2:
    hero["weapon"] = "Mjolnir"
    hero["weapon_strength"] = 10
elif hero_weapon_choice == 3:
    hero["weapon"] = "Sword"
    hero["weapon_strength"] = 7

villain = {
    "name": "Loki",
    "health": 80,
    "weapon": "Fists",
    "weapon_strength": 1,
}

print(
    """Villain weapons:

1. Halbur (10)
2. Scepter (8)
3. Axe (6)

Choose 1-3:"""
)

villain_weapon_choice = int(input(" > "))

if villain_weapon_choice == 1:
    villain["weapon"] = "Halbur"
    villain["weapon_strength"] = 10
elif villain_weapon_choice == 2:
    villain["weapon"] = "Scepter"
    villain["weapon_strength"] = 8
elif villain_weapon_choice == 3:
    villain["weapon"] = "Axe"
    villain["weapon_strength"] = 6

print("The battle begins!")


def print_health_bars(hero_health, villain_health):
    hero_bar = "#" * hero_health
    villain_bar = "#" * villain_health
    print("HERO    : " + hero_bar)
    print("VILLAIN : " + villain_bar)


while True:
    # For now, damage is just weapon strength
    hero_damage = hero["weapon_strength"]

    print(
        f"Hero {hero['name']} deals {hero_damage} damage"
    )

    villain["health"] = villain["health"] - hero_damage
    
    # In this step, we just show the health bars. The rest of the turn comes next.
    print_health_bars(hero["health"], villain["health"])

```

</details>

-----

## Step 3: Full Combat and Winning

### Problem

Let's complete the turn by adding the villain's attack and a way for the battle to end.

Your script should:

1.  Inside the `while` loop, after the hero's attack, check if the villain's health is `0` or less. If it is, print that the villain is dead and use `break` to stop the loop.
2.  If the villain is still alive, add the villain's attack logic (similar to the hero's).
3.  After the villain's attack, check if the hero's health is `0` or less. If it is, print that the hero is dead and `break` the loop.

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * You'll need an `if` statement with the condition `villain["health"] <= 0`.
  * The code for the villain's attack will be very similar to the hero's, just with the variables swapped.
  * Use a second `if` statement to check `hero["health"] <= 0`.
  * The `break` keyword is used to exit a `while` loop immediately.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
import random

print("Welcome to Nordic Pokemon!")

hero = {
    "name": "Thor",
    "health": 90,
    "weapon": "Fists",
    "weapon_strength": 2,
}

# ... (weapon selection code from Step 1 remains here) ...
print(
    """Hero weapons:

1. Spear (4)
2. Mjolnir (10)
3. Sword (7)

Choose 1-3:"""
)

hero_weapon_choice = int(input(" > "))

if hero_weapon_choice == 1:
    hero["weapon"] = "Spear"
    hero["weapon_strength"] = 4
elif hero_weapon_choice == 2:
    hero["weapon"] = "Mjolnir"
    hero["weapon_strength"] = 10
elif hero_weapon_choice == 3:
    hero["weapon"] = "Sword"
    hero["weapon_strength"] = 7

villain = {
    "name": "Loki",
    "health": 80,
    "weapon": "Fists",
    "weapon_strength": 1,
}

print(
    """Villain weapons:

1. Halbur (10)
2. Scepter (8)
3. Axe (6)

Choose 1-3:"""
)

villain_weapon_choice = int(input(" > "))

if villain_weapon_choice == 1:
    villain["weapon"] = "Halbur"
    villain["weapon_strength"] = 10
elif villain_weapon_choice == 2:
    villain["weapon"] = "Scepter"
    villain["weapon_strength"] = 8
elif villain_weapon_choice == 3:
    villain["weapon"] = "Axe"
    villain["weapon_strength"] = 6


print("The battle begins!")


def print_health_bars(hero_health, villain_health):
    hero_bar = "#" * hero_health
    villain_bar = "#" * villain_health
    print("HERO    : " + hero_bar)
    print("VILLAIN : " + villain_bar)


while True:
    # Hero attacks
    hero_damage = hero["weapon_strength"]
    print(f"Hero {hero['name']} deals {hero_damage} damage")
    villain["health"] = villain["health"] - hero_damage

    # Check for villain defeat
    if villain["health"] <= 0:
        print(f"Villain {villain['name']} is dead!")
        break

    # Villain attacks
    villain_damage = villain["weapon_strength"]
    print(f"Villain {villain['name']} deals {villain_damage} damage")
    hero["health"] = hero["health"] - villain_damage
    
    # Check for hero defeat
    if hero["health"] <= 0:
        print(f"Hero {hero['name']} is dead!")
        break

    print_health_bars(hero["health"], villain["health"])

```

</details>

-----

## Step 4: Random Damage with Attack Styles

### Problem

Let's make combat more exciting by adding random damage.

Your script should:

1.  Define a new function `calculate_attack_multiplier` that takes an `attack_style` (1 for Heavy, 2 for Light) as an argument.
      * If the style is 1, it should `return` a random integer between 3 and 6.
      * Otherwise, it should `return` a random integer between 1 and 3.
2.  Inside the `while` loop, before the hero attacks, ask the player to choose an attack style (1 for Heavy, 2 for Light).
3.  Call `calculate_attack_multiplier` with the chosen style to get a multiplier.
4.  Update the hero's damage calculation to be `hero["weapon_strength"] * hero_attack_multiplier`.
5.  Do the same for the villain's turn.

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * Your new function will use `random.randint(min, max)` to get a random number.
  * Inside the loop, for the hero's turn, you'll add `input()` to ask for the style, then call your new function: `hero_attack_multiplier = calculate_attack_multiplier(hero_attack_style)`.
  * The damage is now `villain["health"] - hero["weapon_strength"] * hero_attack_multiplier`.
  * Don't forget to do the same for the villain's turn!

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
import random

# ... (all code from previous steps: welcome message, dictionaries, weapon selection) ...
print("Welcome to Nordic Pokemon!")

hero = {
    "name": "Thor",
    "health": 90,
    "weapon": "Fists",
    "weapon_strength": 2,
}

print(
    """Hero weapons:

1. Spear (4)
2. Mjolnir (10)
3. Sword (7)

Choose 1-3:"""
)

hero_weapon_choice = int(input(" > "))

if hero_weapon_choice == 1:
    hero["weapon"] = "Spear"
    hero["weapon_strength"] = 4
elif hero_weapon_choice == 2:
    hero["weapon"] = "Mjolnir"
    hero["weapon_strength"] = 10
elif hero_weapon_choice == 3:
    hero["weapon"] = "Sword"
    hero["weapon_strength"] = 7

villain = {
    "name": "Loki",
    "health": 80,
    "weapon": "Fists",
    "weapon_strength": 1,
}

print(
    """Villain weapons:

1. Halbur (10)
2. Scepter (8)
3. Axe (6)

Choose 1-3:"""
)

villain_weapon_choice = int(input(" > "))

if villain_weapon_choice == 1:
    villain["weapon"] = "Halbur"
    villain["weapon_strength"] = 10
elif villain_weapon_choice == 2:
    villain["weapon"] = "Scepter"
    villain["weapon_strength"] = 8
elif villain_weapon_choice == 3:
    villain["weapon"] = "Axe"
    villain["weapon_strength"] = 6

print("The battle begins!")


def calculate_attack_multiplier(attack_style):
    if attack_style == 1:
        return random.randint(3, 6)
    else:
        return random.randint(1, 3)


def print_health_bars(hero_health, villain_health):
    hero_bar = "#" * hero_health
    villain_bar = "#" * villain_health
    print("HERO    : " + hero_bar)
    print("VILLAIN : " + villain_bar)


while True:
    # Hero's Turn
    print("Hero attack styles:")
    print("1. Heavy")
    print("2. Light")
    hero_attack_style = int(input("Choose hero attack style (1-2): "))
    hero_attack_multiplier = calculate_attack_multiplier(hero_attack_style)
    
    print(f"Hero {hero['name']} deals {hero['weapon_strength'] * hero_attack_multiplier} damage")
    villain["health"] = villain["health"] - hero_attack_multiplier * hero["weapon_strength"]

    if villain["health"] <= 0:
        print(f"Villain {villain['name']} is dead!")
        break

    # Villain's Turn
    print("Villain attack styles:")
    print("1. Heavy")
    print("2. Light")
    villain_attack_style = int(input("Choose villain attack style (1-2): "))
    villain_attack_multiplier = calculate_attack_multiplier(villain_attack_style)

    hero["health"] = hero["health"] - villain_attack_multiplier * villain["weapon_strength"]
    print(f"Villain {villain['name']} deals {villain['weapon_strength'] * villain_attack_multiplier} damage")

    if hero["health"] <= 0:
        print(f"Hero {hero['name']} is dead!")
        break

    print_health_bars(hero["health"], villain["health"])

```

</details>

-----

## Step 5: Automation Mode

### Problem

Finally, let's add the ability for the computer to play.

Your script should:

1.  At the beginning of the script, create two boolean variables, `is_hero_automated` and `is_villain_automated`, and set them to `True`.
2.  After the welcome message, ask the user if the hero should be played by the computer. Update `is_hero_automated` based on their "y/n" answer.
3.  Do the same for the villain.
4.  Inside the `while` loop, for the hero's turn, check if `is_hero_automated` is `True`.
      * If it is, choose the attack style randomly.
      * If it's `False`, prompt the user for the attack style as before.
5.  Do the same for the villain's turn using `is_villain_automated`.

### Hint

<details>
<summary>Stuck on Step 5? Click for a hint!</summary>

  * After getting the user's choice (e.g., `hero_automation_choice`), you can set the boolean like this: `is_hero_automated = hero_automation_choice == "y"`. This expression will be `True` if they typed "y", and `False` otherwise.
  * Inside the loop, you'll wrap the attack style logic in an `if/else` block.
  * `if is_hero_automated:`
      * `hero_attack_style = random.randint(1, 2)` (or 1, 3 as in the final code to vary light attacks).
  * `else:`
      * The `input()` code you already have.
  * Apply the same `if/else` logic for the villain's turn.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 5? Click to reveal!</summary>

```python
import random


is_hero_automated = True
is_villain_automated = True

print("Welcome to Nordic Pokemon!")

hero_automation_choice = input("Do you want the hero be played by computer? (y/n) ")
villain_automation_choice = input(
    "Do you want the villain be played by computer? (y/n) "
)

if hero_automation_choice == "y":
    is_hero_automated = True
else:
    is_hero_automated = False

# Alternative way to do the same thing
is_villain_automated = villain_automation_choice == "y"

hero = {
    "name": "Thor",
    "health": 90,
    "weapon": "Fists",
    "weapon_strength": 2,
}

print(
    """Hero weapons:

1. Spear (4)
2. Mjolnir (10)
3. Sword (7)

Choose 1-3:"""
)

hero_weapon_choice = int(input(" > "))

if hero_weapon_choice == 1:
    hero["weapon"] = "Spear"
    hero["weapon_strength"] = 4
elif hero_weapon_choice == 2:
    hero["weapon"] = "Mjolnir"
    hero["weapon_strength"] = 10
elif hero_weapon_choice == 3:
    hero["weapon"] = "Sword"
    hero["weapon_strength"] = 7

villain = {
    "name": "Loki",
    "health": 80,
    "weapon": "Fists",
    "weapon_strength": 1,
}

print(
    """Villain weapons:

1. Halbur (10)
2. Scepter (8)
3. Axe (6)

Choose 1-3:"""
)

villain_weapon_choice = int(input(" > "))

if villain_weapon_choice == 1:
    villain["weapon"] = "Halbur"
    villain["weapon_strength"] = 10
elif villain_weapon_choice == 2:
    villain["weapon"] = "Scepter"
    villain["weapon_strength"] = 8
elif villain_weapon_choice == 3:
    villain["weapon"] = "Axe"
    villain["weapon_strength"] = 6

print("The battle begins!")


def calculate_attack_multiplier(attack_style):
    if attack_style == 1:
        return random.randint(3, 6)
    else:
        return random.randint(1, 3)


def print_health_bars(hero_health, villain_health):
    hero_bar = "#" * hero_health
    villain_bar = "#" * villain_health
    print("HERO    : " + hero_bar)
    print("VILLAIN : " + villain_bar)


while True:
    if is_hero_automated:
        hero_attack_style = random.randint(1, 3)
    else:
        print("Hero attack styles:")
        print("1. Heavy")
        print("2. Light")
        hero_attack_style = int(input("Choose hero attack style (1-2): "))

    hero_attack_multiplier = calculate_attack_multiplier(hero_attack_style)

    print(
        f"Hero {hero['name']} deals {hero['weapon_strength'] * hero_attack_multiplier} damage"
    )

    villain["health"] = (
        villain["health"] - hero_attack_multiplier * hero["weapon_strength"]
    )
    
    if villain["health"] <= 0:
        print(f"Villain {villain['name']} is dead!")
        break

    if is_villain_automated:
        villain_attack_style = random.randint(1, 3)
    else:
        print("Villain attack styles:")
        print("1. Heavy")
        print("2. Light")
        villain_attack_style = int(input("Choose villain attack style (1-2): "))

    villain_attack_multiplier = calculate_attack_multiplier(villain_attack_style)

    hero["health"] = (
        hero["health"] - villain_attack_multiplier * villain["weapon_strength"]
    )

    print(
        f"Villain {villain['name']} deals {villain['weapon_strength'] * villain_attack_multiplier} damage"
    )

    print_health_bars(hero["health"], villain["health"])

    if hero["health"] <= 0:
        print(f"Hero {hero['name']} is dead!")
        break
```

</details>

-----

## You Finished!

Congratulations! You've built a complete, dynamic battle game. You have practiced:

  * Using dictionaries to manage character data.
  * Using `if/elif/else` for complex choices like weapon selection.
  * Defining functions that take arguments and return values.
  * Controlling program flow with a `while` loop and `break` statements.
  * Using the `random` module to make the game unpredictable.
  * Using boolean variables to control game modes (automated vs. manual).
  * Using f-strings to format output messages.

Well done, warrior!