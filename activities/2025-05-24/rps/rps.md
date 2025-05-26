# Python Homework: Rock Paper Scissors Game with Functions

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

-----

## Initial Setup

For this homework, you'll be building a Rock Paper Scissors game piece by piece. Start with an empty Python file. You will add to it in each step.

-----

## Step 1: Greeting the Player

### Problem

Every good game starts with an introduction. Your first task is to create a function that prints a greeting message from the game's "champion," Mitsuru Nagase.

  * Define a function named `show_intro`.
  * Inside this function, print the following two lines:
    ```
    Greetings! I am Mitsuru Nagase (永瀬 充)
    I'm the Rock Paper Scissor champion seven years in a row!
    ```
    Followed by a blank line (an empty `print()`).
  * After defining the function, **call** `show_intro()` to display the greeting.

Your program's output should be:

```
Greetings! I am Mitsuru Nagase (永瀬 充)
I'm the Rock Paper Scissor champion seven years in a row!

```

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

Remember how to define a function using `def function_name():`. The `print()` statements will go inside this function, indented. To call the function, you simply type its name followed by parentheses: `function_name()`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()

show_intro()
```

</details>

-----

## Step 2: Asking the Player if They Want to Play

### Problem

Now that you've greeted the player, you need to ask if they want to play.

  * Define a new function called `ask_player_to_play`.
  * Inside this function:
      * Print the question: "Do you want to play a game? (yes or no)"
      * Get the player's input using `input()`.
      * Print a blank line.
      * If the player's answer is "y" or "yes", the function should **return** `True`.
      * Otherwise, it should **return** `False`.
  * Keep the `show_intro()` function and its call from Step 1.
  * After calling `show_intro()`, call your new `ask_player_to_play()` function and store its returned value in a variable (e.g., `player_wants_to_play`).
  * For now, you don't need to do anything with this variable, but it will be used in later steps.

If the player types "yes", the program's interaction might look like:

```
Greetings! I am Mitsuru Nagase (永瀬 充)
I'm the Rock Paper Scissor champion seven years in a row!

Do you want to play a game? (yes or no)
yes

```

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * Your `ask_player_to_play` function will need an `if` statement to check the user's input.
  * Use the `or` operator to check for both "y" and "yes".
  * Remember the `return` keyword to send a value back from the function.
  * When you call `ask_player_to_play()`, use an assignment statement like `variable_name = ask_player_to_play()` to capture the returned boolean.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()


def ask_player_to_play():
    print("Do you want to play a game? (yes or no)")
    ans = input()
    print()
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

show_intro()
player_wants_to_play = ask_player_to_play()
```

</details>

-----

## Step 3: Getting the Player's Move

### Problem

If the player wants to play, you need to ask for their move (Rock, Paper, or Scissors).

  * Define a new function called `get_player_move`.
  * Inside this function:
      * Prompt the user with: "Rock, Paper, or Scissors? (r, p, or s): "
      * Get the player's input.
      * The function should **return** the player's input (which will be "r", "p", or "s").
  * Keep all the code from Step 2.
  * Now, use an `if` statement to check the value of the `player_wants_to_play` variable.
      * If `player_wants_to_play` is `True`:
          * Call `get_player_move()` and store the result in a variable (e.g., `player_move`).
          * Print "You chose " followed by the player's move.
      * Else (if `player_wants_to_play` is `False`):
          * Print "Ok, bye!"

Example interaction if player says "yes" and chooses "r":

```
Greetings! I am Mitsuru Nagase (永瀬 充)
I'm the Rock Paper Scissor champion seven years in a row!

Do you want to play a game? (yes or no)
yes

Rock, Paper, or Scissors? (r, p, or s): r
You chose r
```

Example interaction if player says "no":

```
Greetings! I am Mitsuru Nagase (永瀬 充)
I'm the Rock Paper Scissor champion seven years in a row!

Do you want to play a game? (yes or no)
no

Ok, bye!
```

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * The `get_player_move` function is straightforward: `input()` and `return`.
  * The main part of your script (after the function definitions) will now have an `if/else` structure based on the boolean value returned by `ask_player_to_play()`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()


