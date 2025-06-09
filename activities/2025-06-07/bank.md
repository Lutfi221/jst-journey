# Python Homework: Building a Bank Terminal

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

-----

## Final Goal

When you're finished, you will have built a simple command-line banking application. A user can interact with it, and a sample session will look like this:

```
Hi! Welcome to the Money Bank!

What is your name? Twilight

------------------------------
BALANCE: $100

What do you want to do?
1. Deposit
2. Withdraw
3. See transaction history
4. Exit

 > 1

How much do you want to deposit? 21
Successfully deposited $21.

------------------------------
BALANCE: $121

What do you want to do?
1. Deposit
2. Withdraw
3. See transaction history
4. Exit

 > 2

How much do you want to withdraw? 5
Successfully withdrew $5.

------------------------------
BALANCE: $116

What do you want to do?
1. Deposit
2. Withdraw
3. See transaction history
4. Exit

 > 3

--- Transaction History ---
 - Twilight deposited $21
 - Twilight withdrew $5
---------------------------

------------------------------
BALANCE: $116

What do you want to do?
1. Deposit
2. Withdraw
3. See transaction history
4. Exit

 > 4

Good bye!
```

-----

## Step 1: Greeting and Setup

### Problem

Let's start by setting up the bank. Create a function to greet the user, set up some starting variables for the account, and ask for the user's name.

Your script should:

1.  Define a function called `greet` that prints a welcome message.
2.  Initialize a `balance` variable to `100`.
3.  Initialize an empty list called `transactions`.
4.  Call the `greet` function.
5.  Ask the user for their name and store it in a `name` variable.

When you run your code for this step, it should simply greet you and wait for your name.

```
Hi! Welcome to the Money Bank!

What is your name? Twilight
```

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  * Define the function using `def greet():`. The `print()` statements go inside it.
  * A list is created with square brackets: `[]`.
  * Use the `input()` function to get the user's name.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()
```

</details>

-----

## Step 2: The Main Menu Loop

### Problem

Now, let's create the main part of the program. Add a loop that continuously shows the user their balance and the available options.

Your script should:

1.  Start an infinite `while` loop after getting the user's name.
2.  Inside the loop, print a separator line (e.g., `"-" * 30`).
3.  Print the current balance.
4.  Print the menu of options (Deposit, Withdraw, History, Exit).
5.  Prompt the user for their choice and store it in a variable.

For now, this loop will run forever after you enter a choice. You'll have to manually stop your program. We'll fix that in the next step.

```
...
------------------------------
BALANCE: $100

What do you want to do?
1. Deposit
2. Withdraw
3. See transaction history
4. Exit

 > 
```

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * An infinite loop can be created with `while True:`.
  * Remember to convert the `balance` variable to a string using `str()` before you can add it to other strings for printing.
  * You can use `\n` to create new lines within a single `print` statement for the menu.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()

while True:
    print("-" * 30)
    print("BALANCE: $" + str(balance))
    print()

    print(
        "What do you want to do?\n"
        "1. Deposit\n"
        "2. Withdraw\n"
        "3. See transaction history\n"
        "4. Exit"
    )
    print()

    choice = input(" > ")
    print()
```

</details>

-----

## Step 3: Handling the "Exit" Choice

### Problem

Let's give the user a way to exit the program. If the user's choice is `4`, the program should print a goodbye message and terminate.

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * The `choice` variable from `input()` is a string. You need to convert it to a number using `int()`.
  * Use an `if` statement to check if `choice == 4`.
  * The `break` keyword will exit the current `while` loop.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()

while True:
    print("-" * 30)
    print("BALANCE: $" + str(balance))
    print()

    print(
        "What do you want to do?\n"
        "1. Deposit\n"
        "2. Withdraw\n"
        "3. See transaction history\n"
        "4. Exit"
    )
    print()

    choice = input(" > ")
    print()

    choice = int(choice)

    if choice == 4:
        print("Good bye!")
        break
    
    print() #This extra print will be used by other options later
