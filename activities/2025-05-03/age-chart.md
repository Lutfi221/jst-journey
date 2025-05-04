# Python Homework: Loops and Age Categories

Follow the steps below. For each step:
1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

---

## Step 1: Looping Through Ages

### Problem

Let's start by just getting a list of ages. Write a `for` loop using the `range()` function to print numbers from 1 up to and including 29. Each number should be on a new line.

Here's what your program should output:

```
1
2
...
29
```

### Hint

<details>
  <summary>Stuck on Step 1? Click for a hint!</summary>

  Remember that `range()` can take two arguments: `range(start, stop)`. The starting number is included, but the `stop` number is *not* included. If you want to include 29, what number should the `stop` be?

  Your loop structure will be `for age in range(..., ...):`. What should go inside the `range()`? And what should you `print()` inside the loop?

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
for age in range(1, 30):
    print(age)
```

**Explanation:**
*   `for age in range(1, 30):` sets up a loop that will run for numbers starting from 1 up to (but not including) 30. The variable `age` will take on the values 1, 2, ..., up to 29 in each iteration.
*   `print(age)` inside the loop prints the current value of `age`. Since this is inside the loop, it prints `age` every time the loop runs.

</details>

---

## Step 2: Basic Age Categories

### Problem

Now, let's use conditional logic inside the loop. Using the same loop that iterates through ages 1 to 29, add an `if` statement:
*   If the current `age` is less than 18, print the age followed by the word " minor" on the same line.

Ages 18 and over should not print anything in this step.

Your output should look something like this (it stops at age 17):

```
1 minor
2 minor
...
17 minor
```

### Hint

<details>
  <summary>Stuck on Step 2? Click for a hint!</summary>

  You need an `if` statement *inside* your `for` loop. The condition for the `if` should be `age < 18`.

  The `print()` statement that prints the age and " minor" should only happen *if* the `if` condition is true. Make sure it's indented under the `if` statement.

  Remember to convert the `age` (which is a number) to a string using `str()` before combining it with other strings using the `+` operator.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
for age in range(1, 30):
    if age < 18:
        print(str(age) + " minor")
```

**Explanation:**
*   `for age in range(1, 30):` sets up the loop for ages 1 through 29.
*   `if age < 18:` checks if the current value of `age` is less than 18.
*   `print(str(age) + " minor")` is indented under the `if`. This line only runs when the `age` is indeed less than 18. It converts the age to a string and concatenates it with `" minor"`.

</details>

---

## Step 3: Adding Another Category

### Problem

Let's complete the basic categories. Modify your code from Step 2. Keep the loop iterating through ages 1 to 29, and keep the logic for printing " minor". Now, add a *separate* `if` statement:
*   If the current `age` is 18 or greater, print the age followed by the word " adult" on the same line.

Your output should now cover all ages from 1 to 29, with each age labeled as either " minor" or " adult":

```
1 minor
...
17 minor
18 adult
19 adult
...
29 adult
```

### Hint

<details>
  <summary>Stuck on Step 3? Click for a hint!</summary>

  You should have *two* `if` statements inside your `for` loop. Both `if` statements should be at the same level of indentation (indented relative to the `for` loop, but *not* indented relative to each other).

  The first `if` checks `age < 18`. The second `if` checks `age >= 18`.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
for age in range(1, 30):
    if age < 18:
        print(str(age) + " minor")
    if age >= 18: # This is a separate if statement
        print(str(age) + " adult")
```

**Explanation:**
*   The code is the same as Step 2, but we added a second `if` statement at the same level of indentation as the first one.
*   `if age < 18:` handles the "minor" case.
*   `if age >= 18:` handles the "adult" case. Since these are separate `if` statements, Python checks both conditions for every `age` in the loop. For ages less than 18, the first `if` is true. For ages 18 and over, the second `if` is true. (Note: Using `if`/`elif` would be more efficient here, but this step specifically demonstrates using multiple independent `if` checks as shown in your example code).

</details>

---

## Step 4: More Granular Age Categories

### Problem

Let's get more specific with the age categories! Modify your code from Step 3 to implement the following categories based on the `age` (still looping from 1 to 29):
*   If age is less than or equal to 3, print `age` followed by " toddler".
*   If age is greater than 3 AND less than or equal to 8, print `age` followed by " child".
*   If age is greater than 8 AND less than or equal to 12, print `age` followed by " tween".
*   If age is greater than 12 AND less than or equal to 17, print `age` followed by " minor".
*   If age is greater than or equal to 18, print `age` followed by " adult".

You will need multiple `if` statements again, some using the `and` keyword to check ranges.

Your output should now categorize every age from 1 to 29 according to these specific rules:

```
1 toddler
2 toddler
3 toddler
4 child
...
8 child
9 tween
...
12 tween
13 minor
...
17 minor
18 adult
...
29 adult
```

### Hint

<details>
  <summary>Stuck on Step 4? Click for a hint!</summary>

  You'll need one `if` statement for each category. All of these `if` statements should be inside the `for` loop and at the same level of indentation.

  For the conditions that check a range (like "between 3 and 8"), you will use the `and` keyword to combine two comparisons, like `3 < age and age <= 8`.

  Make sure you print the age and the correct category string for each successful `if` condition.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
for age in range(1, 30):
    # if age is less than or equal to 3
    if age <= 3:
        print(str(age) + " toddler")

    # if age is between 3 and 8 (inclusive)
    if 3 < age and age <= 8:
        print(str(age) + " child")

    # if age is between 8 and 12 (inclusive)
    if 8 < age and age <= 12:
        print(str(age) + " tween")

    # if age is between 12 and 17 (inclusive)
    if 12 < age and age <= 17:
        print(str(age) + " minor")

    # if age is greater than or equal to 18
    if age >= 18:
        print(str(age) + " adult")
```

**Explanation:**
*   The loop `for age in range(1, 30):` iterates through each age from 1 to 29.
*   Inside the loop, there are five separate `if` statements, one for each age category.
*   Each `if` statement checks a specific condition (or range of conditions using `and`).
*   If a condition is true for the current `age`, the corresponding `print()` statement (indented under that `if`) executes, printing the age followed by the category label. Since these are all separate `if` statements, Python checks *each* condition for *every* age, even though an age can only fall into one category. (Again, `if`/`elif`/`else` would be more efficient, but this matches the provided code structure).

Here's an alternative solution using `elif`:

```python
for age in range(1, 30):
    if age <= 3:
        print(str(age) + " toddler")
    elif age <= 8:
        print(str(age) + " child")
    elif age <= 12:
        print(str(age) + " tween")
    elif age <= 17:
        print(str(age) + " minor")
    else:
        # then it must be an adult
        print(str(age) + " adult")
```

</details>

---

## You Finished!

You've practiced:
*   Using `for` loops with `range(start, stop)` to iterate through a sequence of numbers.
*   Using the loop variable (`age`) within the loop.
*   Putting `if` statements inside a loop to perform actions conditionally for each item.
*   Using comparison operators (`<`, `<=`, `>`, `>=`).
*   Using the logical operator `and` to combine multiple conditions in an `if` statement.

Well done!
---