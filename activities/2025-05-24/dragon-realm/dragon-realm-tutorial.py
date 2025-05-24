# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] id="dragon-title" slideshow={"slide_type": "slide"}
# # Chapter 5: The Quest of Dragon Realm!
#
# <img src="images/00016.jpeg" alt="Dragon Realm Title Image" style="height: 300px;"/>
#
# ## An Adventure in Python Programming

# %% [markdown] id="dragon-disclaimer" slideshow={"slide_type": "fragment"}
# **A Note on Our Adventure:** This game involves fictional dragons and choices. We're here to learn Python programming concepts in a fun, fantasy setting. We do not endorse any form of real-world violence or harm. Our dragons are strictly code!

# %% [markdown] id="dragon-how-to-play" slideshow={"slide_type": "slide"}
# ## How to Play Dragon Realm
#
# Brave adventurer, you stand before two caves:
# * One cave hides a **friendly dragon** willing to share its treasure!
# * The other, a **greedy and hungry dragon** that... well, you get the idea.
#
# You must choose a cave (1 or 2). Will fortune favor you?

# %% [markdown] id="dragon-topics" slideshow={"slide_type": "slide"}
# ## Magical Scrolls We'll Uncover (Topics Covered)
#
# In this chapter, we'll master new programming spells:
#
# * 📜 **Flowcharts:** Charting our adventure's path.
# * ✨ **`def` keyword:** Crafting our own magical functions.
# * 📜 **Multiline strings:** Weaving long tales and descriptions.
# * 🔄 **`while` statements:** Loops that continue under a condition.
# * ⚖️ **Boolean operators (`and`, `or`, `not`):** The logic of choices.
# * 📊 **Truth tables:** Understanding Boolean outcomes.
# * 🎁 **`return` keyword:** Functions bestowing gifts (values).
# * 🌍 **Global and local scope:** The realms of variables.
# * 🤝 **Parameters and arguments:** Passing messages to functions.
# * ⏳ **`sleep()` function:** Adding suspense to our tale.

# %% [markdown] id="dragon-sample-run" slideshow={"slide_type": "slide"}
# ## A Glimpse into the Adventure (Sample Run)
#
# This is what a game session might look like. The player's input is shown after the prompt.
# ```text
# You are in a land full of dragons. In front of you,
# you see two caves. In one cave, the dragon is friendly
# and will share his treasure with you. The other dragon
# is greedy and hungry, and will eat you on sight.
# Which cave will you go into? (1 or 2)
# 1
# You approach the cave...
# It is dark and spooky...
# A large dragon jumps out in front of you! He opens his jaws and...
# Eats you and spends your robux!
# Do you want to play again? (yes or no)
# no
# ```

# %% [markdown] id="dragon-flowchart-intro" slideshow={"slide_type": "slide"}
# ## Charting the Dragon's Lair: Flowcharts
#
# Before coding, wise adventurers design their program. A flowchart is like a map showing every possible action.
#
# <img src="images/00061.jpeg" alt="Flowchart for Dragon Realm" style="max-width: 80%; border: 1px solid grey;"/>
#
# *Figure 5-1: Flowchart for the Dragon Realm game. Follow the arrows from START to END.*

# %% [markdown] id="dragon-source-code-intro" slideshow={"slide_type": "slide"}
# ## The Ancient Script: Source Code for Dragon Realm
#
# We'll now examine the Python script, `dragon.py`.
#
# You can type this into your IDLE editor (File > New Window) and save it as `dragon.py`.
#
# <img src="images/00062.jpeg" alt="dragon.py code snippet" style="max-width: 80%; border: 1px solid grey;"/>
#
# *(This is a visual representation; we'll break down the code next.)*

# %% [markdown] id="dragon-imports" slideshow={"slide_type": "slide"}
# ## Summoning Aides: Importing Modules
#
# Our script needs help from Python's built-in magic:
# ```python
# import random
# import time
# ```
# * `random`: For unpredictable events, like which cave has the friendly dragon (`random.randint()`).
# * `time`: To control the pacing of our story (`time.sleep()`).
#
# (This cell just shows the import statements as they appear in the script.)

