class Configuration:
    '''
    The game configuration

    Attribute:
    (int) board_width - board's width
    (int) board_height - board's height
    (int) number_of_mines - number of mines for the game
    '''
    def __init__(self, board_width=16, board_height=16, number_of_mines=40):
        
        self.number_of_mines = number_of_mines
        self.board_height = board_height
        self.board_width = board_width

