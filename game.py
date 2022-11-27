from typing import List, Dict, Optional
from player import Player
from database import Database

class Board:
    def __init__(self) -> None:
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        
    def get_board(self) -> List[List[Optional[str]]]:
        return self.board
    
    def set_board(self, new_board : List[List[Optional[str]]]) -> None:
        self.board = new_board
        
    def print_board(self)->None:
        for row in self.board:
            printLine = [x if x is not None else '_' for x in row]
            print(printLine[0],printLine[1],printLine[2])
        print()


class Game:

    def __init__(self, player1: Player, player2: Player, database: Database) -> None:
        self.board = Board()
        self.current_player = player1
        self.other_player = player2
        self.database = database

    def run(self) -> None:
        winner = None
        while winner is None:            
            self.board.print_board()
            #check if all spaces are filled and it's a draw
            if self.check_draw(self.board):
                print('Draw!')
                self.output_game_result(
                    self.current_player,'draw',
                    self.other_player,'draw'
                )
                break
            
            #have current player make move
            self.board.set_board(
                self.current_player.make_move(
                    self.board.get_board()
                )
            )

            #check winner
            winner = self.get_winner(self.board)
            
            #Winner found, print end result
            if winner is not None:
                self.board.print_board()
                print(f'{self.current_player.get_name()} wins!')
                self.output_game_result(
                    self.current_player,'win',
                    self.other_player,'lose'
                )
                break

            self.switch_players()
            
    def switch_players(self)->None:
        placeholder = self.current_player
        self.current_player = self.other_player
        self.other_player = placeholder
        
    def check_draw(self, board_obj: Board) -> bool:
        #check if its a draw
        isDraw = True
        for row in board_obj.get_board():
            #if there is space left in the board, it's not a draw
            if None in row:
                isDraw = False
        return isDraw
    
    def get_winner(self, board_obj: Board) -> Optional[str]:
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        
        board = board_obj.get_board()
        
        for i in range(3):
            if (board[i][0]==board[i][1] 
                    and board[i][1]==board[i][2]):
                return board[i][0] #return row winner
            if (board[0][i]==board[1][i] 
                    and board[1][i]==board[2][i]):
                return board[0][i] #return col winner
        if (board[0][0]==board[1][1] 
                    and board[1][1]==board[2][2]):
            return board[0][0]
        elif (board[2][0]==board[1][1] 
                    and board[1][1]==board[0][2]):
            return board[2][0]

        return None
    
    def get_board(self)->Board:
        return self.board

    def output_game_result(
                self,player1:Player,result1:str,player2:Player,result2:str
            ) -> Dict[tuple]:

        self.database.add_game_result({
            player1.get_char(): 
                {
                    'name':player1.get_name(),
                    'result': result1
                },
            player2.get_char(): 
                {
                    'name':player2.get_name(),
                    'result': result2
                }
        })
    