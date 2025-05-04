# Python Homework: Loops and Conditionals

Follow the steps below. For each step:
1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

---

## Step 1: Counting with a Loop

### Problem

Your first task is simple: Print the numbers from 0 up to and including 10, with each number on a new line. You *must* use a `for` loop and the `range()` function.

Here's what your program should output mate.

```
0
1
...
9
10
```

### Hint

<details>
  <summary>Stuck on Step 1? Click for a hint!</summary>

  Remember that `range(x)` generates numbers starting from 0 up to (but not including) `x`. If you want to include 10, what number should `x` be?

  Your loop structure will look something like `for number in range(...):`. What should go inside the `range()`? And what should you `print()` inside the loop?

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
for num in range(11):
    print(num)
```

**Explanation:**
*   `for num in range(11):` sets up a loop that will run 11 times. The variable `num` will take on the values 0, 1, 2, ..., up to 10 in each iteration.
*   `print(num)` inside the loop prints the current value of `num`. Since this is inside the loop, it prints `num` every time the loop runs.

</details>

---

## Step 2: Using the Loop Variable

### Problem

Now, let's use the number (`num` variable) from the loop in the output to make a multiplication table. Write a loop that prints a 7x multiplication table for numbers 1 through 10. The output for each line should look like this:

```
7 * 1 =
7 * 2 =
...
7 * 10 =
```

Notice that we are starting from 1 this time, not 0. And we don't care about the results of the multiplication problems yet.

### Hint

<details>
  <summary>Stuck on Step 2? Click for a hint!</summary>

  How can you make `range()` start at 1 instead of 0? Remember that `range()` can take two arguments: `range(start, stop)`. The `stop` value is *not* included.

  Inside the loop, you'll need to print a string. This string should combine the fixed text `"7 * "` with the current number from your loop and `" = "`. You'll need to convert the loop number to a string to combine them using the `+` operator.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
for num in range(1, 11):
    print("7 * " + str(num) + " = ")
```

**Explanation:**
*   `for num in range(1, 11):` sets up a loop that runs for numbers starting from 1 up to (but not including) 11. So `num` will be 1, 2, ..., 10.
*   `print("7 * " + str(num) + " = ")` concatenates three strings: `"7 * "`, the string representation of the current number (`str(num)`), and `" = "`. This combined string is then printed.

</details>

---

## Step 3: Doing Math Inside the Loop

### Problem

Let's complete the 7 times table. Modify your code from Step 2 so that it calculates and prints the actual answer for each multiplication problem. The output should look like this:

```
7 * 1 = 7
7 * 2 = 14
...
7 * 10 = 70
```

### Hint

<details>
  <summary>Stuck on Step 3? Click for a hint!</summary>

  Inside the loop, before you print, you need to calculate `7 * num`. You can store the result of this calculation in a variable, like `answer`.

  Then, when you print, you'll need to add this `answer` to your string. Remember that `answer` will be a number, so you'll need to convert it to a string using `str()` before you can concatenate it with the other string parts.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
for num in range(1, 11):
    answer = 7 * num
    print("7 * " + str(num) + " = " + str(answer))
```

**Explanation:**
*   `for num in range(1, 11):` is the same loop as before (numbers 1 through 10).
*   `answer = 7 * num` performs the multiplication using the fixed number 7 and the current loop number `num`. The result is stored in the `answer` variable.
*   `print("7 * " + str(num) + " = " + str(answer))` concatenates the string parts `"7 * "`, the string version of `num`, `" = "`, and the string version of `answer`. This forms the complete output line.

</details>

---

## Step 4: Dynamic Tables with User Input

### Problem

The 7 times table is cool, but what about other tables? Modify your code so that it first asks the user to "Give me a number". Then, print the multiplication table (from 1 to 10) for the number the user entered.

It should look like this:

```
5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
```

### Hint

<details>
  <summary>Stuck on Step 4? Click for a hint!</summary>

  How do you get input from the user? The `input()` function is what you need.

  Remember that `input()` *always* returns a string. For calculations, you need a number (an integer). How do you convert a string to an integer? Use `int()`.

  Store the user's number in a variable (e.g., `main_number`) *before* the loop starts. Then, inside the loop, use this `main_number` variable in your calculation (`main_number * num`) and in your `print()` statement.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
print("Give me a number")
main_number = input()
main_number = int(main_number)

for num in range(1, 11):
    answer = main_number * num
    print(str(main_number) + " * " + str(num) + " = " + str(answer))
```

**Explanation:**
*   `print("Give me a number")` prompts the user.
*   `main_number = input()` reads the user's input (as a string) and stores it in the `main_number` variable.
*   `main_number = int(main_number)` converts the string input into an integer, overwriting the string value in `main_number`. Now `main_number` is a number we can use in calculations.
*   The loop `for num in range(1, 11):` is the same as before.
*   `answer = main_number * num` performs the multiplication using the user's number and the current loop number.
*   `print(...)` constructs the output string, making sure to convert `main_number`, `num`, and `answer` to strings where necessary.

</details>

---

## Step 5: Using `if` Inside the Loop

### Problem

Let's add a condition! Modify your code from Step 4. It should still ask for a number and print its multiplication table from 1 to 10. However, **skip the line where the multiplier (`num`) is 4.** Because the East Asians considers it unlucky!

If the user enters 5, the output should look like this (notice the missing line for 5 * 4):

```
Give me a number
5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
unlucky
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
```

### Hint

<details>
  <summary>Stuck on Step 5? Click for a hint!</summary>

  You need to decide *whether* to print a line *inside* the loop. This sounds like a job for an `if` statement!

  The condition for your `if` statement should check if the current loop number (`num`) is *not* equal to 4. How do you check for "not equal"? The operator is `!=`.

  The `print()` statement should only happen *if* the condition in your `if` statement is true. Make sure the `print()` statement is indented *inside* the `if` block.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 5? Click to reveal!</summary>

```python
print("Give me a number")
main_number = input()
main_number = int(main_number)

for num in range(1, 11):
    answer = main_number * num
    if num != 4:
        print(str(main_number) + " * " + str(num) + " = " + str(answer))
    else:
        print("unlucky")
```

**Explanation:**
*   The code is the same as Step 4, but with an added `if` statement inside the loop.
*   `if num != 4:` checks if the current value of `num` is not equal to 4.
*   The `print(str(main_number) + ...)` line is indented under the `if` statement. This means that the `print(str(main_number) + ...)` command will only execute if the condition `num != 4` is true.

</details>

---

## You Finished!

You've practiced:
*   Using `for num in range(x)` and `for num in range(start, stop)`.
*   Using the loop variable (`num`) in calculations and `print()` statements.
*   Getting user input and converting it to a number.
*   Putting an `if` statement *inside* a loop to control which actions happen for each item in the loop.
