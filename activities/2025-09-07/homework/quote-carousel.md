Of course! Here is the homework assignment for building a quote carousel, crafted in the style of your provided examples.

# HTML/JS Homework: Building a Quote Carousel

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the HTML and JavaScript code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by opening the HTML file in a web browser!**

-----

## Final Goal

When you're finished, you will have built a simple but fully functional web-based quote carousel. It will display a quote and its author, with "Previous" and "Next" buttons to cycle through a collection of quotes. The final page will look and function like this:

**Quote Carousel**

> "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world."
>
> Albert Einstein

[Previous] [Next]

-----

## Step 1: Initial Setup

Start with the following basic HTML structure. This creates the title, placeholder elements for the quote and author, and two buttons. Your work will involve adding the JavaScript logic to make it interactive. Save this in a file named `quote-carousel.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quote Carousel</title>
</head>
<body>
    <h1>Quote Carousel</h1>
    <div id="quote-container">
        <p id="quote"></p>
        <p id="author"></p>
    </div>
    <button>Previous</button>
    <button>Next</button>

    <script>
        // Your JavaScript code will go here
    </script>
</body>
</html>
```

-----

## Step 2: Storing the Quotes

### Problem

Before we can display quotes, we need to store them in our program. Your task is to create the data for our carousel.

Inside the `<script>` tag, your code should:

1.  Create a JavaScript array variable named `authors` that holds a list of at least four author names (as strings).
2.  Create another JavaScript array variable named `quotes` that holds a corresponding list of quotes for each author.

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  - You can declare an array variable in JavaScript using the `let` keyword and square brackets `[]`. For example: `let my_array = ["first item", "second item"];`.
  - Make sure the order of your authors matches the order of their quotes in the two arrays.

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
    <title>Quote Carousel</title>
</head>
<body>
    <h1>Quote Carousel</h1>
    <div id="quote-container">
        <p id="quote"></p>
        <p id="author"></p>
    </div>
    <button>Previous</button>
    <button>Next</button>

    <script>
        let authors = [
            "Steve Jobs",
            "Albert Einstein",
            "Maya Angelou",
            "Nelson Mandela",
        ]
        let quotes = [
            "The only way to do great work is to love what you do.",
            "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
            "You have to be a little crazy to do great things.",
            "It always seems impossible until it's done.",
        ]
    </script>
</body>
</html>
```

</details>

-----

## Step 3: Displaying the First Quote

### Problem

Now that we have the data, let's show the first quote when the page loads.

Your script should:

1.  Create a JavaScript variable named `currentIndex` and initialize it to `0`. This will track which quote we are currently viewing.
2.  Create a function named `displayQuote`.
3.  Inside this function, get the HTML elements for the quote and author and update their text to show the quote and author from your arrays at the `currentIndex`.
4.  Call the `displayQuote` function once at the end of your script to display the initial quote.

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  - Use `document.getElementById()` to get a reference to the `<p>` tags with the IDs "quote" and "author".
  - You can access an item in an array by its index, like `quotes[currentIndex]`.
  - To change the text inside an HTML element, you can set its `.innerText` property (e.g., `myElement.innerText = "New text";`).
  - Remember to call `displayQuote();` after you define the function to make it run when the script loads.

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
    <title>Quote Carousel</title>
</head>
<body>
    <h1>Quote Carousel</h1>
    <div id="quote-container">
        <p id="quote"></p>
        <p id="author"></p>
    </div>
    <button>Previous</button>
    <button>Next</button>

    <script>
        let authors = [
            "Steve Jobs",
            "Albert Einstein",
            "Maya Angelou",
            "Nelson Mandela",
        ]
        let quotes = [
            "The only way to do great work is to love what you do.",
            "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
            "You have to be a little crazy to do great things.",
            "It always seems impossible until it's done.",
        ]
        let currentIndex = 0;

        function displayQuote() {
            let quoteElem = document.getElementById("quote");
            let authorElem = document.getElementById("author");
            quoteElem.innerText = quotes[currentIndex];
            authorElem.innerText = authors[currentIndex];
        }

        displayQuote();
    </script>
</body>
</html>
```

</details>

-----

## Step 4: Making the "Next" Button Work

### Problem

The "Next" button is still just for show. Let's make it functional.

Your task is to:

