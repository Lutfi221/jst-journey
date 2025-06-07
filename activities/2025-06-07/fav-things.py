# My Favorite Things - A simplified Python program to practice lists.

def show_introduction():
    """Prints the welcome message for the program."""
    print("Selamat datang di aplikasi 'Benda Favoritku'!")
    print("Ketik nama benda untuk ditambahkan ke daftar.")
    print("Ketik 'keluar' untuk berhenti dan melihat daftar final.")
    print("-" * 30) # Prints a line for separation

def show_favorite_things(things_list):
    """
    Displays all the items currently in the list of favorite things.
    The list is passed as an argument.
    """
    print("\n--- Daftar Benda Favoritku Saat Ini ---")
    if not things_list: # An empty list evaluates to 'False' in Python
        print("Daftarmu masih kosong!")
    else:
        # We loop through the list and print each item with a number.
        # enumerate gives us both the index (starting from 1) and the item.
        for i, thing in enumerate(things_list, 1):
            print(f"{i}. {thing}")
    print("------------------------------------")

# We initialize an empty list to store the favorite things.
favorite_things = []

show_introduction()

# This is the main loop of our program. It will run until the user types 'keluar'.
while True:
    # Ask the user for a new item.
    new_thing = input("\nMasukkan benda favorit baru: ")

    # Check if the user wants to exit the loop.
    # .lower() makes the check case-insensitive (e.g., 'Keluar' or 'KELUAR' also works).
    if new_thing.lower() == 'keluar':
        break

    # Check if the item is already in the list to avoid duplicates.
    # The 'in' keyword returns True if the item is found, and False otherwise.
    if new_thing in favorite_things:
        print(f"'{new_thing}' sudah ada di dalam daftar. Coba benda lain.")
    else:
        # If it's not a duplicate, add it to the list.
        favorite_things.append(new_thing)
        print(f"'{new_thing}' telah berhasil ditambahkan!")
    
    # After every attempt to add, print the current list.
    show_favorite_things(favorite_things)

# After the loop finishes, print a final message.
print("\nTerima kasih sudah menggunakan aplikasi ini!")
print("Ini adalah daftar final benda favoritmu:")
show_favorite_things(favorite_things)
