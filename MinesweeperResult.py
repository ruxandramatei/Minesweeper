class MinesweeperResult:
    '''
    Results of a minesweeper game

    Attributes:
    (bool) result - the results of the game, if the player won or lost
    (int) number_of_moves - the number of moves in a game
    '''
    def __init__(self, result, number_of_moves):
        self.result = result
        self.number_of_moves = number_of_moves
