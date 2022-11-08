# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
from typing import List

def make_empty_board():
    """Creates and returns an empty board"""
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board:List):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            return board[i][0] #return row winner
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            return board[0][i] #return col winner
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        return board[0][0]
    elif board[2][0]==board[1][1] and board[1][1]==board[0][2]:
        return board[2][0]

    return None


def other_player(player:str):
    """Given the character for a player, returns the other player."""
    if player == 'O':
        return 'X'
    else:
        return 'O'