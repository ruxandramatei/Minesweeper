import abc
import os
import time

# turn off pygame printing a message on import
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'off'
import pygame
import pygame.locals

class Visualizer(abc.ABC):
    '''
    Base class of visualization of the game
    '''
    @abc.abstractmethod
    def run(self, runner):
        '''
        Runner runner - iterator, Runner of the game
        '''
        pass


class PyGameVisualizer(Visualizer):
    '''
    Visualize a minesweeper game with PyGame
    '''
    SIZE_TILE = 16
    COLOR = (189, 189, 189)
    FILENAME_TILES = os.path.join(os.path.dirname(__file__), 'tiles.png')
    HIDDEN_TILE = 9
    EXPLODED_TILE = 10
    BOMB_TILE = 11
    FLAG_TILE = 12
    WINDOW_NAME = 'Minesweeper'