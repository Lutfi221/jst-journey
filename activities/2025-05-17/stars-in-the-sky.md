# Python Homework: Turtle Graphics - Stars in the Sky

Follow the steps below. For each step:
1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

---

## Initial Setup

For all steps in this homework, you'll start with the following basic Python code. Make sure you have this at the beginning of your Python file. You'll add your drawing code for each step where indicated.

```python
import turtle
import random # You'll need this for a later step!

s = turtle.Screen()
t = turtle.Turtle()

# Set up the drawing environment
s.bgcolor("black")    # Make the screen background black
t.color("yellow")     # Set the turtle's pen and fill color to yellow
t.speed(10)           # Set turtle speed (0 is fastest, 10 is fast)

# Your drawing code for each step will go here

turtle.done() # Keeps the turtle window open until you close it
```
Remember to place the code for each step *before* the `turtle.done()` line.

---

## Step 1: Drawing a Single Star

### Problem

Your first task is to make the turtle draw a single, five-pointed star. The screen background should already be black, and the star's outline should be yellow (as per the initial setup). Do not fill the star with color yet.

Your turtle should start at its default position and orientation.

### Hint

<details>
  <summary>Stuck on Step 1? Click for a hint!</summary>

  *   To draw a star, you'll need a `for` loop that repeats 5 times (for the 5 points of the star).
  *   Inside the loop, the turtle needs to move forward to draw a line, and then turn.
  *   The command `t.forward(amount)` will draw a side of the star. You can choose a `star_size` for this (e.g., `50`).
  *   The command `t.right(angle)` will turn the turtle. The angle for a 5-pointed star is 144 degrees.
  *   Ensure `s.bgcolor("black")` and `t.color("yellow")` are set from the initial setup.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("black") # Matches turtle.bgcolor("black") from snippet
t.color("yellow")
t.speed(10)

star_size = 50

for i in range(5):
    t.forward(star_size)
    t.right(144)

turtle.done()
```

**Explanation:**
*   `import turtle` and `import random` load the necessary libraries.
*   `s = turtle.Screen()` and `t = turtle.Turtle()` set up our drawing window and turtle.
*   `s.bgcolor("black")` sets the background color.
*   `t.color("yellow")` sets the turtle's drawing color.
*   `t.speed(10)` sets the drawing speed.
*   `star_size = 50` defines how long each segment of the star will be.
*   The `for i in range(5):` loop runs five times.
*   `t.forward(star_size)` moves the turtle forward, drawing one of the star's lines.
*   `t.right(144)` turns the turtle 144 degrees to the right. Repeating this sequence five times creates a five-pointed star.
*   `turtle.done()` keeps the window open.

</details>

---

## Step 2: Filling the Star

### Problem

Modify your code from Step 1. Now, in addition to drawing the star, fill its "limbs" (the inside of the star) with yellow color.

### Hint

<details>
  <summary>Stuck on Step 2? Click for a hint!</summary>

  *   The `turtle` library provides commands to control filling shapes.
  *   You need to tell the turtle when to `t.begin_fill()` before you start drawing the shape you want to fill.
  *   After you have finished drawing all the lines of the star (i.e., after your loop completes), you tell the turtle to `t.end_fill()`.
  *   The `t.color("yellow")` command from the initial setup should already handle setting the fill color to yellow.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("black")
t.color("yellow") # Sets both pen and fill color to yellow
t.speed(10)

star_size = 50

t.begin_fill() # Start filling before drawing the star
for i in range(5):
    t.forward(star_size)
    t.right(144)
t.end_fill()   # End filling after the star is drawn

turtle.done()
```

**Explanation:**
*   The code is very similar to Step 1.
*   `t.begin_fill()`: This command is placed *before* the loop that draws the star. It tells the turtle to start recording the path for a filled shape.
*   The `for` loop draws the star as before.
*   `t.end_fill()`: This command is placed *after* the loop. It tells the turtle to complete the fill operation, coloring the area enclosed by the path drawn since `t.begin_fill()`. Since `t.color("yellow")` was used, the fill color is yellow.

</details>

---

## Step 3: Drawing Three Stars in a Row

### Problem

Modify your code from Step 2. Instead of one star, draw three identical filled yellow stars in a horizontal row. After drawing each star, you'll need to move the turtle to a new position to draw the next star, without leaving a trail during the move.

### Hint

<details>
  <summary>Stuck on Step 3? Click for a hint!</summary>

  *   You'll need an outer `for` loop that runs 3 times (once for each star).
  *   Inside this outer loop, you'll include the code to draw a single filled star (the `t.begin_fill()`, the inner loop for star points, and `t.end_fill()`).
  *   To move the turtle without drawing a line, use `t.penup()`.
  *   After lifting the pen, move the turtle to the starting position for the next star (e.g., `t.forward(some_distance)`).
  *   Then, use `t.pendown()` before you start drawing the next star.
  

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("black")
t.color("yellow")
t.speed(10)

