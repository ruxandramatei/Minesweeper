import logging

from Configuration import *
from Result import *
from Status import *
from MinesweeperGame import *
from MinesweeperResult import *
from Square import *
from classRunner import *
from classML import *
from visualize import *

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

print("This will play a single game and then quit.")
print("The minesweeper window needs focus to capture a key press.")
print()

number_of_games = 1
configuration = Configuration()
ai = gameGenerator()
visualize = PyGameVisualizer(pause=1, next_game_prompt=True)
result = run_set_of_games(configuration, number_of_games, ai, visualize).pop()
print('Game lasted {0} moves'.format(result.number_of_moves))