# Python Homework: Turtle Graphics - Drawing a Chessboard

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

s = turtle.Screen()
t = turtle.Turtle()

turtle.tracer(0, 0) # Turns off screen updates for instant drawing

# Initial turtle settings
t.speed(0) # Set turtle speed to fastest (0 is fastest)
t.penup()
# Set a starting position, for example, towards the bottom-left
# An 8x8 board with 60px squares will be 480x480.
# (-300, -300) is a point from where we can draw towards top-right.
t.goto(-300, -300)
t.pendown()

# Define constants for the board
square_size = 60
board_size = 8 # We'll be making an 8x8 board

# Your drawing code for each step will go here

turtle.done() # Keeps the turtle window open until you close it
```
Remember to place the code for each step *before* the `turtle.done()` line. The `turtle.tracer(0,0)` command means the drawing will appear instantly once all commands are processed.

---

## Step 1: Drawing a Row of Black Squares

### Problem

Your first task is to make the turtle draw a single horizontal row of 8 black, filled squares. Each square should be `square_size` in dimension. After drawing each square, the turtle should move to the starting position of the next square in the row.

### Hint

<details>
  <summary>Stuck on Step 1? Click for a hint!</summary>

  *   You'll need a `for` loop that repeats `board_size` (which is 8) times.
  *   Inside the loop, you need to draw one filled square:
      *   Start filling using `t.begin_fill()`.
      *   Draw the four sides of the square: `t.forward(square_size)` and `t.left(90)` repeated 4 times (perhaps using another loop).
      *   End filling using `t.end_fill()`.
  *   After drawing and filling one square, you need to move the turtle to the start of the next square in the same row. This means moving `t.forward(square_size)` *without* turning.
  *   Ensure the fill color is black. You can set this once using `t.fillcolor("black")` before the loop, or ensure the default is black.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```python
import turtle

s = turtle.Screen()
t = turtle.Turtle()

turtle.tracer(0, 0)

t.speed(0)
t.penup()
t.goto(-300, -300)
t.pendown()

square_size = 60
board_size = 8

# Set fill color to black for all squares in this step
t.fillcolor("black")

for i in range(board_size):
    # Draw one filled square
    t.begin_fill()
    for k in range(4): # A square has 4 sides
        t.forward(square_size)
        t.left(90)
    t.end_fill()

    # Move to the start of the next square in the row
    t.forward(square_size)

turtle.done()
```

**Explanation:**
*   The initial setup prepares the turtle.
*   `t.fillcolor("black")` sets the fill color for the squares.
*   The outer `for i in range(board_size):` loop iterates 8 times, once for each square in the row.
*   Inside this loop:
    *   `t.begin_fill()` starts the fill process.
    *   The inner `for k in range(4):` loop draws the 4 sides of a square.
    *   `t.end_fill()` completes the fill for the current square.
    *   `t.forward(square_size)` moves the turtle to the right, ready to draw the next square adjacent to the current one.

</details>

---

## Step 2: Alternating Colors in a Row

### Problem

Modify your code from Step 1. Instead of all black squares, make the squares in the row alternate colors: the first black, the second white, the third black, and so on, for all 8 squares in the row.

### Hint

<details>
  <summary>Stuck on Step 2? Click for a hint!</summary>

  *   Inside your main loop (that iterates `board_size` times), you need to decide the `t.fillcolor()` *before* `t.begin_fill()`.
  *   Use an `if/else` statement to choose between `'black'` and `'white'`.
  *   The loop variable (e.g., `i`) can help you decide. The modulo operator (`%`) is useful here. `i % 2 == 0` is true if `i` is even (0, 2, 4...).
  *   If `i` is even, set one color; if `i` is odd, set the other color.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```python
import turtle

s = turtle.Screen()
t = turtle.Turtle()

turtle.tracer(0, 0)

t.speed(0)
t.penup()
t.goto(-300, -300)
t.pendown()

square_size = 60
board_size = 8

for i in range(board_size):
    # Determine fill color based on loop index 'i'
    if i % 2 == 0: # Even index (0, 2, 4...)
        t.fillcolor('black')
    else: # Odd index (1, 3, 5...)
        t.fillcolor('white')

    # Draw one filled square
    t.begin_fill()
    for k in range(4):
        t.forward(square_size)
        t.left(90)
    t.end_fill()

    # Move to the start of the next square
    t.forward(square_size)

