from typing import NamedTuple
from pprint import pprint


class ChessBoard:
    def __init__(self):
        self.position_x_y: tuple[str, int] = ()
        self.board = []
        pass

    def create_board(self):

        # count_loop = 96
        count_loop = 9
        for x in range(9):
            count_loop -= 1
            if x != 8:
                self.board.append([])
            else:
                continue
               # ⬛⬜

            for y in range(9):
                if y == 8:
                    self.board[x].append(count_loop)
                    if x+1 == 8:
                        self.board.append(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
                    break

                if  count_loop % 2 == 0:
                    if y == 0 or y % 2 == 0:
                        self.board[x].append('⬜')
                    else:
                        self.board[x].append('⬛')
        
        return self.board
    

    def add_counters(self):
        # pawns are 
        pass
    

    


cb = ChessBoard()

pprint(cb.create_board())

# print(ord('a'))
# print(ord('b'))

# for i in range(97, 105):
    # print(ord(i))

# abcdefgh

