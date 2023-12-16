import random
from typing import Literal

def decide_who_win_game(
    user: Literal[0, 1, 2],
    computer: Literal[0, 1, 2]
) -> str:
    """The function that forms the rule logic of the game Rock Paper Scissors.
    The algorithm was created according to the rules at https://wrpsa.com/the-official-rules-of-rock-paper-scissors/.
    
    - Rock wins against scissors.
    - Scissors win against paper.
    - Paper wins against rock.

    Args:
        user (Literal[0, 1, 2]): User-selected value. Must be 1, 2 and 3.
        computer (Literal[0, 1, 2]): Randomly generated value between 0-2.

    Returns:
        str: Result of the game.
    """
    if (
        (user == 0 and computer == 2) or 
        (user == 2 and computer == 1) or
        (user == 1 and computer == 0)
    ):
        return 'You win!'
    elif user_choice == computer_choice:
        return 'Draw'
    return 'You lose'


def control_user_input(
    user_input: str
) -> int:
    """Function that validates the number received from the user.

    Args:
        user_input (str): The value entered by the user.

    Raises:
        ValueError: Error printing when the value is not numeric.
        ValueError: Error where the value is not between 0 and 2.

    Returns:
        int: _description_
    """
    if user_input.isdecimal():
        if 0 <= int(user_input) <= 2:
            return int(user_input)
        else:
            raise ValueError('The value must only be 0, 1 and 2')
    else:
        raise ValueError('The value must be numeric only.')


user_choice = control_user_input(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
)
computer_choice = random.randint(0, 2)
print(f"Computer choice: {computer_choice}")

print(decide_who_win_game(user_choice, computer_choice))
