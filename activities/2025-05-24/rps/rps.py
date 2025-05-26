import random


def show_intro():
    print("Greetings! I am Mitsuru Nagase (永瀬 充)")
    print("I'm the Rock Paper Scissor champion seven years in a row!")
    print()


def ask_player_to_play():
    print("Do you want to play a game? (yes or no)")
    ans = input()
    print()
    if ans == "y" or ans == "yes":
        return True
    else:
        return False

def get_player_move():
    move = input("Rock, Paper, or Scissors? (r, p, or s): ")
    return move

def get_computer_move():
    return random.choice(["r", "p", "s"])

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif player_move == "r" and computer_move == "s":
        return "player"
    elif player_move == "p" and computer_move == "r":
        return "player"
    elif player_move == "s" and computer_move == "p":
        return "player"
    else:
        return "computer"

player_score = 0
computer_score = 0

show_intro()

player_wants_to_play = ask_player_to_play()

while player_wants_to_play:
    player_move = get_player_move()
    print("You chose " + player_move)

    computer_move = get_computer_move()
    print("Computer chose " + computer_move)

    winner = determine_winner(player_move, computer_move)

    if winner == "player":
        print("You win!")
        player_score = player_score + 1
    elif winner == "computer":
        print("You lose!")
        computer_score = computer_score + 1
    else:
        print("It's a tie!")

    player_wants_to_play = ask_player_to_play()

print("Ok, bye!")

print("=" * 30)
print("Final score:")
print("You: " + str(player_score))
print("Computer: " + str(computer_score))
print("=" * 30)
