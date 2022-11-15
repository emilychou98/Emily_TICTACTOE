# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from game import Game,Board
from player import Human,Bot

if __name__ == '__main__':
    
    noValidInput = True
    while(noValidInput):
        gamemode = input('Enter 1 to play against a bot, enter 2 for multiplayer:\n')
        try:
            gamemode = int(gamemode)
            if (gamemode==1) or (gamemode==2):
                noValidInput = False
        except:
            print('Invalid input, try again')
    
    
    if(gamemode==1):
        player1 = Human('O')
        player2 = Bot('X')
    else:
        player1 = Human('O')
        player2 = Human('X')
    
    welcome_string = '''
          The game is Tic Tac Toe, and will ask you to enter two inputs 
          when it is your turn. On your turn, enter a signle digit number for
          the row you want to mark, and a single digit number for the column 
          you want to mark (e.g entering 3 and 1 will mark the lower left corner). 
          The numbers must be either 1, 2, or 3 as the board is only 3x3. 
          Good Luck!
          '''
    
    print(welcome_string)
    
    game = Game(player1,player2)
    game.run()
        
        

