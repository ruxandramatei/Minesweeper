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
    SIZE_TILE = 32
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
            self.game_tiles = None
            self.table_width = 0
            self.table_height = 0
            self.next_game_prompt = next_game_prompt

    def run(self, runner):

        pygame.init()
        pygame.display.set_caption(self.WINDOW_NAME)

        # get the board info of the game
        game = runner.game

        self.table_width = game.board_width
        self.table_height = game.board_height
        
        # give the dimensions in pixels of the screen
        screen_pixels_width = self.SIZE_TILE * self.table_width
        screen_pixels_height = self.SIZE_TILE * self.table_height

        # create the screen
        self.screen = pygame.display.set_mode((screen_pixels_width, screen_pixels_height))
        # give the screen a background color
        self.screen.fill(self.COLOR)

        # load the tiles
        self.game_tiles = self._load_tiles()

        next(runner) # move
        self._draw(game) # update the screen


        if isinstance(self.pause, str):

            print("Move")

            pygame.event.clear()

            while not game.game_over:

                event = pygame.event.wait()

                if event.type == pygame.locals.KEYDOWN:

                    next(runner) # move
                    self._draw(game) # update the board

                elif event.type == pygame.locals.QUIT:

                    game.quit()
                    break
        else:

            while not game.game_over:

                time.sleep(self.pause) # wait for a move

                next(runner) # get the status

                self._draw(game) # update the board

        if self.next_game_prompt: # game paused

            print("Press any key to continue...")

            while True: # render

                event = pygame.event.wait() # wait for an event

                if event.type in [pygame.locals.KEYDOWN, pygame.locals.QUIT]: # resolve that event

                    break

        pygame.quit() # quit the game

    def _load_tiles(self):
        icon = pygame.image.load(self.FILENAME_TILES).convert()
        icon_width, image_height = icon.get_size()
        tiles = []
        for tile_x in range(0, icon_width // self.SIZE_TILE):
            rect = (tile_x * self.SIZE_TILE, 0, self.SIZE_TILE, self.SIZE_TILE)
            tiles.append(icon.subsurface(rect))
        return tiles

    def _draw(self, game):
        for x in range(self.table_width):
            for y in range(self.table_height):
                if not game.exposed_squares[x][y]:
                    if (x, y) in game.flags:
                        tile = self.game_tiles[self.FLAG_TILE]
                    else:
                        tile = self.game_tiles[self.HIDDEN_TILE]
                else:
                    if game.mines_positions[x][y]:
                        tile = self.game_tiles[self.EXPLODED_TILE]
                    else:
                        tile = self.game_tiles[game.neighboring_mine_counts[x][y]]
                self.screen.blit(tile, (32 * x, 32 * y))
        pygame.display.flip()
