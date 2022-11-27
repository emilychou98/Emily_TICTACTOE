import pandas as pd
from typing import Dict

class Database:

    def __init__(self,games_file:str=None,players_file:str=None,
            moves_file:str=None) -> None:
        if games_file:
            self.games = pd.read_csv(games_file)
        else:
            self.games = pd.DataFrame()#TODO

        if players_file:
            self.players = pd.read_csv(players_file)
        else:
            self.players = pd.DataFrame()#TODO
        
        if moves_file:
            self.moves = pd.read_csv(moves_file)
        else:
            self.moves = pd.DataFrame() #TODO


    def add_game_result(self, game_result:Dict[tuple])->None:
        player1_res = game_result['O']
        player2_res = game_result['X']
        self.games.append({
            'player1_name': player1_res['name'],
            'player1_result': player1_res['result'],
            'player2_name': player2_res['name'],
            'player2_result': player2_res['result']
        })

        pd.to_csv('games.csv',index=False)


    def get_player_rank(self, player_name: str)->str:
        