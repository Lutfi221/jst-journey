import random

def play_high_low():
    # 1. Setup the deck (1-13 representing Ace through King)
    # We use a list comprehension here, but [1, 2, 3... 13] works too!
    deck = list(range(1, 14))
    
    # 2. Shuffle the list in place
    random.shuffle(deck)
    
    score = 0
    # .pop(0) removes the first item from the list and returns it
    current_card = deck.pop(0)
    
    print("--- Welcome to High-Low! ---")
    print("Cards are numbered 1 (Ace) through 13 (King).")

    # The game continues as long as there are cards left in the list
    while len(deck) > 0:
        print(f"\nThe current card is: {current_card}")
        print(f"Cards remaining in deck: {len(deck)}")
        
        guess = input("Will the next card be Higher or Lower? (h/l): ").lower()
        
        # Pull the next card
        next_card = deck.pop(0)
        print(f"The next card was: {next_card}")
        
        # 3. Logic to check the guess
        if (guess == 'h' and next_card > current_card) or \
           (guess == 'l' and next_card < current_card):
            score += 1
            print(f"Correct! Your score is: {score}")
        elif next_card == current_card:
            print("It's a tie! No points, but you're still in.")
        else:
            print("Oops! Wrong guess.")
            # We break the loop if they guess wrong
            break
            
        # The 'next' card becomes the 'current' card for the next round
        current_card = next_card

    print("\n--- Game Over ---")
    print(f"Final Score: {score}")
    if len(deck) == 0:
        print("Amazing! You cleared the whole deck!")

if __name__ == "__main__":
    play_high_low()