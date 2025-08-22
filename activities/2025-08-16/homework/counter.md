# HTML/JS Homework: Building an Interactive Counter

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the HTML and JavaScript code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by opening the HTML file in a web browser!**

-----

## Final Goal

When you're finished, you will have built a simple but fully functional web-based counter. It will have buttons to add to the count, multiply the count, and reset it back to zero. The final page will look and function like this:

**Simple Counter**
Count: 0

[+1] [+5] [+10] [2x] [3x] [Reset]

-----

## Initial Setup

Start with the following basic HTML structure. This creates the title, the initial count display, and a single button. Your work will involve adding the JavaScript logic to make it interactive. Save this in a file named `counter.html`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Simple Counter</title>
  </head>
  <body>
    <h1>Simple Counter</h1>
    <p>Count: <span id="count">0</span></p>
    <button>+1</button>

    <script></script>
  </body>
</html>
```

-----

## Step 1: Making the First Button Work

### Problem

Right now, the `+1` button doesn't do anything. Your task is to write the JavaScript code to make it functional.

Your script should:

1.  Create a JavaScript variable to keep track of the count, starting at `0`.
2.  Create a JavaScript variable that references the HTML element where the count is displayed.
3.  Create a JavaScript function named `add`.
4.  Inside the `add` function, write code to increase the count variable by 1 and then update the text of the display element to show the new count.
5.  Connect this `add` function to the `+1` button in your HTML so that it runs when the button is clicked.

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  * You can declare variables in JavaScript using the `let` keyword (e.g., `let count = 0;`).
  * To get a reference to an HTML element, use `document.getElementById('some-id')`. The `span` in the HTML has an `id` of "count".
  * To change the text inside an HTML element, you can set its `.innerText` property (e.g., `myElement.innerText = count;`).
  * Define a function like this: `function add() { ... }`.
  * To make the button call this function, add an `onclick` attribute to the `<button>` tag in your HTML: `<button onclick="add()">+1</button>`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Counter</title>
</head>
<body>
    <h1>Simple Counter</h1>
    <p>Count: <span id="count">0</span></p>
    <button onclick="add()">+1</button>

    <script>
        let count = 0;
        let countElement = document.getElementById('count');
        function add() {
            count = count + 1;
            countElement.innerText = count;
        }
    </script>
</body>
</html>
```

</details>

-----

## Step 2: Adding More Buttons with a Dynamic Function

### Problem

The `add` function is great, but it only adds 1. Let's make it more powerful so it can handle different amounts.

Your task is to:

1.  Add two new buttons to your HTML: one for `+5` and one for `+10`.
2.  Modify the `add` function so that it accepts a parameter (for example, `amount`).
3.  Inside the function, instead of adding `1` to the count, add the `amount` that was passed into the function.
4.  Update the `onclick` attributes on all three buttons (`+1`, `+5`, and `+10`) to pass the correct amount to the `add` function.

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * Your new function definition will look like `function add(amount) { ... }`.
  * Inside the function, the logic will be `count = count + amount;`.
  * To pass a number from your HTML to the function, use the syntax `onclick="add(5)"`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Counter</title>
</head>
<body>
    <h1>Simple Counter</h1>
    <p>Count: <span id="count">0</span></p>
    <button onclick="add(1)">+1</button>
    <button onclick="add(5)">+5</button>
    <button onclick="add(10)">+10</button>

    <script>
        let count = 0;
        let countElement = document.getElementById('count');
        function add(amount) {
            count = count + amount;
            countElement.innerText = count;
        }
    </script>
</body>
</html>
```

</details>

-----

## Step 3: Implementing Multiplication

### Problem

Let's add another way to change the count. Now you'll add buttons that multiply the current count.

Your task is to:

1.  Add two new buttons to your HTML for `2x` and `3x`.
2.  Create a brand new JavaScript function called `multiply` that accepts a parameter (e.g., `amount`).
3.  This function should multiply the current `count` by the `amount` and update the display.
4.  Connect your new buttons to this `multiply` function.

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * The `multiply` function will be very similar to your `add` function.
  * Instead of the `+` operator for addition, you'll use the `*` operator for multiplication.
  * The logic inside the function will be `count = count * amount;`.
  * Make sure to add the `onclick` attributes to your new buttons in the HTML.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Counter</title>
</head>
<body>
    <h1>Simple Counter</h1>
    <p>Count: <span id="count">0</span></p>
    <button onclick="add(1)">+1</button>
    <button onclick="add(5)">+5</button>
    <button onclick="add(10)">+10</button>
    <button onclick="multiply(2)">2x</button>
    <button onclick="multiply(3)">3x</button>

    <script>
        let count = 0;
        let countElement = document.getElementById('count');
        function add(amount) {
            count = count + amount;
            countElement.innerText = count;
        }
        function multiply(amount) {
            count = count * amount;
            countElement.innerText = count;
        }
    </script>
</body>
</html>
```

</details>

-----

## Step 4: Adding a Reset Button

### Problem

The final feature is a way to start over. Let's add a button that resets the counter to zero.

Your task is to:

1.  Add a "Reset" button to your HTML.
2.  Create a new JavaScript function called `reset`. This function does not need to accept any parameters.
3.  Inside the `reset` function, set the `count` variable back to `0` and update the display.
4.  Connect the "Reset" button to this new function.

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * This is the simplest function you'll write.
  * The function definition will be `function reset() { ... }`.
  * The code inside is just two lines: one to set `count = 0` and one to update `countElement.innerText`.
  * Don't forget the `onclick="reset()"` in the HTML for your new button.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale-1.0">
    <title>Simple Counter</title>
</head>
<body>
    <h1>Simple Counter</h1>
    <p>Count: <span id="count">0</span></p>
    <button onclick="add(1)">+1</button>
    <button onclick="add(5)">+5</button>
    <button onclick="add(10)">+10</button>
    <button onclick="multiply(2)">2x</button>
    <button onclick="multiply(3)">3x</button>
    <button onclick="reset()">Reset</button>

    <script>
        let count = 0;
        let countElement = document.getElementById('count');
        function add(amount) {
            count = count + amount;
            countElement.innerText = count;
        }
        function multiply(amount) {
            count = count * amount;
            countElement.innerText = count;
        }
        function reset() {
            count = 0
            countElement.innerText = count;
        }
    </script>
</body>
</html>
```

</details>

-----

## You Finished!

You've built a complete, interactive web component! You have practiced:

  * Structuring a web page with basic **HTML tags** (`h1`, `p`, `button`).
  * Using **JavaScript variables** with `let` to store state.
  * Selecting HTML elements with `document.getElementById`.
  * Manipulating HTML content from JavaScript using `.innerText`.
  * Defining and calling **JavaScript functions**.
  * Using **parameters** to make functions reusable.
  * Handling user interaction with the **`onclick`** event handler.

Well done!