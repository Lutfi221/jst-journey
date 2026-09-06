from google import genai

def create_game_session (api_key):
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-3.5-flash")
    return chat, client

def start_story(chat_session, character_name, theme):
    prompt = f"""
    Let's play a text-based adventure game. 
    Th theme is {theme} and the main character is {character_name}.
    Please write the opening scene of the story.
    Crucial rule: At the end of every response, give me 2 or 3 numbered choices.
    """
    response = chat_session.send_message(prompt)
    return response.text

def play_game():
    print("Welcome to the story builder_OFF!")
    print("_" * 30)

    my_api_key = "XXXX"
    game_chat, game_client = create_game_session(my_api_key)
    print("\n[System: Ai Connection Successful!]")
    
    name = input("What is your name? ")
    scene = input("What is the scene? ")

    print(f"\nAwesome, getting ready to start a {scene} adventure for {name}.")
    print("\nGenerating your adventure..\n")
    theme = start_story(game_chat, name, scene)
    print(theme)



play_game()