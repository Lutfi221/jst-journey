import datetime

print("--- My Digital Journal ---")

# 1. Ask the user to type their journal entry
entry = input("What's on your mind today? \n> ")

# 2. Get the current date and time
current_time = datetime.datetime.now()
# Format the time to look nice (e.g., 2026-06-28 17:04:59)
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 3. Open (or create) the text file in "append" mode
with open("journal.txt", "a") as file:
    # Write the time, the entry, and a divider line to the file
    file.write(f"[{formatted_time}]\n")
    file.write(f"{entry}\n")
    file.write("------------------------\n")

print("\nSuccess! Your entry has been saved to journal.txt.")
