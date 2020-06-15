from Configuration import *
from Result import *
from Status import *
from MinesweeperGame import *
from MinesweeperResult import *
from Square import *
from ClassRunner import *

import pytest
import unittest

class TestMinesweeperGame(unittest.TestCase):
    @pytest.fixture
    def game():
        mines = flip([
            [False, True,  False],
            [False, False, False],
            [False, False, True]
        ])
        
        return MinesweeperGame(Configuration(3, 3, 2), mines)

    def test_check_status_at_beginning_of_game(game):

        assert Status.PLAYING == game.game_status


    def test_check_if_already_exposed_square(game):

        game.select_square(0, 2)

        with pytest.raises(ValueError):
            game.select_square(1, 1)
            
        assert 1 == game.number_of_moves


    def test_check_when_game_is_already_over(game):
        game.select_square(1, 0)
        with pytest.raises(ValueError):
            game.select_square(0, 0)

        assert game.game_over
    
    def test_check_if_game_is_over_after_calling_quit(game):
        game.select_square(0, 0)
        game.quit_game()

        assert game.game_over

    def test_check_selecting_an_outside_position(game2):
        with pytest.raises(ValueError):
            game.select_square(2, 3)

        assert 0 == game.num_moves

if __name__ == '__main__':
    unittest.main()