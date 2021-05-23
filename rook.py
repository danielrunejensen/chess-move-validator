from coordinate import Coordinate
from piece import Piece, Type


class Rook(Piece):
    def __init__(self, color):
        super(Rook, self).__init__(Type.ROOK, color)

    def create_possible_moves(self, from_coordinate, board):
        moves = []
        moves.extend(self.create_directional_coordinates(
            from_coordinate, Coordinate.create_north, None, 0))
        moves.extend(self.create_directional_coordinates(
            from_coordinate, Coordinate.create_south, None, 7))
        moves.extend(self.create_directional_coordinates(
            from_coordinate,Coordinate.create_east, 7, None))
        moves.extend(self.create_directional_coordinates(
            from_coordinate, Coordinate.create_west, 0, None))
        return moves

    def get_impossible_move_message(self):
        return 'only vertical or horizontal moves are allowed'

    def investigate_path(self, board, from_coordinate, to_coordinate, verdict, verbose):
        if from_coordinate.y > to_coordinate.y:
            verdict = self.check_direction(
                board, from_coordinate, to_coordinate, verdict, verbose, Coordinate.create_north)
        elif from_coordinate.y < to_coordinate.y:
            verdict = self.check_direction(
                board, from_coordinate, to_coordinate, verdict, verbose, Coordinate.create_south)
        elif from_coordinate.x < to_coordinate.x:
              verdict = self.check_direction(
                board, from_coordinate, to_coordinate, verdict, verbose, Coordinate.create_east)
        else:
              verdict = self.check_direction(
                board, from_coordinate, to_coordinate, verdict, verbose, Coordinate.create_west)
        return verdict