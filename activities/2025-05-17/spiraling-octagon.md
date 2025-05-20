# Python Homework: Turtle Graphics and Loops

Follow the steps below. For each step:
1.  **Read the problem carefully.**
2.  **Try to write the Python code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by running it!**

---

## Initial Setup

For all steps in this homework, you'll start with the following basic Python code that uses the `turtle` library. Make sure you have this at the beginning of your Python file.

```python
import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) # Set turtle speed (0 is fastest, 10 is fast, 1 is slowest)
# Your drawing code will go here for each step

turtle.done() # Keeps the turtle window open until you close it
```
Remember to place the code for each step *before* the `turtle.done()` line.

---

## Step 1: Drawing a Repeated Square Path

### Problem

Your first task is to make the turtle draw a square. After drawing the first square, the turtle should continue and draw the same square path a total of 10 times. The turtle will trace over its own path.

Your turtle should start at its default position and orientation.

### Hint

<details>
  <summary>Stuck on Step 1? Click for a hint!</summary>

  *   To draw a single square, you need to move forward and turn left (or right) four times. What angle do you use for a square?
  *   To repeat this action 10 times, you'll need a `for` loop. The `range()` function will be helpful here.
  *   The commands `t.forward(amount)` and `t.left(angle)` will be essential. You can pick any reasonable `amount` for the side length of the square (e.g., 100).

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
import turtle
import math

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10)

# Loop 10 times for the 10 squares
for _ in range(10): # We use _ because we don't need the loop variable's value itself
    # Draw one square
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    # After drawing one square, the turtle is back at the start, ready for the next iteration

turtle.done()
```

**Alternative (more compact) Solution for drawing one square inside the loop:**
```python
import turtle
import math

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10)

# Loop 10 times for the 10 squares
for _ in range(10):
    # Draw one square using an inner loop
    for _ in range(4): # A square has 4 sides
        t.forward(100)
        t.left(90)

turtle.done()
```

**Explanation:**
*   `import turtle` loads the turtle graphics library.
*   `s = turtle.Screen()` creates the drawing window.
*   `t = turtle.Turtle()` creates our turtle object.
*   `t.speed(10)` sets the drawing speed.
*   The outer `for _ in range(10):` loop makes the turtle repeat the drawing process 10 times.
*   Inside this loop (in the more compact solution), another `for _ in range(4):` loop draws the four sides of a square.
*   `t.forward(100)` moves the turtle forward by 100 units.
*   `t.left(90)` turns the turtle left by 90 degrees.
*   `turtle.done()` keeps the window open.

</details>

---

## Step 2: Spiraling Out

### Problem

Modify your code from Step 1. Instead of drawing the same square 10 times in the same place, make the turtle draw a square spiral that grows outwards. Each side of the "square" in the spiral should get longer.

Start with a small side length for the first segment and increase it with each segment the turtle draws. You'll still be making 90-degree turns. Loop a chosen number of times (e.g., 40 times, which would be 10 "squares" if each square has 4 sides, or simply 40 segments).

The output should look like an expanding square spiral.

### Hint

<details>
  <summary>Stuck on Step 2? Click for a hint!</summary>

  *   You'll still use a `for` loop. Let the loop variable (e.g., `i`) increase with each iteration.
  *   The `t.forward()` command will need to use a distance that changes. How can you use the loop variable `i` to make the forward distance increase?
  *   Multiplying the loop variable by a small constant (e.g., `10 * i`) can be a good way to increase the distance for `t.forward()`.
  *   You'll still use `t.left(90)` for the turns.
  *   Think about how many turns/segments you want to draw in total. If you loop, say, 40 times, and each time you move forward and turn, you'll get 40 segments.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
import turtle
import math

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10)

# We'll draw many segments to make a visible spiral
# Each iteration draws one side of the expanding "square"
for i in range(40): # For example, 40 segments
    # Make the forward distance increase with each step
    # Start with a small step and multiply by i
    t.forward(5 * i) # You can adjust the '5' to change how fast it spirals
    t.left(90)       # A 90-degree turn for a square-like spiral

turtle.done()
```

