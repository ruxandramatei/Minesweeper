class Square:
    '''
    Informations about the square

    (int) x - x position
    (int) y - y position
    (int) number_of_mines - Number of mines in neighboring squares

    '''
    def __init__(self, x, y, number_of_mines):
        self.x = x
        self.y = y
        self.number_of_mines = number_of_mines

    def __eq__(self, oth):
        if isinstance(oth, self.__class__):
            return self.number_of_mines == oth.number_of_mines and self.x == oth.x and self.y == oth.y
        return

    def __hash__(self):
        return hash((self.x, self.y, self.number_of_mines))

