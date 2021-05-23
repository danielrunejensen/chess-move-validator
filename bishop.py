from coordinate import Coordinate
from piece import Piece, Type


class Bishop(Piece):
    def __init__(self, color):
        super(Bishop, self).__init__(Type.BISHOP, color)

    def create_possible_moves(self, from_coordinate, board):
        moves = []
        moves.extend(self.create_directional_coordinates(
            from_coordinate, Coordinate.create_north_west, 0, 0))
        moves.extend(self.create_directional_coordinates(
            from_coordinate, Coordinate.create_south_west, 0, 7))
        moves.extend(self.create_directional_coordinates(
            from_coordinate,Coordinate.create_north_east, 7, 0))
        moves.extend(self.create_directional_coordinates(
            from_coordinate, Coordinate.create_south_east, 7, 7))
        return moves

    def get_impossible_move_message(self):
        return 'only diagonal moves are allowed'

    def investigate_path(self, board, from_coordinate, to_coordinate, verdict, verbose):
        if from_coordinate.x > to_coordinate.x and from_coordinate.y > to_coordinate.y:
            verdict = self.check_direction(
                board, from_coordinate, to_coordinate, verdict, verbose, Coordinate.create_north_west)
        elif from_coordinate.x < to_coordinate.x and from_coordinate.y < to_coordinate.y:
            verdict = self.check_direction(
                board, from_coordinate, to_coordinate, verdict, verbose, Coordinate.create_south_east)
        elif from_coordinate.x < to_coordinate.x and from_coordinate.y > to_coordinate.y:
            verdict = self.check_direction(
                board, from_coordinate, to_coordinate, verdict, verbose, Coordinate.create_north_east)
        else:
            verdict = self.check_direction(
                board, from_coordinate, to_coordinate, verdict, verbose, Coordinate.create_south_west)

        return verdict
