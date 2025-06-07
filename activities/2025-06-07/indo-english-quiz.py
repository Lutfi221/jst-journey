import random

# This dictionary stores our vocabulary.
# The 'key' is the Indonesian word, and the 'value' is the English translation.
VOCABULARY = {
    "kucing": "cat",
    "buku": "book",
    "rumah": "house",
    "apel": "apple",
    "air": "water",
    "matahari": "sun"
}

def show_introduction():
    """Prints the welcome message for the quiz."""
    print("Selamat datang di Kuis Bahasa Indonesia-Inggris!")
    print("Saya akan memberimu sebuah kata dalam Bahasa Indonesia,")
    print("dan kamu harus menebak artinya dalam Bahasa Inggris.")
    print("-" * 50)

def get_random_word(vocab_dict):
    """
    Selects a random key-value pair from the vocabulary dictionary.
    
    Args:
        vocab_dict: The dictionary to pick a word from.
        
    Returns:
        A tuple containing the Indonesian word and its English translation.
    """
    # Dictionaries don't have indexes like lists, so we can't use random.choice() directly.
    # First, we get a list of all the keys (Indonesian words) from our dictionary.
    word_list = list(vocab_dict.keys())
    
    # Then, we can use random.choice() to pick one word from that list.
    indonesian_word = random.choice(word_list)
    
    # Once we have the key (the Indonesian word), we can look up its value
    # (the English translation) in the dictionary.
    english_translation = vocab_dict[indonesian_word]
    
    return indonesian_word, english_translation

def play_round():
    """
    Plays a single round of the quiz. Returns True if the player was correct, False otherwise.
    """
    # Get a random word pair for this round.
    indonesian, correct_english = get_random_word(VOCABULARY)
    
    # Ask the user for their guess.
    prompt = f"\nApa bahasa Inggris dari '{indonesian}'? "
    user_guess = input(prompt)
    
    # Compare the user's guess with the correct answer.
    # .lower() makes the comparison case-insensitive, so "Cat" and "CAT" are also correct.
    if user_guess.lower() == correct_english:
        print("Benar sekali! Jawabanmu tepat.")
        return True
    else:
        print(f"Salah. Jawaban yang benar adalah '{correct_english}'.")
        return False

"""The main function that runs the application."""
show_introduction()

player_score = 0
rounds_played = 0

# The main application loop.
while True:
    # Play one round and update the score
    if play_round():
        player_score += 1
    
    rounds_played += 1
    
    # Ask the user if they want to play again.
    play_again_input = input("Main lagi? (yes/no): ").lower()
    if play_again_input not in ["yes", "y"]:
        break # Exit the loop if the answer isn't 'yes' or 'y'
        
# After the loop ends, show the final score.
print("\n--- Kuis Selesai ---")
print(f"Skor akhir kamu: {player_score} dari {rounds_played} pertanyaan.")
print("Terima kasih sudah bermain!")
