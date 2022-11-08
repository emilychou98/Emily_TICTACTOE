# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import make_empty_board, get_winner, other_player


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    currentPlayer = 'O'
    while winner == None:
        
        for row in board:
            printLine = [x if x is not None else '_' for x in row]
            print(printLine[0],printLine[1],printLine[2])
        
        noValidInput = True
        while(noValidInput):
            y = input(
                f'{currentPlayer}\'s turn! Type row you want to mark\n'
            )
            x = input(
                f'{currentPlayer}\'s turn! Type column you want to mark\n'
            )
            
            try:
                x = int(x)-1
                y = int(y)-1
                if (x<0) or (x>4) or (y<0) or (y>4):
                    print('row or column selected out of bounds')
                    continue                
                if board[y][x] is not None:
                    print('This spot is already marked!')
                    continue
                
                board[y][x] = currentPlayer
                noValidInput=False
            except:
                print('Invalid input, try again')
        
        currentPlayer = other_player(currentPlayer)
        winner = get_winner(board)
        
        if winner is not None:
            for row in board:
                printLine = [x if x is not None else '_' for x in row]
                print(printLine[0],printLine[1],printLine[2])
            print(f'{other_player(currentPlayer)} wins!')
        
        isDraw = True
        for row in board:
            if None in row:
                isDraw = False
        if isDraw:
            print('Draw!')
            break