# %% [markdown] id="dragon-functions-intro" slideshow={"slide_type": "slide"}
# ## Incantations & Reusable Spells: Functions
#
# Functions are blocks of code that perform a specific task. We define them once and can "call" (use) them many times.
#
# We've used built-in functions like `print()`, `input()`, `randint()`. Now, we'll create our own!

# %% [markdown] id="dragon-def-statement" slideshow={"slide_type": "subslide"}
# ### The `def` Statement: Crafting a Function
#
# We define functions using the `def` keyword. Below is the `displayIntro` function definition from our game. Running this cell defines the function, but doesn't execute its content yet.
#
# <img src="images/00064.jpeg" alt="Parts of a def statement" style="max-width: 70%; border: 1px solid grey; display: block; margin-left: auto; margin-right: auto;"/>
# *Figure 5-2: Parts of a `def` statement*


# %% slideshow={"slide_type": "fragment"}
def displayIntro_example():  # Renamed for this example slide
    print(
        """You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight."""
    )
    print()


# To see it work, we would call displayIntro_example() in another cell.

# %% [markdown] id="dragon-calling-function" slideshow={"slide_type": "subslide"}
# ### Invoking the Spell: Calling a Function
#
# Defining a function doesn't run its code. You must *call* it:


# %% slideshow={"slide_type": "fragment"}
# This is a function definition
def simpleGreeting():
    print("Welcome, brave adventurer!")


# This is the function call (code inside simpleGreeting runs now)
simpleGreeting()

# %% [markdown] id="dragon-function-order" slideshow={"slide_type": "subslide"}
# ### The Order of Spells: Where to Define Functions
#
# A function must be defined *before* you call it.
#
# **Incorrect (causes an error if uncommented):**
# ```python
# # tryToSayGoodbye() # Error! Python doesn't know this spell yet.
#
# # def tryToSayGoodbye():
# #    print('Goodbye, for now!')
# ```
#
# **Correct:**


# %% slideshow={"slide_type": "fragment"}
def sayGoodbye():
    print("Goodbye!")


sayGoodbye()  # Now Python knows the spell.

# %% [markdown] id="dragon-multiline-strings" slideshow={"slide_type": "slide"}
# ## Weaving Long Tales: Multiline Strings
#
# For text that spans multiple lines, use triple quotes (`'''` or `"""`).

# %% slideshow={"slide_type": "fragment"}
intro_message = """This is a tale of ancient lore,
spread across several lines,
telling of dragons and treasure galore."""

print(intro_message)

# %% [markdown] id="dragon-while-loops" slideshow={"slide_type": "slide"}
# ## Persistent Magic: `while` Loops
#
# A `while` loop repeats code as long as its condition is `True`.

# %% slideshow={"slide_type": "fragment"}
# Example:
count = 0
print("Starting the count...")
while count < 3:
    print(f"Still counting... (count is {count})")
    count = count + 1  # or count += 1
print("Done counting!")

# %% [markdown] id="dragon-while-loops-choosecave" slideshow={"slide_type": "fragment"}
# In `dragon.py`, the `chooseCave()` function uses a `while` loop for input validation:
# ```python
# # Snippet from chooseCave():
# #    cave = ''
# #    while cave != '1' and cave != '2': # Loop until valid input
# #        print('Which cave will you go into? (1 or 2)')
# #        cave = input()
# #    return cave
# ```
# (This snippet is illustrative as `input()` is harder to demo in static slides).

# %% [markdown] id="dragon-boolean-ops-intro" slideshow={"slide_type": "slide"}
# ## The Logic of Choice: Boolean Operators
#
# Boolean operators (`and`, `or`, `not`) work with `True` / `False` values.
# They help us make complex decisions.

# %% [markdown] id="dragon-and-operator" slideshow={"slide_type": "subslide"}
# ### The `and` Operator
#
# `A and B` is `True` only if *both* A and B are `True`.
#
# **Truth Table for `and`:**
# | A     | B     | A and B |
# |-------|-------|---------|
# | `True`  | `True`  | `True`  |
# | `True`  | `False` | `False` |
# | `False` | `True`  | `False` |
# | `False` | `False` | `False` |
#
# Let's test it:

# %% slideshow={"slide_type": "fragment"}
print(f"True and True is: {True and True}")
print(f"True and False is: {True and False}")