def ask_player_to_play():
    print("Do you want to play a game? (yes or no)")
    ans = input()
    print()
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

def get_player_move():
    move = input("Rock, Paper, or Scissors? (r, p, or s): ")
    return move

show_intro()
player_wants_to_play = ask_player_to_play()

if player_wants_to_play:
    player_move = get_player_move()
    print("You chose " + player_move)
else:
    print("Ok, bye!")
```

</details>

-----

## Step 4: Getting the Computer's Move

### Problem

Now it's time for the computer to make its move!

  * At the very top of your script, add `import random`.
  * Define a new function called `get_computer_move`.
  * This function should not take any arguments.
  * Inside this function, use `random.choice()` to randomly select one item from the list `["r", "p", "s"]`.
  * The function should **return** the computer's chosen move.
  * Keep all the code from Step 3.
  * Inside the `if player_wants_to_play:` block (after getting and printing the player's move):
      * Call `get_computer_move()` and store the result in a variable (e.g., `computer_move`).
      * Print "Computer chose " followed by the computer's move.

Example interaction (computer's move will be random):

```
Greetings! I am Mitsuru Nagase (永瀬 充)
I'm the Rock Paper Scissor champion seven years in a row!

Do you want to play a game? (yes or no)
yes

Rock, Paper, or Scissors? (r, p, or s): p
You chose p
Computer chose s
```

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * Make sure `import random` is the first line of your program.
  * The `get_computer_move` function will use `return random.choice([...])`. What should be in the `[...]`?
  * The calls to get the player's move and then the computer's move should happen sequentially if the player decided to play.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
import random


def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()


def ask_player_to_play():
    print("Do you want to play a game? (yes or no)")
    ans = input()
    print()
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

def get_player_move():
    move = input("Rock, Paper, or Scissors? (r, p, or s): ")
    return move

def get_computer_move():
    return random.choice(["r", "p", "s"])

show_intro()
player_wants_to_play = ask_player_to_play()

if player_wants_to_play:
    player_move = get_player_move()
    print("You chose " + player_move)

    computer_move = get_computer_move()
    print("Computer chose " + computer_move)
else:
    print("Ok, bye!")
```

</details>

-----

## Step 5: Determining the Winner

### Problem

With both moves made, you need a function to decide who won the round.

  * Define a new function called `determine_winner` that takes two arguments: `player_move` and `computer_move`.
  * Inside this function, use `if/elif/else` statements to compare the moves and determine the winner based on the rules of Rock Paper Scissors:
      * Rock (r) beats Scissors (s)
      * Paper (p) beats Rock (r)
      * Scissors (s) beats Paper (p)
  * The function should **return**:
      * `"tie"` if it's a tie.
      * `"player"` if the player wins.
      * `"computer"` if the computer wins.
  * Keep all the code from Step 4.
  * For this step, you will define the `determine_winner` function, but you **will not call it yet**. We will call it and use its result in the next step.

### Hint

<details>
<summary>Stuck on Step 5? Click for a hint!</summary>

  * Your function signature will be `def determine_winner(player_move, computer_move):`.
  * The first condition to check is if `player_move == computer_move`.
  * Then, use `elif` for player win conditions (e.g., `player_move == "r" and computer_move == "s"`). There will be three such conditions for the player winning.
  * If none of the tie or player-win conditions are met, the `else` block means the computer wins.
  * Make sure each path has a `return` statement.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 5? Click to reveal!</summary>

```python
import random


def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()


def ask_player_to_play():
    print("Do you want to play a game? (yes or no)")
    ans = input()
    print()
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

def get_player_move():
    move = input("Rock, Paper, or Scissors? (r, p, or s): ")
    return move

def get_computer_move():
    return random.choice(["r", "p", "s"])

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif player_move == "r" and computer_move == "s":
        return "player"
    elif player_move == "p" and computer_move == "r":
        return "player"
    elif player_move == "s" and computer_move == "p":
        return "player"
    else:
        return "computer"

show_intro()
player_wants_to_play = ask_player_to_play()

if player_wants_to_play:
    player_move = get_player_move()
    print("You chose " + player_move)

    computer_move = get_computer_move()
    print("Computer chose " + computer_move)
    # We will call determine_winner in the next step
else:
    print("Ok, bye!")
```

