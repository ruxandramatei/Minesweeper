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

    def check_status_at_beginning_of_game(game):

        assert Status.PLAYING == game.game_status


    def check_if_already_exposed_square(game):

        game.select_square(0, 2)

        with pytest.raises(ValueError):
            game.select_square(1, 1)
            
        assert 1 == game.number_of_moves


    def check_when_game_is_already_over(game):
        game.select_square(1, 0)
        with pytest.raises(ValueError):
            game.select_square(0, 0)
        assert game.game_over


if __name__ == '__main__':
    unittest.main()