can_enter_ride = (120 < 150) and ("ticket" == "ticket")  # Height check and ticket check
print(f"Can enter ride? {can_enter_ride}")

# %% [markdown] id="dragon-or-operator" slideshow={"slide_type": "subslide"}
# ### The `or` Operator
#
# `A or B` is `True` if *at least one* of A or B is `True`.
#
# **Truth Table for `or`:**
# | A     | B     | A or B  |
# |-------|-------|---------|
# | `True`  | `True`  | `True`  |
# | `True`  | `False` | `True`  |
# | `False` | `True`  | `True`  |
# | `False` | `False` | `False` |
#
# Example from `dragon.py` (line 36): `playAgain == 'yes' or playAgain == 'y'`

# %% slideshow={"slide_type": "fragment"}
print(f"True or False is: {True or False}")
print(f"False or False is: {False or False}")

has_potion = False
has_spell = True
can_fight_monster = has_potion or has_spell
print(f"Can fight monster? {can_fight_monster}")

# %% [markdown] id="dragon-not-operator" slideshow={"slide_type": "subslide"}
# ### The `not` Operator
#
# `not A` gives the opposite Boolean value of A.
#
# **Truth Table for `not`:**
# | A     | not A   |
# |-------|---------|
# | `True`  | `False` |
# | `False` | `True`  |

# %% slideshow={"slide_type": "fragment"}
print(f"not True is: {not True}")
is_daytime = False
is_nighttime = not is_daytime
print(f"Is it nighttime? {is_nighttime}")

# %% [markdown] id="dragon-evaluating-booleans" slideshow={"slide_type": "subslide"}
# ### Evaluating Booleans in `chooseCave()`
#
# Line 13: `while cave != '1' and cave != '2':`
#
# * If `cave` is `''` (initially):
#     * `'' != '1'` is `True`.
#     * `'' != '2'` is `True`.
#     * So, `True and True` is `True`. The loop continues.
# * If player enters `'1'`:
#     * `'1' != '1'` is `False`.
#     * The `and` condition becomes `False and ...` which is `False`. The loop stops.
# * This ensures the player enters either '1' or '2'. This is called **input validation**.
#
# (This slide is explanatory text.)

# %% [markdown] id="dragon-return-values" slideshow={"slide_type": "slide"}
# ## A Function's Gift: Return Values
#
# The `return` statement sends a value back from a function.
#
# In `dragon.py` (line 17), `chooseCave()` returns the player's valid choice.
#
# ```python
# # def chooseCave():
# #    ... (code to get valid input '1' or '2') ...
# #    return cave
# ```
# When `chooseCave()` is called (line 38: `caveNumber = chooseCave()`), the returned value (`'1'` or `'2'`) is stored in `caveNumber`.


# %% [markdown] slideshow={"slide_type": "fragment"}
# Here's a simpler example of a function that returns a value:
# %% slideshow={"slide_type": "fragment"}
def getPassword():
    # In a real app, this would be more complex!
    secret_password = "swordfish"
    return secret_password


my_secret = getPassword()
print(f"The function returned: {my_secret}")

# %% [markdown] id="dragon-scope" slideshow={"slide_type": "slide"}
# ## Realms of Variables: Global vs. Local Scope
#
# * **Local Scope:** Variables created *inside* a function. They exist only while the function is running and are forgotten when it returns. (e.g., `cave` in `chooseCave()`)
# * **Global Scope:** Variables created *outside* all functions. They exist for the entire program. (e.g., `playAgain` in `dragon.py`)
#
# A local variable can have the same name as a global one, but they are separate!

# %% [markdown] id="dragon-scope-example" slideshow={"slide_type": "subslide"}
# ### Scope Example: The Tale of Two `spam`s
#
# Observe how the `spam` variable behaves inside and outside the `bacon()` function.


# %% slideshow={"slide_type": "fragment"}
def bacon():
    spam = 99  # This is a LOCAL spam
    print(f"Inside bacon(), spam is: {spam}")


spam = 42  # This is a GLOBAL spam
print(f"Before calling bacon(), global spam is: {spam}")
bacon()  # Calls bacon(), which prints its local spam
print(f"After calling bacon(), global spam is still: {spam}")

