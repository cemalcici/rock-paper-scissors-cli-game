# Global packages
import random

# Local packages
from .functions import control_user_input, decide_who_win_game, draw_rps_art

if __name__ == '__main__':
    isExit = False
    while not isExit:
        usr_input = input(
            "What do you choose? " +\
            "Type 0 for Rock, 1 for Paper or 2 for Scissors " +\
            "(Press 'q' to exit)\n"
        )
        if usr_input.lower() == 'q':
            print('Thanks for playing!')
            break
        
        user_choice = control_user_input(usr_input)
        computer_choice = random.randint(0, 2)

        print('Your choice:')
        print(draw_rps_art(user_choice))
        print(f"Computer choice:")
        print(draw_rps_art(computer_choice))
        print(decide_who_win_game(user_choice, computer_choice))
