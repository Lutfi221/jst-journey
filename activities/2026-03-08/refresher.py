# --- FUNCTION 1 ---
def count_vowels(text):
    # VARIABLE 1
    vowel_count = 0
    
    # FOR LOOP 1
    for letter in text:
        # CONDITIONAL 1
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowel_count = vowel_count + 1
            
    return vowel_count

# --- FUNCTION 2 ---
def analyze_numbers(start_number):
    # FOR LOOP 2
    for i in range(start_number):
        # VARIABLE 2
        current_number = i + 1
        
        # CONDITIONAL 2
        if current_number % 2 == 0:
            # STANDARD I/O 1
            print(str(current_number) + " is an EVEN number.")
        else:
            # STANDARD I/O 2
            print(str(current_number) + " is an ODD number.")

# --- MAIN APP START ---

# STANDARD I/O 3
print("Welcome to the Word and Number Analyzer!")
print("Let's look at a word first.")

# STANDARD I/O 4 & VARIABLE 3
user_word = input("Please enter a word (all lowercase): ")

# STANDARD I/O 5 & VARIABLE 4
user_number_string = input("Please enter a small number (e.g., 5): ")
user_number = int(user_number_string)

print("\n--- Word Results ---")
# Call Function 1
total_vowels = count_vowels(user_word)
print("Your word has " + str(total_vowels) + " vowels in it.")

print("\n--- Number Results ---")
# Call Function 2
analyze_numbers(user_number)

print("\nThank you for using the Analyzer!")