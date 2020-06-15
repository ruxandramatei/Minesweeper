import abc
import random

# abstract base class for checking particular methods; keeps all classes together
class ML(abc.ABC):              # ML base class

    @abc.abstractmethod
    def reset(self, config):    # method for playing a new game; args: config (GameConfig): game configuration
        pass

    @abc.abstractmethod         # method for making the next move/click; returning the i,j tuple (position with zero-based index)
    def next(self):
        pass

    @abc.abstractmethod         # method for getting the result of a move; args: result (MoveResult): Information about the move
    def update(self, result):
        pass

    @property
    def flags(self):            # method that gets and displays a list of guessed mine positions (i,j tuples)

        return []

# class for generating the game structure of tiles/mines/numbers
class gameGenerator(ML):
    def __init__(self):

        self.board_width = 0
        self.board_height = 0
        self.clicked_tiles = set()

    def reset(self, config):

        self.board_width = config.board_width
        self.board_height = config.board_height
        self.clicked_tiles.clear()

    def next(self):

        while True:

            i = random.randint(0, self.board_width - 1)   # pseudo-random number generator for rows
            j = random.randint(0, self.board_height - 1)  # pseudo-random number generator for columns
            if (i, j) not in self.clicked_tiles:
                break

        return i, j

    def update(self, result):

        for pos in result.exposed_squares:
            
            self.clicked_tiles.add((pos.x, pos.y))