**Explanation:**
*   The setup is the same.
*   `for i in range(40):` loops 40 times. The variable `i` will go from 0 to 39.
*   `t.forward(5 * i)`: This is the key change.
    *   In the first iteration (`i=0`), `t.forward(0)` (turtle doesn't move).
    *   In the second iteration (`i=1`), `t.forward(5)`.
    *   In the third iteration (`i=2`), `t.forward(10)`, and so on.
    *   This makes each segment the turtle draws longer than the last, causing it to spiral outwards.
*   `t.left(90)` keeps the turns at 90 degrees, maintaining the square-like nature of the spiral.

</details>

---

## Step 3: Making it Jagged (Spiraling with Angle Change)

### Problem

Now, modify your spiraling code from Step 2. Keep the outward spiraling movement (increasing forward distance). However, slightly change the angle of the turn in each step. This will make the spiral look more "jagged" or organic, rather than a perfect square spiral.

Instead of always turning 90 degrees, make the turn angle change slightly with each iteration.

### Hint

<details>
  <summary>Stuck on Step 3? Click for a hint!</summary>

  *   You'll still have your `for` loop and the `t.forward(something * i)` line.
  *   The `t.left()` command is where the change happens.
  *   Instead of `t.left(90)`, try `t.left(90 + some_small_change)`.
  *   This `some_small_change` can also depend on your loop variable `i`. For example, you could add `i / 25` to 90. This means the angle change itself changes slightly with each step.
  *   Experiment with the amount you add or subtract from the base angle.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
import turtle
import math

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) # Set to 0 for fastest if desired, or 10 for fast

# Loop a sufficient number of times to see the pattern
for i in range(100): # Increased iterations to see the effect better
    t.forward(10 * i)   # Increasing forward distance
    t.left(90 + i / 25) # Base 90-degree turn, plus a small increasing change

turtle.done()
```

**Explanation:**
*   The `for i in range(100):` loop runs more times to make the pattern more prominent.
*   `t.forward(10 * i)` continues the outward spiral, possibly with a larger step multiplier.
*   `t.left(90 + i / 25)`:
    *   The base turn is still 90 degrees.
    *   `i / 25` is a small value that increases as `i` increases.
    *   So, the first few turns will be slightly more than 90 degrees (e.g., `90 + 0/25 = 90`, `90 + 1/25 = 90.04`, `90 + 2/25 = 90.08`, etc.).
    *   This slight, cumulative change in the turn angle causes the spiral to deviate from a perfect square shape, creating a "jagged" or curved effect over time.

</details>

---

## Step 4: Drawing a Spiraling Octagon Shape

### Problem

Modify your code from Step 3. Instead of a jagged square-like spiral, try to make the turtle draw a shape that resembles an octagon (8 sides) while still spiraling outwards and having a slightly changing angle.

The main difference between a square and an octagon is the angle of the turns.

### Hint

<details>
  <summary>Stuck on Step 4? Click for a hint!</summary>

  *   An octagon has 8 equal sides and 8 equal angles. The exterior angle of a regular polygon is `360 / number_of_sides`. For an octagon, what would this angle be?
  *   You only need to change one primary number in your `t.left()` command from the previous step to get the basic octagon turn.
  *   You can keep the `+ i / 25` part if you want the spiraling octagon to also have that slightly "organic" or jagged feel as it expands.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
import turtle
import math

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) # Or t.speed(0) for fastest

# Loop many times to see the octagonal spiral
for i in range(100): # Or more, e.g., 150-200, for a larger pattern
    t.forward(5 * i)     # Spiraling outwards, adjust '5' for spiral tightness
    t.left(45 + i / 25)  # Base turn for an octagon is 360/8 = 45 degrees

turtle.done()
```

**Explanation:**
*   The core logic of spiraling outwards (`t.forward(5 * i)`) and having a slightly varying angle (`+ i / 25`) remains similar.
*   The key change is `t.left(45 + i / 25)`:
    *   A regular octagon has 8 sides. To turn from one side to the next, the turtle needs to turn by an exterior angle of `360 / 8 = 45` degrees.
    *   So, the base turn angle is now `45` degrees.
    *   The `+ i / 25` part still adds a small, cumulative change to this base angle, making the octagonal spiral also look a bit "organic" or less rigidly geometric as it expands. If you wanted a more perfect octagonal spiral, you might omit the `+ i / 25` or make it much smaller.

</details>

---

## You Finished!

You've practiced:
*   Importing and using the `turtle` module for graphics.
*   Setting up the `Screen` and `Turtle` objects.
*   Controlling the turtle's speed using `t.speed()`.
*   Moving the turtle with `t.forward()` and turning it with `t.left()`.
*   Using `for` loops with `range()` to repeat drawing commands and create patterns.
*   Using the loop variable within the loop to dynamically change drawing parameters like distance (`t.forward(value * i)`).
*   Modifying turn angles within a loop to change the shape of paths and spirals (`t.left(base_angle + i / factor)`).
*   Understanding how changing the base turn angle affects the fundamental shape being drawn (e.g., 90 degrees for squares, 45 degrees for octagons).
*   Keeping the turtle graphics window open using `turtle.done()`.
---