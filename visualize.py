import abc
import os
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'off'
import pygame
import pygame.locals

class Visualizer(abc.ABC):
    """
    Base class of visualization
    """
    @abc.abstractmethod
    def run(self, runner):
        """
        (Runner) runner - iterator
        """
        pass


class PyGameVisualizer(Visualizer):
    """
    Visualization of the game with PyGame
    """
    SIZE_TILE = 16
    COLOR = (189, 189, 189)
    FILENAME_TILES = os.path.join(os.path.dirname(__file__), 'tiles.png')
    HIDDEN_TILE = 9
    EXPLODED_TILE = 10
    BOMB_TILE = 11
    FLAG_TILE = 12
    WINDOW_NAME = 'Minesweeper'
