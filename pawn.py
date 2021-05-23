from coordinate import Coordinate
from piece import Color, Piece, Type


class Pawn(Piece):
    def __init__(self, color):
        super(Pawn, self).__init__(Type.PAWN, color)

    def create_possible_moves(self, from_coordinate, board):
        moves = []

        if self.color is Color.WHITE:
            moves.append(Coordinate.create_north(from_coordinate))

            south_west_coordinate = Coordinate.create_north_west(from_coordinate)
            piece = board.get_piece(south_west_coordinate)
            if piece is not None and piece.color is Color.BLACK:
                moves.append(south_west_coordinate)

            south_east_coordinate = Coordinate.create_north_east(from_coordinate)
            piece = board.get_piece(south_east_coordinate)
            if piece is not None and piece.color is Color.BLACK:
                moves.append(south_east_coordinate)
        else:
            moves.append(Coordinate.create_south(from_coordinate))

            south_west_coordinate = Coordinate.create_south_west(from_coordinate)
            piece = board.get_piece(south_west_coordinate)
            if piece is not None and piece.color is Color.WHITE:
                moves.append(south_west_coordinate)

            south_east_coordinate = Coordinate.create_south_east(from_coordinate)
            piece = board.get_piece(south_east_coordinate)
            if piece is not None and piece.color is Color.WHITE:
                moves.append(south_east_coordinate)

        return moves

    def get_impossible_move_message(self):
        return 'only 1 forward or 1 forward diagonal attack is allowed'

    def investigate_path(self, board, from_coordinate, to_coordinate, verdict, verbose):
        piece = board.get_piece(to_coordinate)
        if from_coordinate.x == to_coordinate.x:
            if piece is not None:
                verdict['message'] = piece.type.value + \
                    to_coordinate.getUCI() + ' is blocking the path '
                verdict['valid'] = False
        else:
            verdict['move'] = verdict['move'].replace('-', 'x')
            verdict['message'] = piece.type.value + \
                to_coordinate.getUCI() + ' will be captured'
        
        return verdict

    def get_unicode_white(self):
        return  '♙'

    def get_unicode_black(self):
        return  '♟︎'