import random
import sys

items = ["rock", "paper", "scissors"]

def main():
    game()

def game():
    user_win = 0
    comp_win = 0 

    
    while True:
        computer = random.choice(items)
        print(f"User: {user_win}  | Computer: {comp_win}")

        if (user_win - comp_win) == 2:
            sys.exit("You win this game")
        elif (comp_win - user_win) == 2:
            sys.exit("Computer wins this game")
            
     

        user_input = input('Rock, Paper, Scissors, Quit <q>: ').lower()
        print(user_win)
        if user_input == 'q':
            sys.exit("User Exited Game")
        elif user_input == computer:
            print(f"Tie.  Both Selected {user_input}")
            continue
        elif user_input == 'rock' and computer == 'scissors' or user_input == 'paper' and computer == 'rock' or user_input == 'scissors' and computer == 'paper':
            print(f"You won this round!  User: {user_input}, Computer {computer}")
            user_win += 1
            continue
        elif computer == 'rock' and user_input == 'scissors' or computer == 'paper' and user_input == 'rock' or computer == 'scissors' and user_input == 'paper':
            print(f"Computer won this round! User: {user_input}, Computer {computer}")
            comp_win += 1
            continue
        else:
            continue




if __name__ == "__main__":
    main()