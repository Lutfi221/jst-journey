# Build Your Own AI Story Game! 🚀

Welcome to your first AI project! Today, we are going to build a text-based adventure game. You will give the game a character and a theme, and the AI will generate an interactive story just for you.

We are going to write this code step-by-step. Don't worry if you haven't seen some of these words before—we will use simple analogies to explain everything!

---

## Step 1: Bring in the Toolbox (The Import)

**The Analogy:** Imagine you want to build a wooden birdhouse. You can't just build it with your bare hands; you need to go to your garage and bring out your toolbox. 

In Python, a "toolbox" is called a library. We need to bring in the Google toolbox so our code knows how to talk to Google's AI.

**The Code:**
```python
from google import genai
```
*Why we need it:* This line tells Python, "Hey, go grab the `genai` tools so we can build our AI game."

---

## Step 2: Build the Engine (The Helper Functions)

**The Analogy:** Think of the AI like a super-smart friend who lives far away. To talk to them, you need to dial a very specific phone number and press a bunch of confusing buttons. 

Instead of making you (the game creator) press those confusing buttons every single time, we are going to build **Helper Functions**. A function is like an automatic machine: you give it something simple, it does the hard work behind the scenes, and gives you back the result.

### Helper 1: The Phone Line
First, we need a machine that connects to the AI and remembers our conversation.

```python
def create_game_session(api_key):
    # We use our secret password (api_key) to get a "phone"
    client = genai.Client(api_key=api_key)
    
    # We start a chat with the smartest model available
    chat = client.chats.create(model="gemini-3.5-flash")
    
    # We return this active chat line so the game can use it
    return chat
```

### Helper 2: The Story Starter
Next, we need a machine that tells the AI the rules of our game (the character, the theme, and that it must give us numbered choices).

```python
def start_story(chat_session, character_name, theme):
    # We write a secret message telling the AI how to behave
    prompt = f"""
    Let's play a text-based adventure game. 
    The theme is {theme} and the main character is {character_name}. 
    Please write the opening scene of the story. 
    Crucial rule: At the end of every response, give me 2 or 3 numbered choices for what to do next.
    """
    # We send the message over our chat line
    response = chat_session.send_message(prompt)
    
    # We hand back the AI's story text
    return response.text
```

### Helper 3: The Action Taker
Finally, we need a simple machine for when the player makes a choice (like "1" or "Run away!").

```python
def take_action(chat_session, user_action):
    # Send what the user typed to the AI
    response = chat_session.send_message(user_action)
    
    # Hand back what happens next in the story
    return response.text
```

---

## Step 3: Setting the Stage

Now that our "Engine" is built, we can start writing the actual game! 

**The Analogy:** Before a play begins, the director needs to set up the stage, turn on the lights, and ask the actors for their names.

**The Code:**
```python
def play_game():
    print("Welcome to the AI Story Builder!")
    print("-" * 30)
    
    # 1. Turn on the AI (Replace with your actual key!)
    my_api_key = "YOUR_API_KEY" 
    game_chat = create_game_session(my_api_key)
    
    # 2. Ask the player for their character and theme
    name = input("Enter your character's name: ")
    theme = input("Enter a theme (e.g., haunted house, space, pirate): ")
    
    # 3. Use our helper machine to get the very first scene
    print("\nGenerating your adventure...\n")
    scene = start_story(game_chat, name, theme)
    print(scene)
```
*Why we need it:* We use `input()` to pause the program and wait for the player to type something. Then, we feed those answers into our `start_story` machine.

---

## Step 4: The Game Loop (The Beating Heart)

**The Analogy:** Playing a game is like a game of ping-pong. You hit the ball (make a choice), the AI hits it back (tells you what happened), and you hit it again. This back-and-forth keeps going in a loop until someone decides to quit. 

In Python, we use a `while True:` loop to keep the game running forever until we tell it to `break` (stop).

**The Code:**
```python
    # 4. The Infinite Game Loop
    while True:
        # Ask the player what they want to do
        action = input("\nWhat do you do next? (or 'quit' to stop): ")
        
        # Check if they typed 'quit'
        if action.lower() == 'quit':
            print("\nThanks for playing! The end.")
            break # This smashes the loop and ends the game
            
        print("\nLoading the next scene...\n")
        
        # Pass the player's choice to our helper machine
        next_scene = take_action(game_chat, action)
        
        # Print out the new part of the story!
        print(next_scene)
```
*Why we need it:* Without this loop, the game would end after just one turn!

---

## Step 5: Start the Engine!

At the very bottom of our file, we just need one line to tell Python to actually run our game when we click "Play".

```python
# Start the program
if __name__ == "__main__":
    play_game()
```

---

## The Finished Masterpiece 🎨

Here is what your code looks like all put together. Copy this whole thing, paste it into your Python file, add your API key, and have fun!

```python
from google import genai

# ==========================================
# PART 1: THE AI ENGINE (Helper Machines)
# ==========================================

def create_game_session(api_key):
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-3.5-flash")
    return chat

def start_story(chat_session, character_name, theme):
    prompt = f"""
    Let's play a text-based adventure game. 
    The theme is {theme} and the main character is {character_name}. 
    Please write the opening scene of the story. 
    Crucial rule: At the end of every response, give me 2 or 3 numbered choices for what to do next.
    """
    response = chat_session.send_message(prompt)
    return response.text

def take_action(chat_session, user_action):
    response = chat_session.send_message(user_action)
    return response.text


# ==========================================
# PART 2: THE GAME (The Ping-Pong Loop)
# ==========================================

def play_game():
    print("Welcome to the AI Story Builder!")
    print("-" * 30)
    
    my_api_key = "YOUR_API_KEY" 
    game_chat = create_game_session(my_api_key)
    
    name = input("Enter your character's name: ")
    theme = input("Enter a theme (e.g., haunted house, space, pirate): ")
    
    print("\nGenerating your adventure...\n")
    scene = start_story(game_chat, name, theme)
    print(scene)
    
    while True:
        action = input("\nWhat do you do next? (or 'quit' to stop): ")
        
        if action.lower() == 'quit':
            print("\nThanks for playing! The end.")
            break
            
        print("\nLoading the next scene...\n")
        next_scene = take_action(game_chat, action)
        print(next_scene)

if __name__ == "__main__":
    play_game()
```