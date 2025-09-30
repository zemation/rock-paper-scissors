"""A simple command-line rock-paper-scissors game."""
import random
import sys

CHOICES = ["rock", "paper", "scissors"]
WINNING_COMBINATIONS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

def get_winner(user_choice, computer_choice):
    """Determines the winner of a round."""
    if user_choice == computer_choice:
        return "tie"
    if WINNING_COMBINATIONS.get(user_choice) == computer_choice:
        return "user"
    return "computer"

def display_score(user_wins, computer_wins):
    """Displays the current score."""
    print("\n--- Score ---")
    print(f"User: {user_wins} | Computer: {computer_wins}")
    print("---------------")

def game():
    """Main game loop for Rock, Paper, Scissors."""
    user_wins = 0
    computer_wins = 0

    while abs(user_wins - computer_wins) < 2:
        display_score(user_wins, computer_wins)

        # Get user input
        user_input = input(f"Choose {'/'.join(CHOICES)}, or 'q' to quit: ").lower()

        if user_input == 'q':
            print("Thanks for playing!")
            sys.exit()

        if user_input not in CHOICES:
            print(f"Invalid choice. Please choose from {'/'.join(CHOICES)}.")
            continue

        # Get computer choice
        computer_choice = random.choice(CHOICES)
        print(f"You chose: {user_input}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        winner = get_winner(user_input, computer_choice)

        if winner == "user":
            print("🎉 You won this round!")
            user_wins += 1
        elif winner == "computer":
            print("🤖 Computer won this round!")
            computer_wins += 1
        else:
            print("It's a tie!")

    # Announce the final winner
    display_score(user_wins, computer_wins)
    if user_wins > computer_wins:
        print("\nCongratulations! You won the game! 🏆")
    else:
        print("\nSorry, the computer won the game. Better luck next time! 💻")

def main():
    """Entry point of the program."""
    game()

if __name__ == "__main__":
    main()
