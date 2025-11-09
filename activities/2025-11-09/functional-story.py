# A simple, functional CLI game about buying a hotdog.
# This game uses only functions and dictionaries, no classes.

# --- GAME STATE ---

# This dictionary holds all the information about the player.
# We will pass this dictionary to functions to modify it.
player = {
    "name": "Obama",
    "location": "street",  # The player starts on the street.
    "has_house_key": True,  # Let's start with the key to make the game playable.
    "cash": 0,
    "has_atm_card": False,
    "has_shirt": False,     # Player has a shirt in inventory
    "wearing_shirt": False, # Player is currently wearing the shirt
    "hotdog_count": 0
}

# This dictionary holds the state of the game world (e.g., items in locations).
game_state = {
    "house": {
        "has_atm_card": True,  # The ATM card is initially in the house
        "has_shirt": True,     # The shirt is initially in the house
    },
    "bank": {
        "cash_available": 100  # The amount of cash the player can get
    },
    "costco": {
        "hotdog_price": 5      # The price of a hotdog
    }
}

# This dictionary defines all possible actions for each location.
# This is a constant and will not be changed.
AVAILABLE_ACTIONS = {
    "street": ["go to house", "go to bank", "go to costco", "quit"],
    "house": ["get atm card", "get shirt", "wear shirt", "leave house"],
    "bank": ["get cash", "leave bank"],
    "costco": ["buy hotdog", "leave costco", "quit"]
}

# --- HELPER FUNCTIONS ---

def show_status(current_player):
    """Prints the player's current status."""
    print("\n" + "="*20)
    print(f"PLAYER: {current_player['name']}")
    print(f"LOCATION: {current_player['location']}")
    print(f"CASH: ${current_player['cash']}")
    print(f"HOTDOGS: {current_player['hotdog_count']}")
    print("="*20)
    
    # Print inventory
    print("INVENTORY:")
    if current_player["has_house_key"]:
        print("  - House Key")
    if current_player["has_atm_card"]:
        print("  - ATM Card")
    if current_player["has_shirt"]:
        if current_player["wearing_shirt"]:
            print("  - Shirt (wearing)")
        else:
            print("  - Shirt (in bag)")
    
    if not any([current_player["has_house_key"], current_player["has_atm_card"], current_player["has_shirt"]]):
        print("  - (empty)")
    
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

def handle_street_action(current_player, choice):
    """Handles all actions taken from the 'street' location."""
    if choice == "go to house":
        if current_player["has_house_key"]:
            current_player["location"] = "house"
            print("\n>>> You unlocked the door and went inside your house.")
        else:
            print("\n>>> The door is locked! You need a house key.")
            
    elif choice == "go to bank":
        if not current_player["wearing_shirt"]:
            print("\n>>> You can't go to the bank without a shirt! 'No shirt, no service.'")
        elif not current_player["has_atm_card"]:
            print("\n>>> You need your ATM card to use the bank.")
        else:
            current_player["location"] = "bank"
            print("\n>>> You entered the bank.")
            
    elif choice == "go to costco":
        current_player["location"] = "costco"
        print("\n>>> You went to Costco. The smell of hotdogs is amazing.")


def handle_house_action(current_player, current_game_state, choice):
    """Handles all actions taken from the 'house' location."""
    if choice == "get atm card":
        if current_game_state["house"]["has_atm_card"]:
            current_player["has_atm_card"] = True
            current_game_state["house"]["has_atm_card"] = False
            print("\n>>> You found your ATM card on the table.")
        else:
            print("\n>>> You already got the ATM card.")
            
    elif choice == "get shirt":
        if current_game_state["house"]["has_shirt"]:
            current_player["has_shirt"] = True
            current_game_state["house"]["has_shirt"] = False
            print("\n>>> You got a clean shirt from your closet.")
        else:
            print("\n>>> You already took the shirt.")
            
    elif choice == "wear shirt":
        if not current_player["has_shirt"]:
            print("\n>>> You don't have a shirt to wear.")
        elif current_player["wearing_shirt"]:
            print("\n>>> You are already wearing a shirt.")
        else:
            current_player["wearing_shirt"] = True
            print("\n>>> You put on the shirt. You look presentable.")
            
    elif choice == "leave house":
        current_player["location"] = "street"
        print("\n>>> You left the house and are back on the street.")


def handle_bank_action(current_player, current_game_state, choice):
    """Handles all actions taken from the 'bank' location."""
    if choice == "get cash":
        cash_to_get = current_game_state["bank"]["cash_available"]
        if cash_to_get > 0:
            current_player["cash"] += cash_to_get
            current_game_state["bank"]["cash_available"] = 0  # Only one withdrawal
            print(f"\n>>> You withdrew ${cash_to_get} from the ATM.")
        else:
            print("\n>>> You already emptied your account.")
            
    elif choice == "leave bank":
        current_player["location"] = "street"
        print("\n>>> You left the bank and are back on the street.")


def handle_costco_action(current_player, current_game_state, choice):
    """Handles all actions taken from the 'costco' location."""
    if choice == "buy hotdog":
        price = current_game_state["costco"]["hotdog_price"]
        if current_player["cash"] >= price:
            current_player["cash"] -= price
            current_player["hotdog_count"] += 1
            print(f"\n>>> You bought a delicious hotdog for ${price}!")
            print(">>> You win! Enjoy your hotdog.")
        else:
            print(f"\n>>> You don't have enough money. The hotdog costs ${price} and you only have ${current_player['cash']}.")
            
    elif choice == "leave costco":
        current_player["location"] = "street"
        print("\n>>> You left Costco and are back on the street.")


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
    
    # We need a "deep copy" for nested dictionaries like game_state
    # so that changing current_game_state doesn't change the original.
    current_game_state = {
        "house": game_state["house"].copy(),
        "bank": game_state["bank"].copy(),
        "costco": game_state["costco"].copy()
    }


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
        if current_location == "street":
            handle_street_action(current_player, choice)
        elif current_location == "house":
            handle_house_action(current_player, current_game_state, choice)
        elif current_location == "bank":
            handle_bank_action(current_player, current_game_state, choice)
        elif current_location == "costco":
            handle_costco_action(current_player, current_game_state, choice)
            
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