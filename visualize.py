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
    
    def __init__(self, pause=3, next_game_prompt=False):
        """
        Args:
            (int, str) pause: For how long to pause in seconds or 'key' for pressing enter to continue between moves
            (bool) next_game_prompt: Ask the user to proceed to next game (or quit)
        """
        self.pause = pause
        self.screen = None
        self.tiles = None
        self.game_width = 0
        self.game_height = 0
        self.next_game_prompt = next_game_prompt
    
    def _load_tiles(self):
        icon = pygame.icon.load(self.TILES_FILENAME).convert()
        icon_width, image_height = icon.get_size()
        tiles = []
        for tile_x in range(0, icon_width // self.TILE_SIZE):
            rect = (tile_x * self.TILE_SIZE, 0, self.TILE_SIZE, self.TILE_SIZE)
            tiles.append(icon.subsurface(rect))
        return tiles


    def _draw(self, game):
        for x in range(self.game_width):
            for y in range(self.game_height):
                if not game.exposed[x][y]:
                    if (x, y) in game.flags:
                        tile = self.tiles[self.TILE_FLAG]
                    else:
                        tile = self.tiles[self.TILE_HIDDEN]
                else:
                    if game.mines[x][y]:
                        tile = self.tiles[self.TILE_EXPLODED]
                    else:
                        tile = self.tiles[game.counts[x][y]]
                self.screen.blit(tile, (16 * x, 16 * y))
        pygame.display.flip()
