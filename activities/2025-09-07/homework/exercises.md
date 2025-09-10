Of course! Here is the homework assignment for the HTML/JS exercises, written in the requested format.

-----

# HTML/JS Homework: Basic DOM Manipulation

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the HTML and JavaScript code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by opening the HTML file in a web browser!**

-----

## Final Goal

When you're finished, you will have built a single page with four separate interactive components. Each one demonstrates a different way to use JavaScript to manipulate the content of an HTML page based on user actions like clicking a button.

[Here's a video of the final result](./exercises-demo.mp4)

-----

## Initial Setup

Start with the following basic HTML structure. This creates the titles, buttons, and text areas for all four exercises. Your job is to add the JavaScript logic to make each part work as described. Save this code in a file named `exercises.html`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>HTML JS exercises</title>
  </head>
  <body>
    <h1>Reveal text using button</h1>
    <button>Reveal secret message</button>
    <p id="secret-message"></p>

    <script>
      // TODO: Add your js code here
    </script>

    <h1>Switch text using button</h1>
    <button>Switch text</button>
    <p id="text-to-switch">FRONT</p>

    <script>
      // TODO: Add your js code here
    </script>

    <h1>Say what?</h1>
    <button>Say Hello</button>
    <button>Say Goodbye</button>

    <script>
      // TODO: Add your js code here
    </script>

    <h1>Screamer</h1>
    <button>Aah</button>
    <p id="screamer-text">A</p>

    <script>
      // TODO: Add your js code here
    </script>
  </body>
</html>
```

-----

## Step 1: Reveal a Secret Message

### Problem

The first button, "Reveal secret message," currently does nothing. Your task is to make it so that when a user clicks this button, a secret message appears in the empty paragraph below it.

Your script should:

1.  Create a JavaScript function.
2.  Inside the function, set the text of the paragraph element with the ID `secret-message` to `"The password is I see bread people'"`.
3.  Connect this function to the "Reveal secret message" button so it runs on a click.

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  * To make a button clickable, add an `onclick` attribute to the `<button>` tag in your HTML.
  * The `onclick` attribute should call a function you define, for example: `onclick="revealText()"`.
  * You can define a function in your `<script>` tag like this: `function revealText() { ... }`.
  * To find an HTML element from JavaScript, use `document.getElementById("element-id")`.
  * To change the text inside an element, set its `.innerText` property: `myElement.innerText = "some new text";`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```html
<h1>Reveal text using button</h1>
<button onclick="revealText()">Reveal secret message</button>
<p id="secret-message"></p>

<script>
  function revealText() {
    let secretMessage = "The password is I see bread people'";
    document.getElementById("secret-message").innerText = secretMessage;
  }
</script>
```

</details>

-----

## Step 2: Switch Text on a Button Click

### Problem

The next button, "Switch text," should toggle the text in the paragraph below it between "FRONT" and "BACK" each time it's clicked.

Your script should:

1.  Create a JavaScript function.
2.  Inside the function, get the paragraph element with the ID `text-to-switch`.
3.  Check what its current text is.
4.  If the current text is "FRONT", change it to "BACK".
5.  Otherwise (if it's "BACK"), change it back to "FRONT".
6.  Connect this function to the "Switch text" button.

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * You'll need an `if/else` statement in your JavaScript function.
  * First, get the element and store it in a variable: `let textElem = document.getElementById("text-to-switch");`.
  * Then, get its current text: `let currentText = textElem.innerText;`.
  * Your condition will look like this: `if (currentText == "FRONT") { ... } else { ... }`.
  * Inside the `if` and `else` blocks, you will set the `textElem.innerText` to the new value.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```html
<h1>Switch text using button</h1>
<button onclick="switchText()">Switch text</button>
<p id="text-to-switch">FRONT</p>

<script>
  function switchText() {
    let textElem = document.getElementById("text-to-switch");
    let currentText = textElem.innerText;
    if (currentText == "FRONT") {
      textElem.innerText = "BACK";
    } else {
      textElem.innerText = "FRONT";
    }
  }
</script>
```

</details>

-----

## Step 3: Create Reusable Alerts with Parameters

### Problem

In the "Say what?" section, there are two buttons. You need to make the "Say Hello" button show an alert box that says "Hello", and the "Say Goodbye" button show an alert that says "Goodbye". You must accomplish this using only **one** JavaScript function.

Your script should:

1.  Create a single JavaScript function that accepts one parameter (e.g., `message`).
2.  Inside the function, call the built-in `alert()` function, passing the `message` parameter to it.
3.  Connect this function to both buttons, making sure to pass the correct string ("Hello" or "Goodbye") as an argument from each button's `onclick` attribute.

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * Define your function to accept a parameter: `function say(message) { ... }`.
  * Inside the function, simply use `alert(message);`.
  * In your HTML, the `onclick` attribute for the first button should be `onclick="say('Hello')"`. Notice the single quotes inside the double quotes. This is how you pass a string value. Do the same for the "Goodbye" button.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```html
<h1>Say what?</h1>
<button onclick="say('Hello')">Say Hello</button>
<button onclick="say('Goodbye')">Say Goodbye</button>

<script>
  function say(message) {
    alert(message);
  }
</script>
```

</details>

-----

## Step 4: Append Text to Create a Scream

### Problem

For the final exercise, the "Aah" button should make the text in the paragraph below it grow longer with each click. The text starts as "A". The first click should change it to "Aa", the second to "Aaa", the third to "Aaaa", and so on.

Your script should:

1.  Create a JavaScript function.
2.  Inside the function, get the paragraph element with the ID `screamer-text`.
3.  Read its current text content.
4.  Append the letter "a" to the end of that text.
5.  Update the element's text to this new, longer string.
6.  Connect the function to the "Aah" button.

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * Get the element: `let screamerText = document.getElementById("screamer-text");`.
  * To append text to a string in JavaScript, you can use the `+` operator.
  * The core logic will be: `screamerText.innerText = screamerText.innerText + "a";`. This reads the current text, adds "a" to it, and then writes the result back into the element.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```html
<h1>Screamer</h1>
<button onclick="scream()">Aah</button>
<p id="screamer-text">A</p>

<script>
  function scream() {
    let screamerText = document.getElementById("screamer-text");
    screamerText.innerText = screamerText.innerText + "a";
  }
</script>
```

</details>

-----

## You Finished!

You've built several interactive web components! You have practiced:

  * Handling user clicks with the **`onclick`** event handler.
  * Selecting HTML elements from JavaScript using `document.getElementById`.
  * Reading and writing content to HTML elements with `.innerText`.
  * Using `if/else` statements for conditional logic.
  * Creating reusable functions that accept **parameters**.
  * Using string concatenation to modify text.

Well done!