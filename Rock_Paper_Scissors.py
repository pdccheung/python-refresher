import random
from secrets import choice

choices = ["rock", "paper", "scissors"]
win_count = 0
comp_win_count = 0
print ("Welcome to Rock Paper Scissors, Your opponent is the computer, first to 5 victories wins the game!" )

while (win_count < 5 and comp_win_count < 5 ):
    user_choice = input("Choose Rock, Paper, or Scissors, what is your choice? " )
    comp_choice = random.choice(choices)
    
    if user_choice.lower() == "rock": 
        if comp_choice == "rock":
            print(f"You played {user_choice} and Computer chose {comp_choice}, Tie game, go again")
        elif comp_choice == "paper":
            print(f"You played {user_choice} and Computer chose {comp_choice}, You Lose")
            comp_win_count = comp_win_count + 1
        else: 
            win_count = win_count + 1
            print(f"You played {user_choice} and Computer chose {comp_choice}, You win count is at {win_count}")
    elif user_choice.lower() == "paper": 
        if comp_choice == "rock":
            win_count = win_count + 1
            print(f"You played {user_choice} and Computer chose {comp_choice}, You win count is at {win_count}")
        elif comp_choice == "paper":
            print(f"You played {user_choice} and Computer chose {comp_choice}, Tie game, go again")
        else: 
            print(f"You played {user_choice} and Computer chose {comp_choice}, You Lose")
            comp_win_count = comp_win_count + 1
    elif user_choice.lower() == "scissors": 
        if comp_choice == "rock":
            print(f"You played {user_choice} and Computer chose {comp_choice}, You Lose")
            comp_win_count = comp_win_count + 1
        elif comp_choice == "paper":
            win_count = win_count + 1
            print(f"You played {user_choice} and Computer chose {comp_choice}, You win count is at {win_count}")
        else: 
            print(f"You played {user_choice} and Computer chose {comp_choice}, Tie game, go again")
    else:
        print(f"Your choice of {user_choice} is an invalid choice, please choose again")
    

if win_count == 5: 
    print("Congratulations, you've won the game")
elif comp_win_count == 5: 
    print(f"The computer has {comp_win_count} wins, which means you lose" )