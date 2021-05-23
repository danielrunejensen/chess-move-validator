from coordinate import Coordinate
from bishop import Bishop
from rook import Rook
from pawn import Pawn
from piece import Color, Type


class Board:
    def __init__(self, setup):
            self.layout = self.empty_layout()
            self.setup_board(setup)

    def __repr__(self) -> str:
        representation = ''
        for y in range(0,8):
            representation += Coordinate.y_to_uci_int(y) + '   '
            for x in range(0,8):
                piece = self.get_piece(Coordinate(x, y))
                if piece is None:
                        representation += '   '
                else:
                    representation += piece.get_unicode() + '  '
            representation += '\n'
        representation += '    a  b  c  d  e  f  g  h'
        return str(representation)

    def get_piece(self, coordiate):
        return self.layout[coordiate.y][coordiate.x]

    def set_piece(self, coordiate, piece):
        self.layout[coordiate.y][coordiate.x] = piece

    def empty_layout(self):
        return [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

    def setup_board(self, setup):
        annotations = setup.split(',')

        for annotation in annotations:
            piece = self.create_piece(annotation)
            coordinate = Coordinate.create_from_UCI(annotation[2:4])
            self.set_piece(coordinate, piece)

    def create_piece(self, annotation):
        type = self.get_type(annotation)
        color = self.get_color(annotation)

        if type == Type.PAWN:
            return Pawn(color)        
        elif type == Type.ROOK:
            return Rook(color)
        elif type == Type.BISHOP:
            return Bishop(color)

    def get_color(self, annotation):
        color_value = annotation[0]
        if color_value == Color.WHITE.value:
            return Color.WHITE 
        else:
            return Color.BLACK 
    
    def get_type(self, annotation):
        type_value = annotation[1]
        if type_value == Type.PAWN.value:
            return Type.PAWN
        elif type_value == Type.ROOK.value:
            return Type.ROOK
        else:
            return Type.BISHOP