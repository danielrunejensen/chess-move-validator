class Board:
    def __init__(self, layout):
        self.layout = layout

    def get_piece(self, coordiate):
        return self.layout[coordiate.y][coordiate.x]