</details>

-----

## Step 6: Announcing the Winner of the Round

### Problem

Now, let's use the `determine_winner` function and announce the result.

  * Keep all the code from Step 5.
  * Inside the `if player_wants_to_play:` block, after getting and printing both moves:
      * Call your `determine_winner` function, passing in the `player_move` and `computer_move` variables as arguments. Store the returned value in a variable (e.g., `winner`).
      * Use another `if/elif/else` structure to check the value of `winner`:
          * If `winner` is `"player"`, print "You win!".
          * If `winner` is `"computer"`, print "You lose!".
          * Else (if `winner` is `"tie"`), print "It's a tie!".

Example interaction:

```
Greetings! I am Mitsuru Nagase (永瀬 充)
I'm the Rock Paper Scissor champion seven years in a row!

Do you want to play a game? (yes or no)
y

Rock, Paper, or Scissors? (r, p, or s): r
You chose r
Computer chose s
You win!
```

### Hint

<details>
<summary>Stuck on Step 6? Click for a hint!</summary>

  * Make sure you pass the correct arguments to `determine_winner(player_move, computer_move)`.
  * The `if/elif/else` block for announcing the result will compare the string returned by `determine_winner` (e.g., `if winner == "player":`).

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 6? Click to reveal!</summary>

```python
import random


def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()


def ask_player_to_play():
    print("Do you want to play a game? (yes or no)")
    ans = input()
    print()
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

def get_player_move():
    move = input("Rock, Paper, or Scissors? (r, p, or s): ")
    return move

def get_computer_move():
    return random.choice(["r", "p", "s"])

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif player_move == "r" and computer_move == "s":
        return "player"
    elif player_move == "p" and computer_move == "r":
        return "player"
    elif player_move == "s" and computer_move == "p":
        return "player"
    else:
        return "computer"

show_intro()

player_wants_to_play = ask_player_to_play()

if player_wants_to_play:
    player_move = get_player_move()
    print("You chose " + player_move)

    computer_move = get_computer_move()
    print("Computer chose " + computer_move)

    winner = determine_winner(player_move, computer_move)

    if winner == "player":
        print("You win!")
    elif winner == "computer":
        print("You lose!")
    else:
        print("It's a tie!")
else:
    print("Ok, bye!")
```

</details>

-----

## Step 7: Playing Multiple Rounds

### Problem

Most games allow you to play more than once. Let's add a loop so the player can play again.

  * Keep all your functions as they are.
  * Modify the main part of your script (after function definitions and `show_intro()` call).
  * The game logic (getting moves, determining winner, announcing winner) should now be inside a `while` loop.
  * The `while` loop should continue as long as `player_wants_to_play` is `True`.
  * Inside the loop, after a round is played and the winner is announced, you need to call `ask_player_to_play()` again to ask the user if they want to play another round. The result of this call should update the `player_wants_to_play` variable, which will control if the loop continues.
  * If the loop finishes (meaning `player_wants_to_play` became `False`), print "Ok, bye!".

Example interaction for two rounds:

```
Greetings! I am Mitsuru Nagase (永瀬 充)
I'm the Rock Paper Scissor champion seven years in a row!

Do you want to play a game? (yes or no)
y

Rock, Paper, or Scissors? (r, p, or s): r
You chose r
Computer chose p
You lose!
Do you want to play a game? (yes or no)
yes

Rock, Paper, or Scissors? (r, p, or s): s
You chose s
Computer chose p
You win!
Do you want to play a game? (yes or no)
no

Ok, bye!
```

### Hint

<details>
<summary>Stuck on Step 7? Click for a hint!</summary>

  * Your first call to `player_wants_to_play = ask_player_to_play()` will happen *before* the `while` loop starts, to initialize the loop condition.
  * The `while player_wants_to_play:` loop will contain the code that was previously in your `if player_wants_to_play:` block.
  * At the *end* of the `while` loop's body, you'll have `player_wants_to_play = ask_player_to_play()` again.
  * The "Ok, bye!" message should be printed *after* the `while` loop has finished.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 7? Click to reveal!</summary>