```

</details>

-----

## Step 4: Implementing "Deposit"

### Problem

Now for the first real banking feature: depositing money. If the user's choice is `1`, your program should ask for an amount and add it to the balance.

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * Add an `if choice == 1:` condition.
  * Use `input()` to ask for the amount to deposit.
  * Convert the amount from a string to an integer using `int()`.
  * Update the `balance` variable by using addition (`balance = balance + deposit_amount`).

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()

while True:
    print("-" * 30)
    print("BALANCE: $" + str(balance))
    print()

    print(
        "What do you want to do?\n"
        "1. Deposit\n"
        "2. Withdraw\n"
        "3. See transaction history\n"
        "4. Exit"
    )
    print()

    choice = input(" > ")
    print()

    choice = int(choice)

    if choice == 1:
        deposit_amount = int(input("How much do you want to deposit? "))
        balance = balance + deposit_amount
        print("Successfully deposited $" + str(deposit_amount))

    elif choice == 4: # Use elif here as we will add more choices
        print("Good bye!")
        break
    
    print()
```

</details>

-----

## Step 5: Implementing "Withdraw"

### Problem

Next, implement the withdrawal feature. If the user's choice is `2`, ask for an amount to withdraw. You must check if the user has enough funds *before* allowing the withdrawal.

### Hint

<details>
<summary>Stuck on Step 5? Click for a hint!</summary>

  * Add an `elif choice == 2:`.
  * Get the `withdraw_amount` from the user and convert it to an `int`.
  * Inside this block, you'll need another `if` statement to check if `withdraw_amount > balance`.
  * If it is, print an "Insufficient funds" message.
  * Otherwise (in an `else` block), subtract the amount from the `balance`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 5? Click to reveal!</summary>

```python
def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()

while True:
    print("-" * 30)
    print("BALANCE: $" + str(balance))
    print()

    print(
        "What do you want to do?\n"
        "1. Deposit\n"
        "2. Withdraw\n"
        "3. See transaction history\n"
        "4. Exit"
    )
    print()

    choice = input(" > ")
    print()

    choice = int(choice)

    if choice == 1:
        deposit_amount = int(input("How much do you want to deposit? "))
        balance = balance + deposit_amount
        print("Successfully deposited $" + str(deposit_amount))

    elif choice == 2:
        withdraw_amount = int(input("How much do you want to withdraw? "))
        if withdraw_amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - withdraw_amount
            print("Successfully withdrew $" + str(withdraw_amount))
            
    elif choice == 4:
        print("Good bye!")
        break
        
    print()
```

</details>

-----

## Step 6: Recording Transactions

### Problem

A bank needs to keep records. Modify your deposit and withdraw logic to record each transaction. When a user successfully deposits or withdraws, add a descriptive string to the `transactions` list.

### Hint

<details>
<summary>Stuck on Step 6? Click for a hint!</summary>

  * You will be modifying the code inside the `if choice == 1:` and the `else` part of `elif choice == 2:`.
  * Use the list's `.append()` method to add a new string.
  * Construct a string that includes the user's name, the action, and the amount. For example: `name + " deposited $" + str(deposit_amount)`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 6? Click to reveal!</summary>

```python
def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()

while True:
    print("-" * 30)
    print("BALANCE: $" + str(balance))
    print()

    print(
        "What do you want to do?\n"
        "1. Deposit\n"
        "2. Withdraw\n"
        "3. See transaction history\n"
        "4. Exit"
    )
    print()

    choice = input(" > ")
    print()

    choice = int(choice)

    if choice == 1:
        deposit_amount = int(input("How much do you want to deposit? "))
        balance = balance + deposit_amount
        transactions.append(name + " deposited $" + str(deposit_amount))
        print("Successfully deposited $" + str(deposit_amount))

    elif choice == 2:
        withdraw_amount = int(input("How much do you want to withdraw? "))
        if withdraw_amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - withdraw_amount
            transactions.append(name + " withdrew $" + str(withdraw_amount))
            print("Successfully withdrew $" + str(withdraw_amount))

    elif choice == 4:
        print("Good bye!")
        break

    print()
```

