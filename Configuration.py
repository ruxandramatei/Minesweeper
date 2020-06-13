class Configuration:
    '''
    The game configuration

    Attribute:
    (int) board_width - board's width
    (int) board_height - board's height
    (int) number_of_mines - number of mines for the game
    '''
    def __init__(self, board_width=8, board_height=8, number_of_mines=10):
        self.board_width = board_width
        self.board_height = board_height
        self.number_of_mines = number_of_mines

