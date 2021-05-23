# chess-move-validator

```
python main.py a1c1 -h
usage: main.py [-h] [-s SETUP] [-v] [-d] Move

Validates a chess move

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