import argparse
from board import Board
from mapper import uci_char_to_x, uci_int_to_y
from coordinate import Coordinate
from rook import Rook
from bishop import Bishop
from pawn import Pawn
from piece import Color
import sys

def parse_arguments():
    my_parser = argparse.ArgumentParser(description='Validates a chess move')
    my_parser.add_argument('Move',
                           metavar='Move',
                           type=str,
                           help='the chess move to validate in UCI format "a1a2"')
    my_parser.add_argument('-f',
                           '--file',
                           help='path to chess board setup file')
    my_parser.add_argument('-v',
                           '--verbose',
                           action="store_true",
                           help='increase output verbosity')

    return my_parser.parse_args()


def main():
    args = parse_arguments()
    verbose = args.verbose
    
    from_coordinate = Coordinate(uci_char_to_x(args.Move[0]), uci_int_to_y(args.Move[1]))
    to_coordinate = Coordinate(uci_char_to_x(args.Move[2]), uci_int_to_y(args.Move[3]))
    # Input validation missing, make sure only a-h and 1-8 is allowed.

    board = Board([
        [Rook(Color.BLACK), None, None, None,
         None, None, None, Rook(Color.BLACK)],
        [Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK),
         Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK)],
        [None, None, None, None, None, None, None, None],
        [None, None, None, Rook(Color.WHITE), None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Rook(Color.BLACK), Rook(Color.BLACK), None, None, None, None, None, None],
        [Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE),
         Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE)],
        [Rook(Color.WHITE), None, Bishop(Color.WHITE), None,
         None, Bishop(Color.WHITE), None, Rook(Color.WHITE)],
    ])

    piece = board.get_piece(from_coordinate)

    if piece is None:      
        verdict = {'message': 'no piece located at from coordinate'}
    else:
        verdict = piece.validate_move(board, from_coordinate, to_coordinate, verbose)

    print(verdict)

    if verdict['valid']:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
