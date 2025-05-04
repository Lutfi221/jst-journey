Read this cheat sheet after you've done all the homework so it doesn't spoil the fun.

---

# Python Homework Cheat Sheet: Loops & Conditionals

This sheet summarizes useful Python concepts covered in the homework exercises.

- [Python Homework Cheat Sheet: Loops \& Conditionals](#python-homework-cheat-sheet-loops--conditionals)
  - [1. `for` Loops with `range()`](#1-for-loops-with-range)
  - [2. Using the Loop Variable](#2-using-the-loop-variable)
  - [3. `if` Statements inside Loops](#3-if-statements-inside-loops)
  - [4. Comparison Operators](#4-comparison-operators)
  - [5. Logical Operator (`and`)](#5-logical-operator-and)
  - [6. Getting User Input (`input()`)](#6-getting-user-input-input)
  - [7. Type Conversion (`int()`, `str()`)](#7-type-conversion-int-str)
  - [8. Performing Calculations](#8-performing-calculations)


---

## 1. `for` Loops with `range()`

**Explanation:** The `for` loop is used to iterate over a sequence. `range()` generates a sequence of numbers, often used to repeat an action a specific number of times.
*   `range(stop)`: Generates numbers from 0 up to (but not including) `stop`.
*   `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`.

**Code Example:**

```python
# Loop from 0 to 4
for i in range(5):
    print(i)

# Loop from 1 to 10
for num in range(1, 11):
    print(num)
```

**Output:**

```
0
1
2
3
4
1
2
3
4
5
6
7
8
9
10
```

---

## 2. Using the Loop Variable

**Explanation:** Inside a `for` loop, the variable you define (like `i` or `num`) holds the current item from the sequence being iterated over. You can use this variable in calculations, print statements, or conditions.

**Code Example:**

```python
# Print age categories using the 'age' variable
for age in range(1, 6): # Ages 1 through 5
    if age <= 3:
        print(str(age) + " toddler")
    else:
        print(str(age) + " child")
```

**Output:**

```
1 toddler
2 toddler
3 toddler
4 child
5 child
```

---

## 3. `if` Statements inside Loops

**Explanation:** Placing `if` statements inside a loop allows you to perform actions conditionally for *each* item or iteration. You decide whether to execute certain code based on the current value of the loop variable or other conditions.

**Code Example:**

```python
# Print numbers, but skip 4
for num in range(1, 6): # Numbers 1 through 5
    if num != 4:
        print("Current number: " + str(num))
    else:
        print("Skipped number: " + str(num)) # Or just 'print("unlucky")'
```

**Output:**

```
Current number: 1
Current number: 2
Current number: 3
Skipped number: 4
Current number: 5
```

---

## 4. Comparison Operators

**Explanation:** Used in `if` (or `elif`/`else`) conditions to compare values.

**Common Operators:**
*   `<` (less than)
*   `<=` (less than or equal to)
*   `>` (greater than)
*   `>=` (greater than or equal to)
*   `==` (equal to)
*   `!=` (not equal to)

**Code Example:**

```python
my_age = 20

if my_age >= 18:
    print("You are an adult.")
if my_age != 21:
    print("You are not 21.")
```

**Output:**

```
You are an adult.
You are not 21.
```

---

## 5. Logical Operator (`and`)

**Explanation:** Used to combine multiple conditions. The condition joined by `and` is only true if *both* individual conditions are true.

**Code Example:**

```python
score = 75

# Check if score is between 70 and 80 (inclusive)
if score >= 70 and score <= 80:
    print("Score is in the 70s.")
```

**Output:**

```
Score is in the 70s.
```

---

## 6. Getting User Input (`input()`)

**Explanation:** The `input()` function pauses the program and waits for the user to type something and press Enter. It *always* returns the user's input as a string.

**Code Example:**

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

**Output (Example Interaction):**

```
Enter your name: Alice
Hello, Alice!
```

---

## 7. Type Conversion (`int()`, `str()`)

**Explanation:** Often you need to convert data from one type to another. `int()` converts a string (or other compatible type) to an integer. `str()` converts a number (or other type) to a string so you can concatenate it with other strings.

**Code Example:**

```python
# Get user input and convert to integer for math
user_num_str = input("Enter a number: ")
user_num_int = int(user_num_str)

# Use the integer in a calculation
result = user_num_int * 2

# Convert numbers back to string for printing
print("Twice your number is: " + str(result))
```

**Output (Example Interaction):**

```
Enter a number: 15
Twice your number is: 30
```

---

## 8. Performing Calculations

**Explanation:** Standard arithmetic operations (`+`, `-`, `*`, `/`, etc.) can be performed directly on numbers (integers or floats). Results can be stored in variables and used later.

**Code Example:**

```python
fixed_num = 7
for multiplier in range(1, 4): # Loop 1, 2, 3
    product = fixed_num * multiplier
    print(str(fixed_num) + " * " + str(multiplier) + " = " + str(product))
```

**Output:**

```
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
```

---