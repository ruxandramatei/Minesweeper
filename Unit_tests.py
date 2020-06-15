from Configuration import *
from Result import *
from Status import *
from MinesweeperGame import *
from MinesweeperResult import *
from Square import *
from ClassRunner import *

import pytest
import unittest

def flip(array):
    return [list(a) for a in zip(*array)]

class TestMinesweeperGame(unittest.TestCase):
    
    def setUp(self):

        mines = flip([
            [False, True,  False],
            [False, False, False],
            [False, False, True]
        ])
        
        self.game = MinesweeperGame(Configuration(3, 3, 2), mines)

    def test_check_status_at_beginning_of_game(self):

        assert Status.PLAYING == self.game.game_status


    def test_check_if_already_exposed_square(self):

        self.game.select_square(0, 2)

        with pytest.raises(ValueError):
            self.game.select_square(1, 1)
            
        assert 1 == self.game.number_of_moves


    def test_check_when_game_is_already_over(self):
        self.game.select_square(1, 0)
        with pytest.raises(ValueError):
            self.game.select_square(0, 0)

        assert self.game.game_over
    
    def test_check_if_game_is_over_after_calling_quit(self):
        self.game.select_square(0, 0)
        self.game.quit_game()

        assert self.game.game_over

    def test_check_selecting_an_outside_position(self):
        with pytest.raises(ValueError):
            self.game.select_square(2, 3)

        assert 0 == self.game.number_of_moves

if __name__ == '__main__':
    unittest.main()