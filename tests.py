import unittest
import logic


class TestLogic(unittest.TestCase):
    
    def test_get_winner(self):
        """unit tests get_winner function of logic.py
        """
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
        board = [
            ['X', None, 'O'],
            [None, 'O', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), None)
        
        board = [
            [None, 'O', None],
            ['X', 'O', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
        
        board = [
            ['O', None, 'O'],
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
        board = [
            ['O', None, 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
        board = [
            ['O', None, 'X'],
            ['O', 'O', 'X'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
        board = [
            ['O', None, 'X'],
            ['O', 'X', 'X'],
            ['O', 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

    def test_other_player(self):
        """unit tests other_player function of logic.py
        """
        self.assertEqual(logic.other_player('X'),'O')
        self.assertEqual(logic.other_player('O'),'X')

    def test_make_empty_board(self):  
        """unit tests make_empty_board function of logic.py
        """  
        self.assertEqual(len(logic.make_empty_board()),3)
        self.assertEqual(len(logic.make_empty_board()[0]),3)
        self.assertEqual(logic.make_empty_board()[0][0],None)

if __name__ == '__main__':
    unittest.main()