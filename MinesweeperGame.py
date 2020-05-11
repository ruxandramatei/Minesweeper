import random
import copy
import itertools
import logging

# from Result import *

class MinesweeperGame:
    """
        Attribute:
            (int) board_width - gives the width of the board
            
        Attribute:
            (int) board_height (int) - gives the height of the board
            
                
        Attribute:
            (int) number_of_moves - gives the number of moves made by the player
        
        Attribute:
            ((boolean) list) exposed_squares - bidimensional list of booleans indicating exposed squares
          
        Attribute:
            (int) number_of_mines - gives the number of mines on the board
        
        Attribute:
            ((boolean) list) mines_locations - bidimensional list of booleans indicating mine locations
        
        Attribute:
            ((int) list) neighboring_mine_counts - bidimensional list of integer counts of neighboring mines for squares
            
        
    """
    

    def __init__(self, game_design, mines_positions = None):
        
        """
        Parameter:
            (GameConfig) game_design - gives the  aspect of the game
            
        Optional parameter:
            (list(boolean)) mines_positions - gives the mines positions
        """
        
        # set the dimensions of the board
        self.board_width = game_design.board_width
        self.board_height = game_design.board_height
        
        # set the number of player's moves
        self.number_of_moves = 0
        
        # init the exposed squares bidimensional list
        self.exposed_squares = [[False for y in range(self.board_height)] for x in range(self.board_width)]
        
        # set the number of mines
        self.number_of_mines = game_design.number_of_mines
        
        # init the positions of the mines
        if mines_positions:
            self.mines_locations = copy.deepcopy(mines_positions)
        else:
            self.mines_locations = [[False for y in range(self.board_height)] for x in range(self.board_width)]
            self._place_mines_random() # place the mines on the board randomly
        
        # init the counter of the neighboring mines
        self.neighboring_mine_counts = [[0 for y in range(self.board_height)] for x in range(self.board_width)]
        
        
        # set instance attributes
        
        # set the number of exposed squares
        self._number_of_exposed_squares = 0
        
        # set the explosion flag on false 
        self._explosion = False
        
        # set the quit flag on false
        self._quit = False
        
        # set the number of safe squares
        self._number_of_safe_squares = self.board_width * self.board_height - self.number_of_mines
        
        # init the flag dictionary
        self._flags = {}
        
        # init the neighboring_mine_counts()
        self._init_neighboring_counts()
        
        logger.info("Minesweeper was initialized")
        
        
    def _place_mines_random(self):
        
        locations = list()
        
        while (len(locations) < self.number_of_mines):
            
            x = random.randint(0, self.board_width - 1) 
            y = random.randint(0, self.board_height - 1)
            
            locations.append((x, y))
            
        for location in locations:
            posX = location[0]
            posY = location[1]
            self.mines_locations[posX][posY] = True
            
            
    def _init_neighboring_counts(self):
        """
            Calculates how many neighboring squares have mines for all squares
        """
        for x, y in itertools.product(range(self.board_width), range(self.board_height)):
            
            for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
                
                if dx == 0 and dy == 0: # the square(x, y) location
                    continue
                
                next_x, next_y = x + dx, y + dy
                # check if the neighbor is on the board
                if self._is_inside_the_board(next_x, next_y):
                    self.neighboring_mine_counts[x][y] += self.number_of_mines[next_x][next_y]
                    
                    
    def _is_inside_the_board(self, x, y):
        if x < 0 or x >= self.board_width or y < 0 or y >= self.board_height:
            return False
        return True
