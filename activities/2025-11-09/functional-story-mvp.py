# A simple, functional CLI game about buying a hotdog.
# This game uses only functions and dictionaries, no classes.

# --- GAME STATE ---

# This dictionary holds all the information about the player.
# We will pass this dictionary to functions to modify it.
player = {
    "location": "street",  # The player starts on the street.
    "hotdog_count": 0
}

# This dictionary defines all possible actions for each location.
# This is a constant and will not be changed.
AVAILABLE_ACTIONS = {
    "street": ["go to costco", "quit"],
    "costco": ["buy hotdog", "leave costco", "quit"]
}

# --- HELPER FUNCTIONS ---

def show_status(current_player):
    """Prints the player's current status."""
    print("\n" + "="*20)
    print(f"LOCATION: {current_player['location']}")
    print(f"HOTDOGS: {current_player['hotdog_count']}")
    print("="*20)


def show_possible_actions(location):
    """Prints the actions available at the current location."""
    print("ACTIONS:")
    # Get the list of actions for the location, or an empty list if location is invalid
    actions = AVAILABLE_ACTIONS.get(location, [])
    for i, action in enumerate(actions, 1):
        print(f"  {i}. {action}")
    print("="*20)


def get_player_choice(location):
    """Gets and validates the player's action choice."""
    actions = AVAILABLE_ACTIONS.get(location, [])
    
    while True:
        choice = input("What do you want to do? (Enter a number or the full action): ").strip().lower()
        
        # Check if they entered a number
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(actions):
                return actions[index]  # Return the action string
        
        # Check if they entered the full action string
        if choice in actions:
            return choice
            
        print(f"Invalid choice. Please choose from the list: {', '.join(actions)}")


# --- ACTION HANDLER FUNCTIONS ---
# These functions modify the player and game_state dictionaries.

def handle_action(current_player, choice):
    """Handles all player actions."""
    location = current_player["location"]
    
    if location == "street":
        if choice == "go to costco":
            current_player["location"] = "costco"
            print("\n>>> You went to Costco.")
    
    elif location == "costco":
        if choice == "buy hotdog":
            current_player["hotdog_count"] += 1
            print(f"\n>>> You bought a delicious hotdog!")
            print(">>> You win! Enjoy your hotdog.")
        elif choice == "leave costco":
            current_player["location"] = "street"
            print("\n>>> You left Costco.")


# --- MAIN GAME LOOP ---

def play_game():
    """The main function to run the game."""
    
    print("="*40)
    print("=== WELCOME TO THE HOTDOG QUEST! ===")
    print("="*40)
    print(f"Your goal: Buy a hotdog at Costco.")
    print("Good luck!\n")

    # We make copies of the original state dictionaries.
    # This way, if we wanted to restart the game, the originals are unchanged.
    current_player = player.copy()

    while True:
        # 1. Show the player's current status
        show_status(current_player)
        
        # 2. Show the possible actions based on location
        current_location = current_player["location"]
        show_possible_actions(current_location)
        
        # 3. Get the player's choice
        choice = get_player_choice(current_location)
        
        # 4. Handle the "quit" action first
        if choice == "quit":
            print("\n>>> Thanks for playing. Goodbye!")
            break
            
        # 5. Process the action based on the current location
        handle_action(current_player, choice)
            
        # 6. Check for the win condition
        if current_player["hotdog_count"] > 0:
            print("\n=== CONGRATULATIONS! ===")
            print("You successfully bought a hotdog!")
            print("==========================")
            break

# This special line checks if the script is being run directly
# (as opposed to being imported as a module).
# If it is, it calls the play_game() function.
if __name__ == "__main__":
    play_game()