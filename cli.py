# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from game import Game,Board
from player import Human,Bot
import pandas as pd

if __name__ == '__main__':

    stats = pd.read_csv('win_database.csv')
    
    noValidInput = True
    while(noValidInput):
        gamemode = input('Enter 1 to play against a bot\nEnter 2 for multiplayer\nEnter 3 to see stats:\n')
        try:
            gamemode = int(gamemode)
            if (gamemode==1) or (gamemode==2):
                noValidInput = False
            else:
                raise Exception
        except:
            print('\t\nInvalid input, try again\n')
    
    
    if(gamemode==1):
        while(noValidInput):
            player1Name = input('Enter Player Name: ')
            if player1Name=='Bot':
                print('\nYou are not a bot, please use a different name\n')
            else:
                noValidInput==False
        player1 = Human('O',player1Name)
        player2 = Bot('X')
    elif(gamemode==2):
        while(noValidInput):
            player1Name = input('Enter Player 1 Name: ')
            if player1Name=='Bot':
                print('\nYou are not a bot, please use a different name\n')
            else:
                noValidInput==False
        while(noValidInput):
            player2Name = input('Enter Player 2 Name: ')
            if player2Name=='Bot':
                print('\nYou are not a bot, please use a different name\n')
            else:
                
                noValidInput==False
        player1 = Human('O',player1Name)
        player2 = Human('X',player2Name)
    else:
        #TODO
        pass
    
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
        
        

