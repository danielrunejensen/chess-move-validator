from enum import Enum, auto

class Color(Enum):
    WHITE = 0
    BLACK = 1

class Type(Enum):
    PAWN = 'P'
    ROOK = 'R'
    BISHOP = 'B'

class Piece:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    
    def validate_move(self, board, from_coordinate, to_coordinate, verbose):
        verdict = {'move': self.type.value + from_coordinate.getUCI() + '-' + to_coordinate.getUCI(), 'valid': True}
        if board.get_piece(from_coordinate) is not self:
            verdict['message'] = 'from coordinate must refer to the piece found on the board'
            verdict['valid'] = False
        elif from_coordinate == to_coordinate:
            verdict['message'] = 'move to the same square is illegal'
            verdict['valid'] = False
        return verdict

    def __repr__(self) -> str:
        return str({'type': self.type, 'color': self.color})

