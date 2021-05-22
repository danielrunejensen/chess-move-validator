from mapper import x_to_uci_char, y_to_uci_int


class Coordinate():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self) -> str:
        return str({'x': self.x, 'y': self.y, 'UCI': self.getUCI()})

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def getUCI(self):
        return str(x_to_uci_char(self.x) + y_to_uci_int(self.y))