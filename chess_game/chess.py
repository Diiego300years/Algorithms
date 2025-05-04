from typing import NamedTuple
from pprint import pprint


# white ASCII counters below
#♚♛♜♝♞♟


class ChessBoard:
    """
        Class which should handle all stuff with board.
    """
    def __init__(self):
        self.position_x_y: tuple[str, int] = ()
        self.board = self._create_board()
        self.counter_handler = CounterHandler(self)

        

    def _create_board(self) -> list[list[str]]:
        """
            Create board with ⬜⬛ and counters.

            return: list of list with strings as chessboard.
        """
        chess_board = []
        count_loop: int = 9

        for x in range(9):
            count_loop -= 1
            if x != 8:
                chess_board.append([])
            else:
                continue
               # ⬛⬜

            for y in range(9):
                if y == 8:
                    chess_board[x].append(count_loop)
                    if x+1 == 8:
                        chess_board.append(['A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H '])
                    break

                if  count_loop % 2 == 0:
                    if y == 0 or y % 2 == 0:
                        chess_board[x].append('⬜')
                    else:
                        chess_board[x].append('⬛')
                else:
                    if y == 0 or y % 2 == 0:
                        chess_board[x].append('⬛')
                    else:
                        chess_board[x].append('⬜')
        
        return chess_board
    

    def add_counter(self, pawn: str, row: int, col: int) -> None:
        self.board[row][col] = pawn
        

class CounterHandler:

    def __init__(self, board: ChessBoard):
        self.board = board
        self.living_counters = []	
        self.bcounters = [' ♖', ' ♘',  ' ♗', ' ♕',	' ♔', ' ♗', ' ♘', ' ♖']
        self.wcounters = [' ♜', ' ♞', ' ♝', ' ♛',' ♚',' ♝',' ♞', ' ♜']


        self._init_counters()
    
    def _init_counters(self):

        for col in range(8):
            bpawn = '♟️'
            wpawn = ' ♟'
            self.living_counters.append(bpawn)
            self.living_counters.append(wpawn)
            self.board.add_counter(bpawn, 1, col)
            self.board.add_counter(wpawn, 6, col)
            self.living_counters.append(self.bcounters[col])
            self.board.add_counter(self.bcounters[col], 0, col)
            self.living_counters.append(self.wcounters[col])
            self.board.add_counter(self.wcounters[col], 7, col)

    


cb = ChessBoard()

ch = CounterHandler(cb)
pprint(ch.board.board)

# pprint(f'co {cb._create_board()}')

# print(ord('a'))
# print(ord('b'))

# for i in range(97, 105):
    # print(ord(i))

# abcdefgh