# %% [markdown] id="dragon-parameters" slideshow={"slide_type": "slide"}
# ## Passing Messages: Function Parameters & Arguments
#
# A **parameter** is a variable in a function definition that receives a value when the function is called.
# An **argument** is the actual value passed to the function.
#
# ```python
# # 'chosenCave' is a PARAMETER in the original game's checkCave function
# # def checkCave(chosenCave):
# #     print('You chose cave number: ' + chosenCave)
# #     # ... more code ...
# ```
# When `checkCave(caveNumber)` is called (line 39 in `dragon.py`), the value in `caveNumber` is the **argument**.

# %% [markdown] id="dragon-parameters-example" slideshow={"slide_type": "subslide"}
# ### Parameters Example: `sayHello`
#
# The `sayHello` function takes one parameter, `name`.


# %% slideshow={"slide_type": "fragment"}
def sayHello(name_param):  # 'name_param' is a parameter
    message = f"Hello, {name_param}. Your name has {len(name_param)} letters."
    print(message)


sayHello("Alice")  # 'Alice' is an argument
sayHello("Bob")  # 'Bob' is an argument
wizard_name = "Gandalf"
sayHello(wizard_name)  # The value of wizard_name ('Gandalf') is an argument

# %% [markdown] id="dragon-game-results" slideshow={"slide_type": "slide"}
# ## Building Suspense: Displaying Game Results with `time.sleep()`
#
# The `time.sleep()` function pauses the program for a number of seconds. This adds drama!
# Shorter pauses are used in this demo cell.

# %% slideshow={"slide_type": "fragment"}
import time  # Make sure time is imported for this cell

print("You approach the cave...")
time.sleep(0.5)  # Pause for 0.5 seconds
print("It is dark and spooky...")
time.sleep(0.5)  # Pause for 0.5 seconds
print("A large dragon jumps out in front of you! He opens his jaws and...")
time.sleep(0.5)  # Pause for 0.5 seconds
print("...the story continues!")

# %% [markdown] id="dragon-deciding-fate" slideshow={"slide_type": "slide"}
# ## Fate's Choice: Deciding the Friendly Dragon
#
# How does the game decide which dragon is friendly?
#
# ```python
# # Snippet from checkCave(chosenCave):
# # friendlyCave = random.randint(1, 2)
# #
# # if chosenCave == str(friendlyCave):
# #     print('Gives you his treasure!')
# # else:
# #     print('Eats you and spends your robux!')
# ```
# * `random.randint(1, 2)`: Randomly picks 1 or 2.
# * `str(friendlyCave)`: Converts the integer `friendlyCave` to a string. This is crucial because `chosenCave` (from `input()`) is a string.

# %% [markdown] slideshow={"slide_type": "fragment"}
# Let's simulate this choice:
# %% slideshow={"slide_type": "fragment"}
import random  # Ensure random is imported

# Simulate player's choice
player_chosen_cave_str = random.choice(["1", "2"])  # Player randomly picks '1' or '2'
print(f"Player chose cave: {player_chosen_cave_str}")

# Determine the friendly dragon's cave
friendly_dragon_cave_int = random.randint(1, 2)
friendly_dragon_cave_str = str(friendly_dragon_cave_int)
print(f"The friendly dragon is in cave: {friendly_dragon_cave_str}")

# Check the outcome
if player_chosen_cave_str == friendly_dragon_cave_str:
    print("Gives you his treasure!")
else:
    print("Eats you and spends your robux!")

# %% [markdown] id="dragon-game-loop" slideshow={"slide_type": "slide"}
# ## The Adventure Continues: The Main Game Loop
#
# The game allows playing multiple times using a `while` loop:
#
# ```python
# # Structure of the main game loop in dragon.py
# playAgain = 'yes'
# while playAgain == 'yes' or playAgain == 'y':
#     # ... game logic starts here ...
#     displayIntro()
#     caveNumber = chooseCave()
#     checkCave(caveNumber)
#     # ... game logic ends ...
#
#     print('Do you want to play again? (yes or no)')
#     playAgain = input()
# ```
# * `playAgain` is initialized to `'yes'` to ensure the loop runs at least once.
# * The loop continues based on player's input.
# * Our custom functions are called to run the game.
# (This is a structural overview, `input()` makes direct demo in static slides tricky).

