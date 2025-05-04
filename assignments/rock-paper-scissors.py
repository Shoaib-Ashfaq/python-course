import random
import sys

def get_user_move():
    """
    Parses and validates the user's move from command-line arguments.

    Returns:
        str: A valid move ('rock', 'paper', or 'scissors') entered by the user.

    Raises:
        ValueError: If the number of arguments is incorrect or the move is invalid.
        Exits the program if an error is encountered.
    """

    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python rock_paper_scissors.py <your_move>\nValid moves: rock, paper, scissors")
        user_input = sys.argv[1].lower()
        if user_input not in valid_moves:
            raise ValueError("Invalid move. Choose one of: rock, paper, scissors.")
        return user_input
    except ValueError as e:
        print(e)
        sys.exit(1)

def get_computer_move():
    """
    Randomly selects a move for the computer from the list of valid moves.

    Returns:
        str: The computer's move ('rock', 'paper', or 'scissors').
    """

    return random.choice(valid_moves)

def determine_winner(user, computer):
    """
    Determines the winner of a Rock-Paper-Scissors game.

    Args:
        user (str): The user's move ('rock', 'paper', or 'scissors').
        computer (str): The computer's move ('rock', 'paper', or 'scissors').

    Returns:
        str: A message indicating the result - whether it's a tie, user wins, or computer wins.
    """

    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

valid_moves = ["rock", "paper", "scissors"]

user_move = get_user_move()
computer_move = get_computer_move()

print(f"\nYou chose: {user_move}")
print(f"Computer chose: {computer_move}")
result = determine_winner(user_move, computer_move)
print(result)