turtle.done()
```

**Explanation:**
*   The key change is inside the loop for the row.
*   `if i % 2 == 0:` checks if the current square's index `i` is even.
    *   If it's even (0, 2, ...), `t.fillcolor('black')` is set.
    *   Else (if `i` is odd), `t.fillcolor('white')` is set.
*   The rest of the square drawing logic and movement remains the same. This creates a row with alternating black and white squares.

</details>

---

## Step 3: Drawing the Full Grid (Basic Chessboard Structure)

### Problem

Now, expand your single row of alternating colored squares into a full 8x8 grid. You'll need to draw 8 rows, and each row should be like the one you created in Step 2.
After drawing each row, the turtle needs to move to the beginning of the next row, which will be positioned directly above the row just completed.

For this step, the coloring might not be a perfect chessboard yet (e.g., all rows might start with black). We'll fix the precise chessboard pattern in the next step.

### Hint

<details>
  <summary>Stuck on Step 3? Click for a hint!</summary>

  *   You'll need *nested* `for` loops. An outer loop for the rows (iterating `board_size` times) and an inner loop for the squares within each row (also iterating `board_size` times).
  *   The inner loop will contain the logic from Step 2 for drawing one row with alternating colors. Let the outer loop variable be `i` (for rows) and the inner loop variable be `j` (for columns/squares in a row).
  *   The color alternation logic from Step 2 (`if j % 2 == 0: ... else: ...`) should now use the *inner loop variable* (`j`) to alternate colors within a row.
  *   **Crucially**, after the inner loop finishes (i.e., one row is drawn), you must:
      1.  Lift the pen: `t.penup()`.
      2.  Move the turtle back to the horizontal starting position of the row. This means moving backward by `square_size * board_size`.
      3.  Move the turtle up to the starting vertical position of the next row. A common way is: `t.left(90)`, `t.forward(square_size)`, `t.right(90)`. This sequence moves the turtle "up" by `square_size` while keeping its heading to the right.
      4.  Put the pen down: `t.pendown()`.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```python
import turtle

s = turtle.Screen()
t = turtle.Turtle()

turtle.tracer(0, 0)

t.speed(0)
t.penup()
t.goto(-300, -300)
t.pendown()

square_size = 60
board_size = 8

# Outer loop for rows
for i in range(board_size):
    # Inner loop for squares in a row (columns)
    for j in range(board_size):
        # Color determination based on column index 'j' for this step
        if j % 2 == 0:
            t.fillcolor('black')
        else:
            t.fillcolor('white')

        t.begin_fill()
        for k in range(4): # Draw one square
            t.forward(square_size)
            t.left(90)
        t.end_fill()

        t.forward(square_size) # Move to next square position in the row

    # After finishing a row, move to the start of the next row
    t.penup()
    t.backward(square_size * board_size) # Go back to the row's starting X
    t.left(90)                           # Turn to face upwards
    t.forward(square_size)               # Move up by one square_size
    t.right(90)                          # Turn back to face right
    t.pendown()

turtle.done()
```

**Explanation:**
*   An outer loop `for i in range(board_size):` controls the rows.
*   An inner loop `for j in range(board_size):` controls the columns (squares within each row).
*   The color logic `if j % 2 == 0:` makes each row alternate starting with black (as `j` resets for each row).
*   The critical part is after the inner loop completes:
    *   `t.penup()`
    *   `t.backward(square_size * board_size)`: Moves the turtle to the left edge of the board for the current row.
    *   `t.left(90)`, `t.forward(square_size)`, `t.right(90)`: This sequence moves the turtle up by one square's height to begin the next row, while maintaining its orientation to draw squares to the right.
    *   `t.pendown()`

</details>

---

## Step 4: Achieving True Chessboard Colors

### Problem

Modify your code from Step 3 to create the correct alternating color pattern for a chessboard. On a chessboard, if a square at `(row, col)` is black, then its neighbors `(row+1, col)` and `(row, col+1)` are white.

The color of a square now depends on both its row index (`i`) and its column index (`j`).

### Hint

<details>
  <summary>Stuck on Step 4? Click for a hint!</summary>

  *   The `if/else` condition for `t.fillcolor()` needs to consider both the row index (`i` from the outer loop) and the column index (`j` from the inner loop).
  *   One common way: If the sum of the row and column indices (`i + j`) is even, the square is one color (e.g., black). If the sum is odd, it's the other color (e.g., white). So, check `(i + j) % 2 == 0`.
  *   Alternatively, a more explicit condition: A square is one color if (`i` is even AND `j` is even) OR (`i` is odd AND `j` is odd). Otherwise, it's the other color. This can be written as: `(i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)`.

</details>

### Solution

<details>
  <summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```python