</details>

-----

## Step 7: Displaying Transaction History

### Problem

Now that you're recording transactions, let's give the user a way to see them. If the user's choice is `3`, display the full history of transactions.

### Hint

<details>
<summary>Stuck on Step 7? Click for a hint!</summary>

  * Add an `elif choice == 3:`.
  * Inside this block, it's good practice to first check if the `transactions` list is empty. Use `len(transactions) == 0`. If it is, print "No transactions yet."
  * If the list is not empty, use a `for` loop to iterate through each `transaction` in the `transactions` list and print it.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 7? Click to reveal!</summary>

```python
def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()

while True:
    print("-" * 30)
    print("BALANCE: $" + str(balance))
    print()

    print(
        "What do you want to do?\n"
        "1. Deposit\n"
        "2. Withdraw\n"
        "3. See transaction history\n"
        "4. Exit"
    )
    print()

    choice = input(" > ")
    print()

    choice = int(choice)

    if choice == 1:
        deposit_amount = int(input("How much do you want to deposit? "))
        balance = balance + deposit_amount
        transactions.append(name + " deposited $" + str(deposit_amount))
        print("Successfully deposited $" + str(deposit_amount))

    elif choice == 2:
        withdraw_amount = int(input("How much do you want to withdraw? "))
        if withdraw_amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - withdraw_amount
            transactions.append(name + " withdrew $" + str(withdraw_amount))
            print("Successfully withdrew $" + str(withdraw_amount))

    elif choice == 3:
        print("--- Transaction History ---")
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(" - " + transaction)
        print("---------------------------")

    elif choice == 4:
        print("Good bye!")
        break
        
    print()
```

</details>

-----

## Step 8: Handling Invalid Input

### Problem

Finally, let's make our program more robust by handling invalid menu choices. If the user enters a number that is not 1, 2, 3, or 4, print a message letting them know you don't understand.

### Hint

<details>
<summary>Stuck on Step 8? Click for a hint!</summary>

  * At the very end of your `if/elif` chain, you can add an `else:` block. This code will only run if none of the previous `if` or `elif` conditions were true.
  * Inside the `else:` block, simply print a message like "I don't understand that choice."

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 8? Click to reveal!</summary>

```python
def greet():
    print("Hi! Welcome to the Money Bank!")
    print()

balance = 100
transactions = []

greet()

name = input("What is your name? ")
print()

while True:
    print("-" * 30)
    print("BALANCE: $" + str(balance))
    print()

    print(
        "What do you want to do?\n"
        "1. Deposit\n"
        "2. Withdraw\n"
        "3. See transaction history\n"
        "4. Exit"
    )
    print()

    choice = input(" > ")
    print()

    choice = int(choice)

    if choice == 1:
        deposit_amount = int(input("How much do you want to deposit? "))
        balance = balance + deposit_amount
        transactions.append(name + " deposited $" + str(deposit_amount))
        print("Successfully deposited $" + str(deposit_amount))

    elif choice == 2:
        withdraw_amount = int(input("How much do you want to withdraw? "))
        if withdraw_amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - withdraw_amount
            transactions.append(name + " withdrew $" + str(withdraw_amount))
            print("Successfully withdrew $" + str(withdraw_amount))

    elif choice == 3:
        print("--- Transaction History ---")
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(" - " + transaction)
        print("---------------------------")

    elif choice == 4:
        print("Good bye!")
        break

    else:
        print("I don't understand that choice.")

    print()
```

</details>

-----

## You Finished!

You've built a complete, interactive command-line application! You have practiced:

  * Defining and calling functions.
  * Using variables to store numbers (`int`), strings (`str`), and lists (`[]`).
  * Getting user input with `input()`.
  * Controlling program flow with a `while` loop and `if/elif/else` statements.
  * Using `break` to exit a loop.
  * Converting between data types with `int()` and `str()`.
  * Modifying lists with `.append()`.
  * Checking the length of a list with `len()`.
  * Iterating through a list with a `for` loop.

Great job!