# %% [markdown] id="dragon-full-code-title" slideshow={"slide_type": "slide"}
# ## The Complete Scroll: `dragon.py`
#
# Below is the entire script for Dragon Realm. This code cell contains the full game. If you were running this notebook interactively (and not just viewing slides), you could execute this cell to play the game (it would prompt for input in your Jupyter interface).

# %% id="dragon-full-code-cell" slideshow={"slide_type": "fragment"}
# dragon.py (Full Source Code)
import random
import time


def displayIntro():
    print(
        """You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight."""
    )
    print()


def chooseCave():
    cave = ""
    # Input validation loop
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()  # Jupyter will show an input box here if run interactively
    return cave


def checkCave(
    chosenCave_param,
):  # Renamed parameter to avoid conflict if cell is run multiple times
    print("You approach the cave...")
    time.sleep(1)  # Slightly shorter sleeps for faster game in demo
    print("It is dark and spooky...")
    time.sleep(1)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()  # Adds a blank line for readability
    time.sleep(1)

    friendlyCave_num = random.randint(1, 2)

    if chosenCave_param == str(friendlyCave_num):
        print("Gives you his treasure!")
    else:
        print("Eats you and spends your robux!")


# Main game loop
# playAgain = 'yes' # This variable would control the loop
# To actually run the game from this cell, you'd uncomment the loop
# and the initial 'playAgain' and run the cell. For static slides,
# we usually don't run interactive input loops.

# Example of how the main game loop would start:
# print("--- Starting Dragon Realm Game (Conceptual Run) ---")
# displayIntro()
# player_choice = chooseCave() # This would prompt for input
# checkCave(player_choice)
# print("--- End of Conceptual Run ---")
# print("To play fully, you'd need the 'playAgain' loop and run this cell interactively.")


# %% [markdown] id="dragon-summary" slideshow={"slide_type": "slide"}
# ## Treasures Unlocked: Summary
#
# In our Dragon Realm quest, we learned:
# * **Functions (`def`)** organize code into reusable blocks.
# * **Arguments & Parameters** pass data to functions.
# * **Return values** get data back from functions.
# * **Scopes (local/global)** determine where variables live.
# * **Boolean logic (`and`, `or`, `not`)** helps make decisions.
# * **`while` loops** repeat code based on a condition.
# * **`time.sleep()`** adds pauses for effect.
# * **`random.randint()`** introduces unpredictability.
#
# Functions are fundamental to writing clean, manageable, and powerful Python programs!

# %% [markdown] id="dragon-end" slideshow={"slide_type": "slide"}
# ## Your Quest is Complete!
#
# You've bravely faced the Dragon Realm and learned valuable Python spells!
#
# <img src="https://www.publicdomainpictures.net/pictures/200000/velka/treasure-chest-14691182017IL.jpg" alt="Treasure Chest" style="height: 250px;"/>
#
# What adventures will you code next?
#
# (Reminder: Images from the tutorial like `images/00016.jpeg` need to be in an 'images' subdirectory for them to display.)

# %% [markdown] slideshow={"slide_type": "skip"}
# ### Notes for Presenter (and to ensure images work):
#
# 1.  Make sure you have an `images` folder in the same directory as this Jupyter Notebook.
# 2.  Place the images from the tutorial (`00016.jpeg`, `00061.jpeg`, `00062.jpeg`, `00064.jpeg`) into that `images` folder.
# 3.  The treasure chest image is linked from an external source for variety.
# 4.  To run these slides:
#     * Make sure you have `nbconvert` and its dependencies: `pip install jupyter nbconvert`
#     * From your terminal, navigate to the directory containing this notebook and run:
#         `jupyter nbconvert your_notebook_name.ipynb --to slides --post serve --ExecutePreprocessor.enabled=True --execute`
#         (Replace `your_notebook_name.ipynb` with the actual filename).
#     * Using `--execute` will run the cells and embed their outputs. Be cautious with cells that expect `input()` if you pre-execute for static slides, as they might cause the conversion to hang or require default input handling. For the full `dragon.py` cell, it's mostly commented out to prevent issues with `input()` during automatic execution for slide generation.
#     * For a better interactive slide experience with `input()`, tools like RISE (`pip install RISE`) are recommended, which allow live execution within the slideshow.
