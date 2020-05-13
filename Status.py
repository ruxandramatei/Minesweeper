import enum

class Status(enum.Enum):
    '''
    The status of the game
    '''

    QUIT = 1
    DEFEAT = 2
    PLAYING = 3
    VICTORY = 4