```python
import random


def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()


def ask_player_to_play():
    print("Do you want to play a game? (yes or no)")
    ans = input()
    print()
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

def get_player_move():
    move = input("Rock, Paper, or Scissors? (r, p, or s): ")
    return move

def get_computer_move():
    return random.choice(["r", "p", "s"])

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif player_move == "r" and computer_move == "s":
        return "player"
    elif player_move == "p" and computer_move == "r":
        return "player"
    elif player_move == "s" and computer_move == "p":
        return "player"
    else:
        return "computer"

show_intro()

player_wants_to_play = ask_player_to_play()

while player_wants_to_play:
    player_move = get_player_move()
    print("You chose " + player_move)

    computer_move = get_computer_move()
    print("Computer chose " + computer_move)

    winner = determine_winner(player_move, computer_move)

    if winner == "player":
        print("You win!")
    elif winner == "computer":
        print("You lose!")
    else:
        print("It's a tie!")

    player_wants_to_play = ask_player_to_play()

print("Ok, bye!")
```

</details>

-----

## Step 8: Keeping Score

### Problem

Let's make the game more interesting by keeping score!

  * Before the `show_intro()` call, initialize two variables: `player_score = 0` and `computer_score = 0`. These should be global variables.
  * Inside the `while` loop, when a winner is determined:
      * If the player wins, increment `player_score` by 1.
      * If the computer wins, increment `computer_score` by 1.
  * After the `while` loop finishes (after printing "Ok, bye!"), print the final scores. The output should look like this:
    ```
    ==============================
    Final score:
    You: <player_score_value>
    Computer: <computer_score_value>
    ==============================
    ```
    (Replace `<player_score_value>` and `<computer_score_value>` with the actual scores).

Example interaction (scores depend on game outcomes):

```
... (game rounds) ...
Do you want to play a game? (yes or no)
n

Ok, bye!
==============================
Final score:
You: 1
Computer: 2
==============================
```

### Hint

<details>
<summary>Stuck on Step 8? Click for a hint!</summary>

  * Declare `player_score` and `computer_score` near the top of your script, outside of any functions.
  * Inside the loop, where you print "You win!" or "You lose!", add `player_score = player_score + 1` or `computer_score = computer_score + 1`.
  * To print the final score section, use multiple `print()` statements. Remember to convert the score variables (which are integers) to strings using `str()` before concatenating them with other strings for printing.
  * `print("=" * 30)` is a neat trick to print a line of 30 equal signs.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 8? Click to reveal!</summary>

```python
import random


def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()


def ask_player_to_play():
    print("Do you want to play a game? (yes or no)")
    ans = input()
    print()
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

def get_player_move():
    move = input("Rock, Paper, or Scissors? (r, p, or s): ")
    return move

def get_computer_move():
    return random.choice(["r", "p", "s"])

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif player_move == "r" and computer_move == "s":
        return "player"
    elif player_move == "p" and computer_move == "r":
        return "player"
    elif player_move == "s" and computer_move == "p":
        return "player"
    else:
        return "computer"

player_score = 0
computer_score = 0

show_intro()

player_wants_to_play = ask_player_to_play()

while player_wants_to_play:
    player_move = get_player_move()
    print("You chose " + player_move)

    computer_move = get_computer_move()
    print("Computer chose " + computer_move)

    winner = determine_winner(player_move, computer_move)

    if winner == "player":
        print("You win!")
        player_score = player_score + 1
    elif winner == "computer":
        print("You lose!")
        computer_score = computer_score + 1
    else:
        print("It's a tie!")

    player_wants_to_play = ask_player_to_play()

print("Ok, bye!")

print("=" * 30)
print("Final score:")
print("You: " + str(player_score))
print("Computer: " + str(computer_score))
print("=" * 30)
```

</details>

-----

## You Finished! 🎉

You've practiced:

  * Defining and calling **functions** (`def`).
  * Functions that take **arguments** and **return values**.
  * Using `input()` to get user input.
  * Using the `random` module, specifically `random.choice()`.
  * Conditional logic with `if/elif/else` statements.
  * Using `while` loops to repeat parts of your program.
  * Working with string comparisons and boolean values.
  * Initializing and updating variables to keep score.
