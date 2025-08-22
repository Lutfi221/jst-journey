# HTML/JS Homework: Building an Interactive Grass Grower

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the HTML and JavaScript code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by opening the HTML file in a web browser!**

-----

## Final Goal

When you're finished, you will have built a simple but fun interactive web page. It will have buttons to "grow" grass and mushrooms, and another button to clear the lawn. The final page will look and function like this:

**Grass Grower**

[Grow Grass] [Grow Mushroom] [Destroy Lawn]

  * ☘️
  * ☘️
  * 🍄
  * ☘️

-----

## Step 1: Initial Setup

Start with the following basic HTML structure. This creates the title, a button to grow grass, and an empty list that will serve as our "lawn". Your work will involve adding the JavaScript logic to make it interactive. Save this in a file named `grass-grower.html`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF--8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Grass Grower</title>
  </head>
  <body>
    <h1>Grass Grower</h1>
    <button>Grow Grass</button>
    <ul id="lawn"></ul>

    <script></script>
  </body>
</html>
```

-----

## Step 2: Making the Grass Grow

### Problem

Right now, the "Grow Grass" button doesn't do anything. Your task is to write the JavaScript code to make it functional.

Your script should:

1.  Create a JavaScript variable that references the HTML `<ul>` element where the grass will grow.
2.  Create a JavaScript function named `growGrass`.
3.  Inside the `growGrass` function, write code to add a new list item containing a shamrock emoji (`<li>☘️</li>`) to the lawn.
4.  Connect this `growGrass` function to the "Grow Grass" button in your HTML so that it runs when the button is clicked.

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * To get a reference to an HTML element, use `document.getElementById('some-id')`. The `<ul>` in the HTML has an `id` of "lawn".
  * To add HTML content to an element, you can modify its `.innerHTML` property. The pattern `myElement.innerHTML = myElement.innerHTML + '...'` will append new content.
  * Define a function like this: `function growGrass() { ... }`.
  * To make the button call this function, add an `onclick` attribute to the `<button>` tag in your HTML: `<button onclick="growGrass()">Grow Grass</button>`.

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
    <title>Grass Grower</title>
  </head>
  <body>
    <h1>Grass Grower</h1>
    <button onclick="growGrass()">Grow Grass</button>
    <ul id="lawn"></ul>

    <script>
      let lawnElem = document.getElementById("lawn");
      function growGrass() {
        lawnElem.innerHTML = lawnElem.innerHTML + "<li>☘️</li>";
      }
    </script>
  </body>
</html>
```

</details>

-----

## Step 3: Adding a Mushroom

### Problem

Growing grass is great, but every lawn needs variety. Let's add a button to grow a mushroom.

Your task is to:

1.  Add a new "Grow Mushroom" button to your HTML, right next to the "Grow Grass" button.
2.  Create a brand new JavaScript function called `growMushroom`.
3.  The `growMushroom` function should do the same thing as `growGrass`, but it should add a mushroom emoji (`<li>🍄</li>`) to the lawn.
4.  Connect your new button to this `growMushroom` function.

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * Your new function `growMushroom()` will be very similar to your `growGrass()` function.
  * The logic inside will be almost identical: `lawnElem.innerHTML = lawnElem.innerHTML + '<li>🍄</li>';`.
  * Make sure to add the `onclick` attribute to your new `<button>` tag in the HTML.

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
    <title>Grass Grower</title>
  </head>
  <body>
    <h1>Grass Grower</h1>
    <button onclick="growGrass()">Grow Grass</button>
    <button onclick="growMushroom()">Grow Mushroom</button>
    <ul id="lawn"></ul>

    <script>
      let lawnElem = document.getElementById("lawn");
      function growGrass() {
        lawnElem.innerHTML = lawnElem.innerHTML + "<li>☘️</li>";
      }
      function growMushroom() {
        lawnElem.innerHTML = lawnElem.innerHTML + "<li>🍄</li>";
      }
    </script>
  </body>
</html>
```

</details>

-----

## Step 4: Adding a "Destroy Lawn" Button

### Problem

The final feature is a way to clear the lawn and start over. Let's add a button that removes all the grass and mushrooms.

Your task is to:

1.  Add a "Destroy Lawn" button to your HTML.
2.  Create a new JavaScript function called `destroyLawn`.
3.  Inside the `destroyLawn` function, write code that clears all the content from the `lawnElem`.
4.  Connect the "Destroy Lawn" button to this new function.

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * This is the simplest function you'll write.
  * The function definition will be `function destroyLawn() { ... }`.
  * To clear the content of an element, you can set its `.innerHTML` property to an empty string: `lawnElem.innerHTML = '';`.
  * Don't forget the `onclick="destroyLawn()"` in the HTML for your new button.

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
    <title>Grass Grower</title>
  </head>
  <body>
    <h1>Grass Grower</h1>
    <button onclick="growGrass()">Grow Grass</button>
    <button onclick="growMushroom()">Grow Mushroom</button>
    <button onclick="destroyLawn()">Destroy Lawn</button>
    <ul id="lawn"></ul>
    <script>
      let lawnElem = document.getElementById("lawn");
      function growGrass() {
        lawnElem.innerHTML = lawnElem.innerHTML + "<li>☘️</li>";
      }
      function growMushroom() {
        lawnElem.innerHTML = lawnElem.innerHTML + "<li>🍄</li>";
      }
      function destroyLawn() {
        lawnElem.innerHTML = "";
      }
    </script>
  </body>
</html>
```

</details>

-----

## You Finished!

You've built a complete, interactive web component! You have practiced:

  * Structuring a web page with basic **HTML tags** (`h1`, `ul`, `button`).
  * Using **JavaScript variables** with `let` to store references to HTML elements.
  * Selecting HTML elements with `document.getElementById`.
  * Manipulating HTML content from JavaScript using `.innerHTML`.
  * Defining and calling multiple **JavaScript functions**.
  * Handling user interaction with the **`onclick`** event handler.

Well done!