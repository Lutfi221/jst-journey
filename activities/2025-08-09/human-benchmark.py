import time
import random
import os

def clear_screen():
    """Clears the terminal screen. Works on Windows, macOS, and Linux."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def reaction_speed_test(num_attempts=3):
    """
    Conducts a reaction speed test for a given number of attempts.

    Args:
        num_attempts (int): The number of times the test should run.

    Returns:
        list: A list of reaction times in seconds for each successful attempt.
    """
    print("# Reaction speed test")
    print("\nPress Enter as soon as you see the word 'GO!'")
    input("Press Enter to start...") # Wait for user to be ready

    reaction_times = []
    for i in range(num_attempts):
        print(f"\n## Attempt {i + 1}")
        print("\nWait for it...")

        # Wait for a random duration between 2 and 6 seconds
        time.sleep(random.uniform(2, 6))

        print("\nGO!")
        start_time = time.time()
        input() # Wait for the user to press Enter
        end_time = time.time()

        reaction_time = end_time - start_time
        reaction_times.append(reaction_time)
        print(f"Reaction time: {reaction_time:.3f} seconds")
        time.sleep(1) # Pause before the next attempt

    return reaction_times

def memorization_test():
    """
    Conducts a number sequence memorization test.

    The number of digits increases with each correct answer. The game
    ends when the user makes a mistake.

    Returns:
        int: The highest number of digits the user successfully memorized.
    """
    print("\n# Memorization")
    print("\nRetype the digits you see on the screen.")
    input("Press Enter to start...")

    num_digits = 3
    attempt_number = 1
    max_digits_memorized = 0

    while True:
        print(f"\n## Attempt {attempt_number}")
        print("\nWait for it...")
        time.sleep(0.1)
        print("GO!")
        time.sleep(0.1)

        # Generate a random sequence of digits
        number_to_memorize = ''.join([random.choice('0123456789') for _ in range(num_digits)])

        print("\nMEMORIZE:")
        print(' '.join(number_to_memorize)) # Print with spaces for readability
        
        # Give the user time to memorize (1 second per digit)
        time.sleep(num_digits)

        clear_screen()
        
        try:
            user_input = input(" > ")
        except KeyboardInterrupt:
            print("\nGame ended.")
            break

        if user_input.strip() == number_to_memorize:
            print("Correct!")
            max_digits_memorized = num_digits
            num_digits += 1 # Increase difficulty
            attempt_number += 1
            input("Press Enter to continue...")
        else:
            print(f"\nWrong! The correct number was {number_to_memorize}")
            break # End the game

    return max_digits_memorized

def main():
    """
    Main function to run the benchmark games and display the report.
    """
    # Run the reaction speed test
    all_reaction_times = reaction_speed_test()
    
    # Run the memorization test
    most_digits = memorization_test()

    # --- BENCHMARK REPORT ---
    print("\n# Benchmark Report")
    print("-" * 20)

    # Calculate and display average reaction time
    if all_reaction_times:
        average_time = sum(all_reaction_times) / len(all_reaction_times)
        print(f"Average reaction time: {average_time:.3f} seconds")
    else:
        print("No reaction times recorded.")

    # Display memorization score
    if most_digits > 0:
        print(f"Most amount of digits memorized: {most_digits}")
    else:
        print("No digits were memorized.")
    
    print("-" * 20)
    print("\nGame over. Thanks for playing!")


# This line ensures the main() function is called only when the script is executed directly
if __name__ == "__main__":
    main()
