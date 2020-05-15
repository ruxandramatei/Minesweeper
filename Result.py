class Result:
    '''
    Results of a square selection

    Attributes:
        (set) exposed_squares - set of squares exposed after selection
        (Status) status - status of the current game
        '''
    def __init__(self, status, exposed_squares=()):
        self.status = status
        self.exposed_squares = set(exposed_squares)
