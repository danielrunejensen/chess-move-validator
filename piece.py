from enum import Enum

class Color(Enum):
    WHITE = 'W'
    BLACK = 'B'

class Type(Enum):
    PAWN = 'P'
    ROOK = 'R'
    BISHOP = 'B'

class Piece:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def __repr__(self) -> str:
        return str({'type': self.type, 'color': self.color})

    def validate_move(self, board, from_coordinate, to_coordinate, verbose):
        verdict = {'move': self.type.value + from_coordinate.getUCI() +
                   '-' + to_coordinate.getUCI(), 'valid': True}
        if board.get_piece(from_coordinate) is not self:
            verdict['message'] = 'from coordinate must refer to the piece found on the board'
            verdict['valid'] = False
            return verdict
        elif from_coordinate == to_coordinate:
            verdict['message'] = 'move to the same square is illegal'
            verdict['valid'] = False
            return verdict

        possible_moves = self.create_possible_moves(from_coordinate, board)
        if verbose is True:
            print('Possible Moves:')
            print(possible_moves)

        if to_coordinate not in possible_moves:
            verdict['message'] = self.get_impossible_move_message()
            verdict['valid'] = False
            return verdict

        if verbose is True:
            print('Investigated path:')
        verdict = self.investigate_path(
            board, from_coordinate, to_coordinate, verdict, verbose)

        return verdict

    def create_directional_coordinates(self, coordinate, create_next_coordinate, x_limit, y_limit):
        coordinates = []

        if coordinate.x == x_limit or coordinate.y == y_limit:
            return coordinates

        current_coordinate = coordinate
        while True:
            current_coordinate = create_next_coordinate(current_coordinate)
            coordinates.append(current_coordinate)

            if current_coordinate.x == x_limit or current_coordinate.y == y_limit:
                break

        return coordinates

    def check_direction(self, board, from_coordinate, to_coordinate, verdict, verbose, create_next_coordinate):
        current_coordinate = from_coordinate
        while True:
            current_coordinate = create_next_coordinate(current_coordinate)
            piece = board.get_piece(current_coordinate)

            if verbose:
                print((current_coordinate, piece))

            if piece is None:
                if current_coordinate == to_coordinate:
                    return verdict
            else:
                return self.check_piece(piece, current_coordinate, to_coordinate, verdict)

    def check_piece(self, piece, piece_coordinate, to_coordinate, verdict):
        if piece_coordinate == to_coordinate and piece.color is not self.color:
            verdict['move'] = verdict['move'].replace('-', 'x')
            verdict['message'] = piece.type.value + \
                piece_coordinate.getUCI() + ' will be captured'
        else:
            verdict['message'] = piece.type.value + \
                piece_coordinate.getUCI() + ' is blocking the path '
            verdict['valid'] = False

        return verdict