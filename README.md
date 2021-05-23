# chess-move-validator
This is a limited chess move validator with support only for the Pawn, Bishop and Rook.

## Features
 - Chess board can be setup via the commandline
 - Block detection
 - Capture detection 

## Notes
This program was created and tested with Python 3.9.5 only

## Help
```
python main.py --help
usage: main.py [-h] [-s SETUP] [-v] [-d] Move

This is a limited chess move validator with support for the Pawn, Bishop and Rook.

positional arguments:
  Move                  the chess move to validate in UCI format "a1a2"

optional arguments:
  -h, --help            show this help message and exit
  -s SETUP, --setup SETUP
                        the chess board setup must follow the following format "WPa2,BPa7,WRa1,BRa8,WBc1,BBc8" (default:
                        "WRa1,WBc1,WBf1,WRh1,WPa2,WPb2,WPc2,WPd2,WPe2,WPf2,WPg2,WPh2,BPa7,BPb7,BPc7,BPd7,BPe7,BPf7,BPg7,BPh7,BRa8,BBc8,BBf8,BRh8")
  -v, --verbose         increase output verbosity
  -d, --display         display the board
  ```

## Example usage
Where we would like to validate if it is possible to move a chess piece from a1 to a2 which is described with `a1a2`. We are using the default chess setup and there we are checking if the Rook on a1 can move to a2. It cannot because its path is blocked by the Pawn at a2.
```
python main.py a1a2
{'move': 'Ra1-a2', 'valid': False, 'message': 'Pa2 is blocking the path '}
```

Here is the same command again but this time with the display flag set. It will validate just the same but at the same time it will print a far from perfect chess board representation in yor terminal.

```
python main.py a1a2 --display
8   ♜ ■ ♝ ■ □ ♝ □ ♜
7   ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎ ♟︎
6   □ ■ □ ■ □ ■ □ ■
5   ■ □ ■ □ ■ □ ■ □
4   □ ■ □ ■ □ ■ □ ■
3   ■ □ ■ □ ■ □ ■ □
2   ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
1   ♖ □ ♗ □ ■ ♗ ■ ♖
    a b c d e f g h

{'move': 'Ra1-a2', 'valid': False, 'message': 'Pa2 is blocking the path '}
```

The default chess setup can be changed by giving the optional flag --setup a string with the wanted configuration. This way any chess board configuration can be used and validated against.

```
python main.py a1c1 --display --setup WPa2,BPa7,WRa1,BRa8,WBc1,BBc8
8   ♜ ■ ♝ ■ □ ■ □ ■ 
7   ♟︎ □ ■ □ ■ □ ■ □
6   □ ■ □ ■ □ ■ □ ■
5   ■ □ ■ □ ■ □ ■ □
4   □ ■ □ ■ □ ■ □ ■
3   ■ □ ■ □ ■ □ ■ □
2   ♙ ■ □ ■ □ ■ □ ■
1   ♖ □ ♗ □ ■ □ ■ □
    a b c d e f g h
{'move': 'Ra1-c1', 'valid': False, 'message': 'Bc1 is blocking the path '
```

Verbose output can also be set to see what is going on behind the scenes.

```
python main.py a1h8 --verbose --display --setup WBa1,BBh8
8   □ ■ □ ■ □ ■ □ ♝ 
7   ■ □ ■ □ ■ □ ■ □
6   □ ■ □ ■ □ ■ □ ■
5   ■ □ ■ □ ■ □ ■ □
4   □ ■ □ ■ □ ■ □ ■
3   ■ □ ■ □ ■ □ ■ □
2   □ ■ □ ■ □ ■ □ ■
1   ♗ □ ■ □ ■ □ ■ □
    a b c d e f g h
{'from_coordinate': {'x': 0, 'y': 7, 'UCI': 'a1'}, 'to_coordinate': {'x': 7, 'y': 0, 'UCI': 'h8'}}
Possible Moves:
[{'x': 1, 'y': 6, 'UCI': 'b2'}, {'x': 2, 'y': 5, 'UCI': 'c3'}, {'x': 3, 'y': 4, 'UCI': 'd4'}, {'x': 4, 'y': 3, 'UCI': 'e5'}, {'x': 5, 'y': 2, 'UCI': 'f6'}, {'x': 6, 'y': 1, 'UCI': 'g7'}, {'x': 7, 'y': 0, 'UCI': 'h8'}]
Investigated path:
({'x': 1, 'y': 6, 'UCI': 'b2'}, None)
({'x': 2, 'y': 5, 'UCI': 'c3'}, None)
({'x': 3, 'y': 4, 'UCI': 'd4'}, None)
({'x': 4, 'y': 3, 'UCI': 'e5'}, None)
({'x': 5, 'y': 2, 'UCI': 'f6'}, None)
({'x': 6, 'y': 1, 'UCI': 'g7'}, None)
({'x': 7, 'y': 0, 'UCI': 'h8'}, {'unicode': '♝', 'type': <Type.BISHOP: 'B'>, 'color': <Color.BLACK: 'B'>})
{'move': 'Ba1xh8', 'valid': True, 'message': 'Bh8 will be captured'}
```

Same example as above but with a blocking piece in its way.

```
python main.py a1h8 --verbose --display --setup WBa1,BBh8,WRd4
8   □ ■ □ ■ □ ■ □ ♝ 
7   ■ □ ■ □ ■ □ ■ □
6   □ ■ □ ■ □ ■ □ ■
5   ■ □ ■ □ ■ □ ■ □
4   □ ■ □ ♖ □ ■ □ ■
3   ■ □ ■ □ ■ □ ■ □
2   □ ■ □ ■ □ ■ □ ■
1   ♗ □ ■ □ ■ □ ■ □
    a b c d e f g h
{'from_coordinate': {'x': 0, 'y': 7, 'UCI': 'a1'}, 'to_coordinate': {'x': 7, 'y': 0, 'UCI': 'h8'}}
Possible Moves:
[{'x': 1, 'y': 6, 'UCI': 'b2'}, {'x': 2, 'y': 5, 'UCI': 'c3'}, {'x': 3, 'y': 4, 'UCI': 'd4'}, {'x': 4, 'y': 3, 'UCI': 'e5'}, {'x': 5, 'y': 2, 'UCI': 'f6'}, {'x': 6, 'y': 1, 'UCI': 'g7'}, {'x': 7, 'y': 0, 'UCI': 'h8'}]
Investigated path:
({'x': 1, 'y': 6, 'UCI': 'b2'}, None)
({'x': 2, 'y': 5, 'UCI': 'c3'}, None)
({'x': 3, 'y': 4, 'UCI': 'd4'}, {'unicode': '♖', 'type': <Type.ROOK: 'R'>, 'color': <Color.WHITE: 'W'>})
{'move': 'Ba1-h8', 'valid': False, 'message': 'Rd4 is blocking the path '}
```