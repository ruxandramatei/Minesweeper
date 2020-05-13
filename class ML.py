import abc

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


