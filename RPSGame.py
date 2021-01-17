# File name: RPSGame.py
# Author: Jesse Malinen
# Description: Simple Rock-Paper-Scissors game

# import random to get the AI choice
import random

# defining the main function
def RPSGame():
    
    # score tallies
    ai_win_count = 0
    player_win_count = 0
    ties = 0
    
    # main loop
    while True:
        choices = ['rock', 'paper', 'scissors']
        ai_choice = random.choice(choices) # ai chooses one randomly from list
        
        user_choice = input('(rock, paper, scissors) Type your choice: ').strip().lower()
        print()
        ai_wins = 'The AI wins!'
        player_wins = 'You win!'
        
        # determining winner, adding to tallies with +=1
        print(f'You played {user_choice}, the computer played {ai_choice}')
        if user_choice == 'scissors' and ai_choice == 'rock' or \
           user_choice == 'paper' and ai_choice == 'scissors' or \
           user_choice == 'rock' and ai_choice == 'paper':
            print(ai_wins)
            ai_win_count += 1

        elif user_choice == 'rock' and ai_choice == 'scissors' or \
            user_choice == 'scissors' and ai_choice == 'paper' or \
                user_choice == 'paper' and ai_choice == 'rock':
                print(player_wins)
                player_win_count += 1

        else:
            if user_choice == ai_choice:
                print('Its a draw!')
                ties += 1

        print(f'Computer: {ai_win_count} - You: {player_win_count} - Ties: {ties}')
        
RPSGame()