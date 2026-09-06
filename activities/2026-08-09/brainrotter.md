Here is a step-by-step tutorial designed directly for your student. It builds the app piece by piece, ensuring they can run the code at every stage to see their progress and catch errors early.

---

# Build a Brainrot Summarizer App

In this project, you're going to build an AI app that reads a text file and summarizes it using heavy internet slang. Instead of writing the whole thing at once, we are going to build it in four stages.

**Before you start:**
Make sure you have your Gemini API key handy and that you have the library installed. Run this in your terminal if you haven't already:
`pip install google-genai`

1. **The Drag-and-Drop CLI:** Getting input from the user.
First, we need a way for the user to give our app a file. Command Line Interfaces (CLI) actually support drag-and-drop! When you drag a file into a terminal, it pastes the file's path (where it lives on your computer).

Sometimes, the terminal wraps this path in invisible spaces or quotation marks, so we use a concept called **string stripping** to clean it up before using it.

Write this code and run it. Try dragging a text file into your terminal when it asks!

```python
def run_brainrotter():
    print("Welcome to the Brainrotter 3000!")
    print("_" * 30)
    
    # input() pauses the code and waits for the user
    raw_input = input("\nDrag and drop your text file here (and press Enter): ")
    
    # .strip() removes trailing spaces and extra quotes that the terminal might add
    file_path = raw_input.strip(' \'"')
    
    print(f"\nAwesome, I will look for a file at: {file_path}")

# Start the app
run_brainrotter()

```


2. **Reading the File Safely:** Handling errors and file I/O.
Now that we have the path, we need to open the file and read the text inside it.

We will use a `try / except` block. This is a crucial programming concept: it tells Python, "Try to do this dangerous thing (opening a file). If it blows up (because the file doesn't exist), don't crash the whole program. Do this instead."

Update your `run_brainrotter` function to look like this, then run it again! Test it with a real text file, and then test it by typing a fake name to see your error message in action.

```python
def run_brainrotter():
    print("Welcome to the Brainrotter 3000!")
    print("_" * 30)
    
    raw_input = input("\nDrag and drop your text file here (and press Enter): ")
    file_path = raw_input.strip(' \'"')
    
    try:
        # 'with open' safely opens the file and automatically closes it when done
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        print(f"\nSuccess! Here are the first 50 characters of your file:")
        print(content[:50] + "...") # Only print a little bit so we don't flood the screen
        
    except FileNotFoundError:
        print("\nBruh, that file doesn't exist. L + ratio.")
    except Exception as e:
        print(f"\nOof, something went wrong: {e}")

run_brainrotter()

```


3. **Connecting to the AI Engine:** API clients and sessions.
Now we are going to set up our connection to Gemini. We will create a separate function for this to keep our code organized.

We use the API key to prove we are allowed to use the AI, and we tell it which "model" we want to use. We are setting up a `chat` session so the AI can remember context if we decide to add follow-up questions later.

Add the import at the top, add the new function, and update your main loop to call it. Run it to make sure you see the "Connection Successful" message!

```python
import os
from google import genai

# --- NEW FUNCTION ---
def create_ai_session(api_key):
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-3.5-flash")
    return chat, client

def run_brainrotter():
    print("Welcome to the Brainrotter 3000!")
    print("_" * 30)

    # Put your actual API key here!
    my_api_key = "YOUR_API_KEY_HERE" 
    ai_chat, ai_client = create_ai_session(my_api_key)
    print("\n[System: Ai Connection Successful, no cap!]")
    
    raw_input = input("\nDrag and drop your text file here (and press Enter): ")
    file_path = raw_input.strip(' \'"')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        print(f"\nAwesome, reading the text. Let him cook...")
        
    except FileNotFoundError:
        print("\nBruh, that file doesn't exist. L + ratio.")
    except Exception as e:
        print(f"\nOof, something went wrong: {e}")

run_brainrotter()

```


4. **Prompt Engineering:** Sending data and getting a response.
The final step! We need to take the text we read from the file and inject it into a set of instructions (a prompt) for the AI.

We will use an **f-string** (notice the `f` before the quotes). This allows us to easily drop variables like `{file_content}` directly into a block of text. We send that prompt to our chat session, wait for the AI to think, and print the response.

Add the `generate_brainrot_summary` function, update the `try` block to use it, and you have a finished app!

```python
import os
from google import genai

def create_ai_session(api_key):
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-3.5-flash")
    return chat, client

# --- NEW FUNCTION ---
def generate_brainrot_summary(chat_session, file_content):
    prompt = f"""
    Take the following text and summarize it into exactly 3 sentences. 
    Crucial rule: You must use heavy Gen Z / Gen Alpha "brainrot" internet slang (e.g., skibidi, rizz, gyatt, mewing, sigma, fanum tax, no cap, let him cook).
    
    Text to summarize:
    {file_content}
    """
    # This sends the message and pauses the code until the AI replies
    response = chat_session.send_message(prompt)
    return response.text

def run_brainrotter():
    print("Welcome to the Brainrotter 3000!")
    print("_" * 30)

    my_api_key = "YOUR_API_KEY_HERE" 
    ai_chat, ai_client = create_ai_session(my_api_key)
    print("\n[System: Ai Connection Successful, no cap!]")
    
    raw_input = input("\nDrag and drop your text file here (and press Enter): ")
    file_path = raw_input.strip(' \'"')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        print(f"\nAwesome, reading the text. Let him cook...\n")
        
        # --- NEW CODE ---
        summary = generate_brainrot_summary(ai_chat, content)
        print(summary)
        
    except FileNotFoundError:
        print("\nBruh, that file doesn't exist. L + ratio.")
    except Exception as e:
        print(f"\nOof, something went wrong: {e}")

run_brainrotter()

```