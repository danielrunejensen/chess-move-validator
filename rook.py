from coordinate import Coordinate
from piece import Piece, Type


class Rook(Piece):
    def __init__(self, color):
        super(Rook, self).__init__(Type.ROOK, color)

    def validate_move(self, board, from_coordinate, to_coordinate, verbose):
        verdict = Piece.validate_move(
            self, board, from_coordinate, to_coordinate, verbose)

        if not verdict['valid']:
            return verdict

        possible_moves = self.create_possible_moves(from_coordinate)

        if to_coordinate not in possible_moves:
            verdict['invalid'] = 'only vertical or horizontal moves are allowed'
            verdict['valid'] = False
            return verdict

        verdict = self.validate_possible_moves(
            board, from_coordinate, to_coordinate, verdict, verbose)

        return verdict

    def create_possible_moves(self, from_coordinate):
        moves = []

        for x in range(8):
            if from_coordinate.x is not x:
                moves.append(Coordinate(x, from_coordinate.y))

        for y in range(8):
            if from_coordinate.y is not y:
                moves.append(Coordinate(from_coordinate.x, y))

        return moves

    def validate_possible_moves(self, board, from_coordinate, to_coordinate, verdict, verbose):
        if from_coordinate.x < to_coordinate.x:
            verdict = self.check_range_horizontal(
                board, from_coordinate.x+1, to_coordinate.x+1, to_coordinate, verdict, 1, verbose)
        elif from_coordinate.x > to_coordinate.x:
            verdict = self.check_range_horizontal(
                board, from_coordinate.x-1, to_coordinate.x-1, to_coordinate, verdict, -1, verbose)
        elif from_coordinate.y < to_coordinate.y:
            verdict = self.check_range_vertical(
                board, from_coordinate.y+1, to_coordinate.y+1, to_coordinate, verdict, 1, verbose)
        else:
            verdict = self.check_range_vertical(
                board, from_coordinate.y-1, to_coordinate.y-1, to_coordinate, verdict, -1, verbose)
        return verdict

    def check_range_horizontal(self, board, from_range, to_range, to_coordinate, verdict, step_range, verbose):
        for x in range(from_range, to_range, step_range):
            investigated_coordinate = Coordinate(x, to_coordinate.y)
            piece = board.get_piece(investigated_coordinate)
            if verbose:
                print((investigated_coordinate, piece))
            if piece is None:
                if investigated_coordinate != to_coordinate:
                    continue
            else:
                return self.check_piece(piece, investigated_coordinate, to_coordinate, verdict)

        return verdict

    def check_range_vertical(self, board, from_range, to_range, to_coordinate, verdict, step_range, verbose):
        for y in range(from_range, to_range, step_range):
            investigated_coordinate = Coordinate(to_coordinate.x, y)
            piece = board.get_piece(investigated_coordinate)
            if verbose:
                print((investigated_coordinate, piece))
            if piece is None:
                if investigated_coordinate != to_coordinate:
                    continue
            else:
                return self.check_piece(piece, investigated_coordinate, to_coordinate, verdict)

        return verdict

    def check_piece(self, piece, piece_coordinate, to_coordinate, verdict):
        if piece_coordinate == to_coordinate and piece.color is not self.color:
            verdict['move'] = verdict['move'].replace('-', 'x')
            verdict['message'] = piece.type.value + \
                to_coordinate.getUCI() + ' will be captured'
        else:
            verdict['message'] = piece.type.value + \
                to_coordinate.getUCI() + ' is blocking the path '
            verdict['valid'] = False

        return verdict
