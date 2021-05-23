import argparse
from board import Board
from coordinate import Coordinate
import sys
import re 

def parse_arguments():
    my_parser = argparse.ArgumentParser(description='This is a limited chess move validator with support for the Pawn, Bishop and Rook.')
    my_parser.add_argument('move',
                           metavar='Move',
                           type=uci_regex,
                           help='the chess move to validate in UCI format "a1a2"')
    my_parser.add_argument('-s',
                           '--setup',
                           type=setup_regex,
                           default='WRa1,WBc1,WBf1,WRh1,WPa2,WPb2,WPc2,WPd2,WPe2,WPf2,WPg2,WPh2,BPa7,BPb7,BPc7,BPd7,BPe7,BPf7,BPg7,BPh7,BRa8,BBc8,BBf8,BRh8',
                           help='the chess board setup must follow the following format "WPa2,BPa7,WRa1,BRa8,WBc1,BBc8" (default: "WRa1,WBc1,WBf1,WRh1,WPa2,WPb2,WPc2,WPd2,WPe2,WPf2,WPg2,WPh2,BPa7,BPb7,BPc7,BPd7,BPe7,BPf7,BPg7,BPh7,BRa8,BBc8,BBf8,BRh8")')
    my_parser.add_argument('-v',
                           '--verbose',
                           action="store_true",
                           help='increase output verbosity for debugging')
    my_parser.add_argument('-d',
                           '--display',
                           action="store_true",
                           help='prints the current setup of the chess board to the terminal')


    return my_parser.parse_args()

def uci_regex(arg_value, pat=re.compile(r"^[a-h][1-8][a-h][1-8]$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError('move must follow the UCI format')
    return arg_value

def setup_regex(arg_value, pat=re.compile(r"^[BW][PRB][a-h][1-8](,[BW][PRB][a-h][1-8])*$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError('the chess board setup must follow the following format "WPa2,BPa7,WRa1,BRa8,WBc1,BBc8"')
    return arg_value

def main():
    args = parse_arguments()
    verbose = args.verbose
    display = args.display
    board = Board(args.setup)

    if display:
        print(board)

    from_coordinate = Coordinate.create_from_UCI(args.move[0:2])
    to_coordinate = Coordinate.create_from_UCI(args.move[2:4])

    if verbose:
        print({'from_coordinate': from_coordinate, 'to_coordinate': to_coordinate})

    piece = board.get_piece(from_coordinate)
    if piece is None:      
        verdict = {'valid': False, 'message': 'no piece located at from coordinate'}
    else:
        verdict = piece.validate_move(board, from_coordinate, to_coordinate, verbose)

    print(verdict)

    if verdict['valid']:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