1.  Create a new JavaScript function called `nextQuote`.
2.  Inside this function, increase the `currentIndex` by 1.
3.  Add logic to check if the `currentIndex` has gone past the end of the `quotes` array. If it has, reset it back to `0`.
4.  After updating the index, call the `displayQuote` function to show the new quote.
5.  Connect this `nextQuote` function to the "Next" button in your HTML so that it runs when clicked.

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  - To get the number of items in an array, you can use its `.length` property (e.g., `quotes.length`).
  - An `if` statement will be needed to check if the index is too high. The condition will be something like `currentIndex >= quotes.length`.
  - To make the button call the function, add an `onclick` attribute to the `<button>` tag: `<button onclick="nextQuote()">Next</button>`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quote Carousel</title>
</head>
<body>
    <h1>Quote Carousel</h1>
    <div id="quote-container">
        <p id="quote"></p>
        <p id="author"></p>
    </div>
    <button>Previous</button>
    <button onclick="nextQuote()">Next</button>

    <script>
        let authors = [
            "Steve Jobs",
            "Albert Einstein",
            "Maya Angelou",
            "Nelson Mandela",
        ]
        let quotes = [
            "The only way to do great work is to love what you do.",
            "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
            "You have to be a little crazy to do great things.",
            "It always seems impossible until it's done.",
        ]
        let currentIndex = 0;

        function displayQuote() {
            let quoteElem = document.getElementById("quote");
            let authorElem = document.getElementById("author");
            quoteElem.innerText = quotes[currentIndex];
            authorElem.innerText = authors[currentIndex];
        }

        function nextQuote() {
            currentIndex = currentIndex + 1;
            if (currentIndex >= quotes.length) {
                currentIndex = 0;
            }
            displayQuote();
        }

        displayQuote();
    </script>
</body>
</html>
```

</details>

-----

## Step 5: Making the "Previous" Button Work

### Problem

Finally, let's complete the carousel by making the "Previous" button functional.

Your task is to:

1.  Create a new JavaScript function called `prevQuote`.
2.  Inside this function, decrease the `currentIndex` by 1.
3.  Add logic to check if the `currentIndex` has become less than `0`. If it has, set it to the index of the last item in the array.
4.  After updating the index, call the `displayQuote` function.
5.  Connect this `prevQuote` function to the "Previous" button in your HTML.

### Hint

<details>
<summary>Stuck on Step 5? Click for a hint!</summary>

  - The index of the last item in an array is always its length minus one (`quotes.length - 1`).
  - The `if` statement in this function will check `currentIndex < 0`.
  - Remember to add the `onclick` attribute to your "Previous" button in the HTML.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 5? Click to reveal!</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quote Carousel</title>
</head>
<body>
    <h1>Quote Carousel</h1>
    <div id="quote-container">
        <p id="quote"></p>
        <p id="author"></p>
    </div>
    <button onclick="prevQuote()">Previous</button>
    <button onclick="nextQuote()">Next</button>

    <script>
        let authors = [
            "Steve Jobs",
            "Albert Einstein",
            "Maya Angelou",
            "Nelson Mandela",
        ]
        let quotes = [
            "The only way to do great work is to love what you do.",
            "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
            "You have to be a little crazy to do great things.",
            "It always seems impossible until it's done.",
        ]
        let currentIndex = 0;

        function displayQuote() {
            let quoteElem = document.getElementById("quote");
            let authorElem = document.getElementById("author");
            quoteElem.innerText = quotes[currentIndex];
            authorElem.innerText = authors[currentIndex];
        }

        function prevQuote() {
            currentIndex = currentIndex - 1;
            if (currentIndex < 0) {
                currentIndex = quotes.length - 1;
            }
            displayQuote();
        }

        function nextQuote() {
            currentIndex = currentIndex + 1;
            if (currentIndex >= quotes.length) {
                currentIndex = 0;
            }
            displayQuote();
        }

        displayQuote();
    </script>
</body>
</html>
```

</details>

-----

## You Finished! 🎉

You've built a complete, interactive quote carousel! You have practiced:

  - Storing data in **JavaScript arrays**.
  - Using a **variable** (`currentIndex`) to keep track of the application's state.
  - Selecting HTML elements with `document.getElementById`.
  - Manipulating HTML content using `.innerText`.
  - Defining and calling **JavaScript functions**.
  - Using **`if` statements** for conditional logic.
  - Handling user interaction with the **`onclick`** event handler.

Well done!