import turtle

s = turtle.Screen()
t = turtle.Turtle()

turtle.tracer(0, 0)

t.speed(0)
t.penup()
t.goto(-300, -300)
t.pendown()

square_size = 60
board_size = 8

# Outer loop for rows
for i in range(board_size):
    # Inner loop for squares in a row (columns)
    for j in range(board_size):
        # Determine color based on both row (i) and column (j)
        # If (i is even AND j is even) OR (i is odd AND j is odd), color it black
        # This is one way to get the chessboard pattern.
        if (i % 2 == 0 and j % 2 == 0) or \
           (i % 2 != 0 and j % 2 != 0):
            t.fillcolor('black')
        else:
            t.fillcolor('white')
        
        # Alternative (often simpler) condition:
        # if (i + j) % 2 == 0:
        #    t.fillcolor('black')
        # else:
        #    t.fillcolor('white')

        t.begin_fill()
        for k in range(4): # Draw one square
            t.forward(square_size)
            t.left(90)
        t.end_fill()

        t.forward(square_size) # Move to next square position in the row

    # After finishing a row, move to the start of the next row
    t.penup()
    t.backward(square_size * board_size)
    t.left(90)
    t.forward(square_size)
    t.right(90)
    t.pendown()

turtle.done()
```

**Alternative (more compact) Solution for color logic:**
The solution above includes a common way to determine chessboard colors. A more mathematically concise way is to check the parity of the sum of the indices:

```python
# Inside the nested loops (replace the if/else block for fillcolor):
if (i + j) % 2 == 0:
    t.fillcolor('black') # Or your desired starting color for (0,0)
else:
    t.fillcolor('white')
```
If your (0,0) square (bottom-left if you draw bottom-up) needs to be white, you might swap the colors or use `(i + j) % 2 != 0` for black.

**Explanation:**
*   The main structure is the same as Step 3.
*   The crucial change is the condition for `t.fillcolor()`. It now uses both `i` (row index) and `j` (column index).
*   The condition `(i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)` means:
    *   If both `i` and `j` are even, the square is black.
    *   If both `i` and `j` are odd, the square is black.
    *   Otherwise (one is even and one is odd), the square is white.
    This creates the classic chessboard pattern.
*   The alternative `if (i + j) % 2 == 0:` condition is simpler and achieves the same result. If the sum of indices is even, it's one color; if odd, it's the other. This naturally creates the alternating pattern across rows and columns.

</details>

---

## You Finished!

Congratulations on drawing a chessboard! You've practiced:
*   Importing and using the `turtle` module.
*   Setting up the `Screen` and `Turtle` objects.
*   Using `turtle.tracer(0,0)` for instant drawing.
*   Moving the turtle with `t.penup()`, `t.pendown()`, `t.goto()`, `t.forward()`, `t.backward()`, and `t.left()`/`t.right()`.
*   Drawing filled shapes using `t.begin_fill()`, `t.end_fill()`, and `t.fillcolor()`.
*   Using `for` loops to repeat actions.
*   Using **nested `for` loops** to create grid-like structures.
*   Using `if/else` statements for conditional logic (choosing colors).
*   Using the **modulo operator (`%`)** to determine even/odd numbers for alternating patterns.
*   Combining row and column indices to create complex patterns like a chessboard.
*   Resetting the turtle's position to draw successive rows in a grid.
*   Keeping the turtle graphics window open using `turtle.done()`.
