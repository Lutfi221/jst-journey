# Shopping List Manager - A simple Python program to practice using lists.


def show_introduction():
    """Prints the welcome message for the program."""
    print("Welcome to the Shopping List Manager!")
    print("You can add, remove, and view items on your list.")
    print("-" * 35)  # Prints a decorative line


def show_menu():
    """Displays the main menu options and gets the user's choice."""
    print("\nPlease select an option:")
    print("1. Add an item to the list")
    print("2. Remove an item from the list")
    print("3. View the current list")
    print("4. Exit the program")
    return input("Enter your choice (1-4): ")


def show_list(the_list):
    """
    Displays all the items currently in the shopping list.
    The list is passed as an argument.
    """
    print("\n--- Your Shopping List ---")
    if not the_list:  # An empty list evaluates to False
        print("Your list is currently empty.")
    else:
        # Loop through the list and print each item with its number
        for i, item in enumerate(the_list, 1):
            print(f"{i}. {item}")
    print("--------------------------")


def add_item(the_list):
    """
    Asks the user for a new item and adds it to the list.
    It checks for duplicates before adding.
    """
    new_item = input("What item would you like to add? ")
    if new_item in the_list:
        print(f"Sorry, '{new_item}' is already on your list.")
    else:
        # .append() adds the new item to the end of the list.
        the_list.append(new_item)
        print(f"'{new_item}' has been added to your list.")


def remove_item(the_list):
    """
    Asks the user for an item to remove from the list.
    It handles the case where the item does not exist.
    """
    if not the_list:
        print("Your list is already empty. There is nothing to remove.")
        return  # Exit the function early

    item_to_remove = input("What item would you like to remove? ")

    # We must check if the item exists before trying to remove it.
    # Trying to .remove() an item that isn't in the list will cause an error.
    if item_to_remove in the_list:
        the_list.remove(item_to_remove)
        print(f"'{item_to_remove}' has been removed from your list.")
    else:
        print(f"Sorry, '{item_to_remove}' was not found on your list.")


"""The main function that runs the application."""
# Initialize an empty list to hold our shopping items.
shopping_list = []

show_introduction()

# The main application loop. It continues until the user chooses to exit.
while True:
    user_choice = show_menu()

    if user_choice == "1":
        add_item(shopping_list)
    elif user_choice == "2":
        remove_item(shopping_list)
    elif user_choice == "3":
        show_list(shopping_list)
    elif user_choice == "4":
        print("Thank you for using the Shopping List Manager. Goodbye!")
        break  # This exits the while loop
    else:
        print("That's not a valid choice. Please enter a number from 1 to 4.")

    # After most actions, it's helpful to show the user the updated list.
    if user_choice in ["1", "2"]:
        show_list(shopping_list)
