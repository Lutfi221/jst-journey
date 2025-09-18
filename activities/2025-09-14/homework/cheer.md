Of course! Here is the homework assignment for building the cheer page, following the structure and style of your examples.

# HTML/JS Homework: Building a Cheer Page with Loops

Follow the steps below. For each step:

1.  **Read the problem carefully.**
2.  **Try to write the HTML and JavaScript code yourself in VS Code.**
3.  **If you get stuck, open the "Hint" section.**
4.  **Once you think you have a solution or want to check your work, open the "Solution" section.**
5.  **Make sure your code works by opening the HTML file in a web browser!**

-----

## Final Goal

When you're finished, you will have built a simple web page that uses JavaScript loops to generate two different lists of encouraging messages. This exercise will teach you how to dynamically create HTML content from data stored in JavaScript arrays.

**Cheer Page**

  - You are a star!

  - You are a champion!

  - You are a genius!

  - ...and so on.

  - You are amazing!

  - You are fantastic!

  - You are wonderful!

  - ...and so on.

-----

## Initial Setup

Start with the following basic HTML structure. It contains two empty unordered lists (`<ul>`) that you will populate using JavaScript. Save this in a file named `cheer.html`.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <ul id="nickname-list"></ul>
    <ul id="cheer-list"></ul>
    <script>
      // code here
    </script>
  </body>
</html>
```

-----

## Step 1: Setting Up the Nicknames

### Problem

Before you can display the list of nicknames, you need to store them in your program and get a reference to the HTML element where they will be displayed.

Your script should:

1.  Create a JavaScript variable that references the HTML element with the ID `nickname-list`.
2.  Create a JavaScript array variable named `nicknames` and fill it with the following strings: `"star"`, `"champion"`, `"genius"`, `"superstar"`, `"rockstar"`, `"legend"`, `"hero"`, `"superhero"`.

### Hint

<details>
<summary>Stuck on Step 1? Click for a hint!</summary>

  * To get a reference to an HTML element, use `document.getElementById('some-id')`. The first `<ul>` in the HTML has an `id` of "nickname-list". Store this in a variable using `let`.
  * To create an array, use square brackets `[]` and separate each string with a comma. For example: `let myArray = ["value1", "value2"];`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 1? Click to reveal!</summary>

```html
<script>
  let nicknameListElem = document.getElementById("nickname-list");
  let nicknames = [
    "star",
    "champion",
    "genius",
    "superstar",
    "rockstar",
    "legend",
    "hero",
    "superhero",
  ];
</script>
```

</details>

-----

## Step 2: Displaying the Nicknames with a Loop

### Problem

Now that you have the data, use a `for` loop to go through each nickname in the `nicknames` array and add it to the webpage as a list item.

Your script should:

1.  Create a `for` loop that iterates through every item in the `nicknames` array.
2.  Inside the loop, for each `nickname`, append a new list item to the `nicknameListElem`. The text should be formatted like: `<li>You are a [nickname]!</li>`.

### Hint

<details>
<summary>Stuck on Step 2? Click for a hint!</summary>

  * A `for` loop structure looks like this: `for (let i = 0; i < array.length; i++) { ... }`. You can get the length of the `nicknames` array with `nicknames.length`.
  * Inside the loop, you can get the current nickname with `let nickname = nicknames[i];`.
  * To add HTML content to an element, you can append to its `.innerHTML` property. The pattern `myElement.innerHTML += '...'` is useful for this.
  * Remember to build the string correctly, for example: `"<li>You are a " + nickname + "!</li>"`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 2? Click to reveal!</summary>

```html
<script>
  let nicknameListElem = document.getElementById("nickname-list");
  let nicknames = [
    "star",
    "champion",
    "genius",
    "superstar",
    "rockstar",
    "legend",
    "hero",
    "superhero",
  ];

  for (let i = 0; i < nicknames.length; i++) {
    let nickname = nicknames[i];
    nicknameListElem.innerHTML += "<li>You are a " + nickname + "!</li>";
  }
</script>
```

</details>

-----

## Step 3: Setting Up the Adjectives

### Problem

Let's prepare for the second list. Similar to the first step, you need to get the HTML element for the cheer list and create an array of adjectives.

Your script should:

1.  Create a JavaScript variable that references the HTML element with the ID `cheer-list`.
2.  Create a JavaScript array variable named `adjectives` and fill it with the following strings: `"amazing"`, `"fantastic"`, `"wonderful"`, `"great"`, `"awesome"`.

### Hint

<details>
<summary>Stuck on Step 3? Click for a hint!</summary>

  * This is very similar to Step 1. Use `document.getElementById('cheer-list')` to get the second list element.
  * Create the `adjectives` array using the same `let adjectives = [...]` syntax you used for the nicknames.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 3? Click to reveal!</summary>

```html
<script>
  // ... code from previous steps ...

  let cheerListElem = document.getElementById("cheer-list");
  let adjectives = ["amazing", "fantastic", "wonderful", "great", "awesome"];
</script>
```

</details>

-----

## Step 4: Displaying the Adjectives with a Loop

### Problem

Finally, create a second `for` loop to display the adjectives in the second list on the webpage.

Your script should:

1.  Create a `for` loop that iterates through every item in the `adjectives` array.
2.  Inside the loop, for each `adjective`, append a new list item to the `cheerListElem`. The text should be formatted like: `<li>You are [adjective]!</li>`.

### Hint

<details>
<summary>Stuck on Step 4? Click for a hint!</summary>

  * This loop will follow the exact same pattern as the one you wrote in Step 2, but it will use the `adjectives` array and the `cheerListElem` variable.
  * The string you build inside this loop will be slightly different: `"<li>You are " + adjective + "!</li>"`.

</details>

### Solution

<details>
<summary>Ready to check your answer for Step 4? Click to reveal!</summary>

```html
<script>
  // ... code from step 1 & 2 ...
  let nicknameListElem = document.getElementById("nickname-list");
  let nicknames = [
    "star",
    "champion",
    "genius",
    "superstar",
    "rockstar",
    "legend",
    "hero",
    "superhero",
  ];

  for (let i = 0; i < nicknames.length; i++) {
    let nickname = nicknames[i];
    nicknameListElem.innerHTML += "<li>You are a " + nickname + "!</li>";
  }

  // ... code from step 3 ...
  let cheerListElem = document.getElementById("cheer-list");
  let adjectives = ["amazing", "fantastic", "wonderful", "great", "awesome"];

  // Solution for step 4
  for (let i = 0; i < adjectives.length; i++) {
    let adjective = adjectives[i];
    cheerListElem.innerHTML += "<li>You are " + adjective + "!</li>";
  }
</script>
```

</details>

-----

## You Finished!

You've successfully used JavaScript to dynamically generate content on a webpage! You have practiced:

  - Selecting HTML elements with `document.getElementById`.
  - Creating and populating **JavaScript arrays**.
  - Using a **`for` loop** to iterate through an array.
  - Accessing array elements by their index (e.g., `myArray[i]`).
  - Modifying a webpage's content by appending to the `.innerHTML` property.

Great job!