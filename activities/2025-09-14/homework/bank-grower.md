Of course. Here is the homework markdown document based on the materials and structure provided.

# HTML/JS Homework: Building a Balance List with Loops

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the HTML and JavaScript code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by opening the HTML file in a web browser!**

-----

## Final Goal

When you're finished, you will have built a web page that uses a JavaScript `for` loop to dynamically generate a list of bank balances. The list will count down by hundreds, and certain values will be conditionally hidden. The final page will look like this:

  - $ 1000
  - $ 900
  - $ 800
  - hidden
  - hidden
  - hidden
  - $ 400
  - $ 300
  - $ 200
  - $ 100

-----

## Initial Setup

Start with the following basic HTML structure. This creates a title and an empty list that you will populate with JavaScript. Save this in a file named `balances.html`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Grow numbers</title>
  </head>
  <body>
    <ul id="balance-list"></ul>
    <script>
      // Your code will go here
    </script>
  </body>
</html>
```

-----

## Step 1: A Simple Loop

### Problem

Your first task is to create a basic `for` loop that generates a list of numbers from 0 up to (but not including) 10.

Your script should:

1.  Get a reference to the `<ul>` element with the ID `balance-list`.
2.  Write a `for` loop that iterates from 0 to 9.
3.  Inside the loop, add a new list item `<li>` to the `<ul>` for each number. The output for each item should look like `$ 0`, `$ 1`, etc.

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  - To get the list element, use `let balanceListElem = document.getElementById("balance-list");`.
  - A `for` loop has three parts: initialization, condition, and increment. The structure looks like `for (let i = 0; i < 10; i++) { ... }`.
  - To add items to the list, you can use `balanceListElem.innerHTML += '<li> $ ' + i + '</li>';`. The `+=` operator appends the new string to the existing content.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Grow numbers</title>
  </head>
  <body>
    <ul id="balance-list"></ul>
    <script>
      let balanceListElem = document.getElementById("balance-list");
      for (let i = 0; i < 10; i++) {
        balanceListElem.innerHTML += "<li> $ " + i + "</li>";
      }
    </script>
  </body>
</html>
```

</details>

-----

## Step 2: Make it to a Thousand

### Problem

A list of 10 isn't very impressive. Modify your loop from Step 1 so that it counts all the way up to (but not including) 1000.

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  - You only need to change one part of your `for` loop.
  - The middle part of the loop declaration (`i < 10`) controls when the loop stops. What should you change `10` to?

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Grow numbers</title>
  </head>
  <body>
    <ul id="balance-list"></ul>
    <script>
      let balanceListElem = document.getElementById("balance-list");
      for (let i = 0; i < 1000; i++) {
        balanceListElem.innerHTML += "<li> $ " + i + "</li>";
      }
    </script>
  </body>
</html>
```

</details>

-----

## Step 3: Increase by Hundreds

### Problem

Listing every number to 1000 is too long! Let's change the loop to show balances in increments of 100 (0, 100, 200, etc.).

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  - The third part of the `for` loop declaration controls how the counter variable `i` changes after each iteration.
  - Instead of `i++` (which adds 1), you can use `i += 100` to add 100.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Grow numbers</title>
  </head>
  <body>
    <ul id="balance-list"></ul>
    <script>
      let balanceListElem = document.getElementById("balance-list");
      for (let i = 0; i < 1000; i += 100) {
        balanceListElem.innerHTML += "<li> $ " + i + "</li>";
      }
    </script>
  </body>
</html>
```

</details>

-----

## Step 4: Count Down from Big to Small

### Problem

Let's reverse the order. Modify the loop so that it counts down from 1000 to 100, in steps of 100. The list should show `$ 1000`, `$ 900`, and so on.

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  - A countdown loop has a different structure.
  - **Initialization:** Start `i` at `1000`.
  - **Condition:** The loop should continue as long as `i` is greater than `0` (`i > 0`).
  - **Increment/Decrement:** You need to subtract 100 in each step (`i -= 100`).

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Grow numbers</title>
  </head>
  <body>
    <ul id="balance-list"></ul>
    <script>
      let balanceListElem = document.getElementById("balance-list");
      for (let i = 1000; i > 0; i -= 100) {
        balanceListElem.innerHTML += "<li> $ " + i + "</li>";
      }
    </script>
  </body>
</html>
```

</details>

-----

## Step 5: Hide Certain Numbers

### Problem

Now, let's add some logic inside the loop. If a balance is between $300 and $600 (inclusive), display the word "hidden" instead of the amount.

### Hint

<details>
<summary>Stuck on Step 5? Click for a hint!</summary>

  - Inside your `for` loop, you'll need an `if/else` statement.
  - The `if` condition needs to check two things at once. You can do this with the `&&` (AND) operator.
  - Your condition will look like `if (i >= 300 && i <= 600)`.
  - If the condition is true, add the "hidden" list item. In the `else` block, add the normal balance list item.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 5? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Grow numbers</title>
  </head>
  <body>
    <ul id="balance-list"></ul>
    <script>
      let balanceListElem = document.getElementById("balance-list");
      for (let i = 1000; i > 0; i -= 100) {
        if (i >= 300 && i <= 600) {
          balanceListElem.innerHTML += "<li> hidden </li>";
        } else {
          balanceListElem.innerHTML += "<li> $ " + i + "</li>";
        }
      }
    </script>
  </body>
</html>
```

</details>

-----

## Step 6: Change the Hidden Range

### Problem

Finally, let's adjust the logic. Modify your code so that it hides balances that are between $500 and $700 (inclusive) instead of the previous range.

### Hint

<details>
<summary>Stuck on Step 6? Click for a hint!</summary>

  - This is a small change. You only need to edit the numbers inside your `if` condition.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 6? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Grow numbers</title>
  </head>
  <body>
    <ul id="balance-list"></ul>
    <script>
      let balanceListElem = document.getElementById("balance-list");
      for (let i = 1000; i > 0; i -= 100) {
        if (i >= 500 && i <= 700) {
          balanceListElem.innerHTML += "<li> hidden </li>";
        } else {
          balanceListElem.innerHTML += "<li> $ " + i + "</li>";
        }
      }
    </script>
  </body>
</html>
```

</details>