star_size = 50

# Outer loop for drawing three stars
for i in range(3):
    # Draw one filled star
    t.begin_fill()
    for j in range(5): # Inner loop for the 5 points of a star
        t.forward(star_size)
        t.right(144)
    t.end_fill()

    # Move to the next star's position
    t.penup()
    t.forward(100) # Move forward to create space
    t.pendown()

turtle.done()
```

**Explanation:**
*   We introduce an outer loop: `for i in range(3):`. This loop will execute its contents three times.
*   Inside this outer loop, the code for drawing one filled star (from Step 2) is placed.
*   `t.begin_fill()` and `t.end_fill()` are inside the outer loop, so each star is individually filled.
*   After a star is drawn and filled, `t.penup()` lifts the pen.
*   `t.forward(100)` moves the turtle to the right by `100` units.
*   `t.pendown()` puts the pen back down, ready to draw the next star. This movement occurs after every star, including the last one.

</details>

---

## Step 4: Drawing Five Randomly Placed Stars

### Problem

Now, let's make things more dynamic! Modify your code to draw **five** filled yellow stars. Each star should appear at a somewhat random position on the screen. The stars should still be yellow on a black background.

### Hint

<details>
  <summary>Stuck on Step 4? Click for a hint!</summary>

  *   You'll need the `random` module. Make sure `import random` is at the top of your script.
  *   The function `random.randint(a, b)` returns a random integer between `a` and `b` (inclusive).
  *   Your outer loop should run 5 times for five stars.
  *   After drawing each star (and using `t.end_fill()`), you need to:
      1.  Lift the pen: `t.penup()`.
      2.  Generate random `dx` (change in x) and `dy` (change in y) values (e.g., `random.randint(-100, 100)`).
      3.  Move the turtle using these relative changes: `t.forward(dx)`, `t.left(90)`, `t.forward(dy)`, and then `t.right(90)` to restore the turtle's orientation for drawing the next star.
      4.  Put the pen down: `t.pendown()`.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("black")
t.color("yellow")
t.speed(10)

# Initial positioning, as in the snippet
t.penup()
t.backward(200)
t.pendown()

star_size = 50

# Loop to draw five stars (as per problem description)
for i in range(5):
    # Draw one filled star
    t.begin_fill()
    for j in range(5): # Inner loop for the 5 points of a star
        t.forward(star_size)
        t.right(144)
    t.end_fill()

    # Prepare to move to a new random position for the next star
    t.penup()

    # Generate random changes in x and y direction
    dx = random.randint(-100, 100)
    dy = random.randint(-100, 100)

    # Move turtle by dx, then dy (relative to current position and orientation)
    # This sequence aims to move randomly while keeping star orientation consistent
    t.forward(dx)
    t.left(90)
    t.forward(dy)
    t.right(90) # Restores original orientation

    t.pendown() # Pen down ready for the next star

turtle.done()
```

**Explanation:**
*   The outer loop `for i in range(5):` runs five times to draw five stars, as requested by the problem.
*   The `t.penup(); t.backward(200); t.pendown();` lines before the loop provide an initial positioning.
*   Inside the loop, after a star is drawn and filled:
    *   `t.penup()` lifts the pen.
    *   `dx = random.randint(-100, 100)` and `dy = random.randint(-100, 100)` generate random values for movement.
    *   The sequence `t.forward(dx)`, `t.left(90)`, `t.forward(dy)`, `t.right(90)` moves the turtle relatively. The `t.right(90)` is important to reset the turtle's orientation so the next star is drawn upright.
    *   `t.pendown()` puts the pen down, ready for the next star.

</details>

---

## You Finished!

You've practiced:
*   Importing and using the `turtle` module for graphics.
*   Setting up the `Screen` and `Turtle` objects.
*   Controlling screen properties like `bgcolor`.
*   Controlling turtle properties like `color` (for pen and fill) and `speed`.
*   Drawing shapes using `t.forward()` and `t.right()`.
*   Using `for` loops to repeat drawing commands and create shapes like stars.
*   Using nested `for` loops.
*   Filling shapes with color using `t.begin_fill()` and `t.end_fill()`.
*   Moving the turtle without drawing using `t.penup()` and `t.pendown()`.
*   Importing and using the `random` module, specifically `random.randint()`, to add unpredictability.
*   Using random numbers to determine relative movements for drawn elements.
*   Keeping the turtle graphics window open using `turtle.done()`.
