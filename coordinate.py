class Coordinate():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self) -> str:
        return str({'x': self.x, 'y': self.y, 'UCI': self.getUCI()})

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def getUCI(self):
        return str(Coordinate.x_to_uci_char(self.x) + Coordinate.y_to_uci_int(self.y))
    
    def create_from_UCI(uci):
        return Coordinate(Coordinate.uci_char_to_x(uci[0]), Coordinate.uci_int_to_y(uci[1]))

    def create_north(coordinate):
        return Coordinate(coordinate.x, coordinate.y-1)

    def create_south(coordinate):
        return Coordinate(coordinate.x, coordinate.y+1)

    def create_east(coordinate):
        return Coordinate(coordinate.x+1, coordinate.y)

    def create_west(coordinate):
        return Coordinate(coordinate.x-1, coordinate.y)

    def create_north_west(coordinate):
        return Coordinate(coordinate.x-1, coordinate.y-1)

    def create_south_west(coordinate):
        return Coordinate(coordinate.x-1, coordinate.y+1)

    def create_north_east(coordinate):
        return Coordinate(coordinate.x+1, coordinate.y-1)

    def create_south_east(coordinate):
        return Coordinate(coordinate.x+1, coordinate.y+1)

    def uci_char_to_x(uci_char):
        if(uci_char == 'a'):
            return 0
        elif(uci_char == 'b'):
            return 1
        elif(uci_char == 'c'):
            return 2
        elif(uci_char == 'd'):
            return 3
        elif(uci_char == 'e'):
            return 4
        elif(uci_char == 'f'):
            return 5
        elif(uci_char == 'g'):
            return 6
        elif(uci_char == 'h'):
            return 7
        else:
            return '#'

    def x_to_uci_char(x):
        if(x == 0):
            return 'a'
        elif(x == 1):
            return 'b'
        elif(x == 2):
            return 'c'
        elif(x == 3):
            return 'd'
        elif(x == 4):
            return 'e'
        elif(x == 5):
            return 'f'
        elif(x == 6):
            return 'g'
        elif(x == 7):
            return 'h'
        else:
            return '#'

    def uci_int_to_y(uci_int):
        y = int(uci_int)
        if(y == 8):
            return 0
        elif(y == 7):
            return 1
        elif(y == 6):
            return 2
        elif(y == 5):
            return 3
        elif(y == 4):
            return 4
        elif(y == 3):
            return 5
        elif(y == 2):
            return 6
        elif(y == 1):
            return 7
        else:
            return '#'

    def y_to_uci_int(y):
        if(y == 0):
            return str(8)
        elif(y == 1):
            return str(7)
        elif(y == 2):
            return str(6)
        elif(y == 3):
            return str(5)
        elif(y == 4):
            return str(4)
        elif(y == 5):
            return str(3)
        elif(y == 6):
            return str(2)
        elif(y == 7):
            return str(1)
        else:
            return '#'
