from typing import List, Optional
import random 

class Player:
    def __init__(self, player_char:str) -> None:
        self.char = player_char
        
    def get_char(self) -> str:
        return self.char
    
class Human(Player):
    
    def make_move(self, board: List[List[Optional[str]]]
            ) -> List[List[Optional[str]]]:
        noValidInput = True
        while(noValidInput):
            y = input(
                f'Player {self.get_char()}\'s turn! Type row you want to mark\n'
            )
            x = input(
                f'Player {self.get_char()}\'s turn! Type column you want to mark\n'
            )
            
            try:
                x = int(x)-1
                y = int(y)-1
                if (x<0) or (x>2) or (y<0) or (y>2):
                    print('row or column selected out of bounds, try again\n')
                    continue                
                if board[y][x] is not None:
                    print('This spot is already marked!, try again\n')
                    continue
                
                board[y][x] = self.get_char()
                noValidInput=False
            except:
                print('Invalid input, input must be a single digit number, try again\n')
        return board        
        
        
class Bot(Player):
    
    def make_move(self, board: List[List[Optional[str]]]
            ) -> List[List[Optional[str]]]:
        
        #Middle space is the best
        #take it if available
        if board[1][1] is None:
            board[1][1] = self.get_char()
            print('Bot has made a move!')
            return board
        
        available_spaces = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] is None:
                    available_spaces.append((row,col))
                    
        selected = random.choice(available_spaces)
        board[selected[0]][selected[1]] = self.get_char()
        print('Bot has made a move!')
        return board