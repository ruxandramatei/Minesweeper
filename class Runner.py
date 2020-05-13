import logging
from Status import *

logger = logging.getLogger(__name__)

# class for running the game
class Runner:                         # class Game Runner as iterator with attr:   game(Game):Minesweeper game  and
                                                                                 # ml(ML): Minesweeper ML
    def __init__(self, game, ml):
        self.game = game
        self.ml = ml

    def __iter__(self):               # returns iterator
        return self

    def __next__(self):               # allows to run one move
        if not self.game.game_over:                     # if game isn't over, get coordinates of mouse, select the tile and update the move
            coordinates = self.ml.next()
            result = self.game.select_square(*coordinates)
            self.ml.update(result)
            if result.status == Status.PLAYING:         # if game can be played, allow placing of flags
                self.game.flags = self.ml.flags
            else:
                logger.info("Game is over")             # if none applies, display "Game over"
        else:
            raise StopIteration()                       # stop game
