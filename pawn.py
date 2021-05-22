from coordinate import Coordinate
from piece import Color, Piece, Type


class Pawn(Piece):
    def __init__(self, color):
        super(Pawn, self).__init__(Type.PAWN, color)

    def validate_move(self, board, from_coordinate, to_coordinate, verbose):
        verdict = Piece.validate_move(
            self, board, from_coordinate, to_coordinate, verbose)

        if not verdict['valid']:
            return verdict

        possible_moves = self.create_possible_moves(board, from_coordinate)

        if to_coordinate not in possible_moves:
            verdict['message'] = 'only 1 forward or 1 forward diagonal attack is allowed'
            verdict['valid'] = False
            return verdict
        
        verdict = self.validate_possible_moves( board, from_coordinate, to_coordinate, verdict)

        return verdict

    def create_possible_moves(self, board, from_coordinate):
        moves = []

        if self.color is Color.WHITE:
            moves.append(Coordinate(from_coordinate.x, from_coordinate.y-1))

            left_attack_coordinate = Coordinate(
                from_coordinate.x+1, from_coordinate.y-1)
            piece = board.get_piece(left_attack_coordinate)
            if piece is not None and piece.color is Color.BLACK:
                moves.append(left_attack_coordinate)

            right_attack_coordinate = Coordinate(
                from_coordinate.x-1, from_coordinate.y-1)
            piece = board.get_piece(right_attack_coordinate)
            if piece is not None and piece.color is Color.BLACK:
                moves.append(right_attack_coordinate)
        else:
            moves.append(Coordinate(from_coordinate.x, from_coordinate.y+1))

            left_attack_coordinate = Coordinate(
                from_coordinate.x+1, from_coordinate.y+1)
            piece = board.get_piece(left_attack_coordinate)
            if piece is not None and piece.color is Color.BLACK:
                moves.append(left_attack_coordinate)

            right_attack_coordinate = Coordinate(
                from_coordinate.x-1, from_coordinate.y+1)
            piece = board.get_piece(right_attack_coordinate)
            if piece is not None and piece.color is Color.BLACK:
                moves.append(right_attack_coordinate)

        return moves

    def validate_possible_moves(self, board, from_coordinate, to_coordinate, verdict):
        piece = board.get_piece(to_coordinate)
        if from_coordinate.x == to_coordinate.x:
            if piece is None:
                return verdict
            else:
                verdict['message'] = piece.type.value + \
                    to_coordinate.getUCI() + ' is blocking the path '
                verdict['valid'] = False
        else:
            verdict['move'] = verdict['move'].replace('-', 'x')
            verdict['message'] = piece.type.value + \
                to_coordinate.getUCI() + ' will be captured'
        
        return verdict
