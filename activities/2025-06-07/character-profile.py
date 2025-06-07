# Game Character Profile - A simple Python program to practice using dictionaries.

def show_introduction():
    """Prints the welcome message for the program."""
    print("Selamat datang di Pembuat Profil Karakter Game!")
    print("Silakan jawab beberapa pertanyaan untuk membuat karaktermu.")
    print("-" * 50)

def create_character_profile():
    """
    Prompts the user for character details and stores them in a dictionary.
    
    Returns:
        A dictionary containing the character's profile information.
    """
    print("Membuat karakter baru...")
    
    # Get information from the user.
    name = input("Siapa nama karaktermu? ")
    char_class = input(f"Apa kelas dari {name}? (misal: Prajurit, Penyihir, Pemanah) ")
    hometown = input(f"Dari mana {name} berasal? ")
    
    # Create a dictionary to hold the character's data.
    # The 'keys' are strings that describe the data ('name', 'class', 'hometown').
    # The 'values' are the variables containing the user's input.
    profile = {
        "name": name,
        "class": char_class,
        "hometown": hometown
    }
    
    print("Profil berhasil dibuat!")
    return profile

def display_character_profile(profile_dict):
    """
    Displays a formatted summary of a character's profile from a dictionary.
    
    Args:
        profile_dict: The dictionary containing the character's data.
    """
    print("\n--- Profil Karakter ---")
    # We access the data in the dictionary using its keys.
    print(f"Nama     : {profile_dict['name']}")
    print(f"Kelas    : {profile_dict['class']}")
    print(f"Asal     : {profile_dict['hometown']}")
    print("-----------------------")

"""The main function that runs the application."""
show_introduction()

# We call the function to create the profile and store the returned dictionary.
character_data = create_character_profile()

# We then pass that dictionary to the display function.
display_character_profile(character_data)

print("\nSelamat bertualang!")
