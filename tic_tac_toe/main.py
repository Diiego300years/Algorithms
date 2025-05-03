from typing import NamedTuple

# I should prepare kind of board for game.
type Pointer = list[int,int]
type GameBoard = list[list]

class BoardTic:
    pointer: Pointer
    board: GameBoard

    def __init__(self) -> None:
        self.pointer: Pointer = [] 
        self.board: GameBoard = []
        self.x_turn: bool = True
    
    def choose_point(self):
        x = self.pointer[0]
        y = self.pointer[1]
        if self.x_turn:
            self.board[x][y] = 'X'
        else:
            self.board[x][y] = 'O'

    def create_board(self):
        for x in range(3):
            self.board.append([])
            for y in range(3):
                self.board[x].append([])

    def show_board(self):
        # return self.board
        lines: list[str] = []
        for i, row in enumerate(self.board, start=1):
            lines.append(str(row))
            if i % 3 == 0:
                lines.append("")    # pusta linia jako oddzielacz
        return "\n".join(lines)




class GamePlay(BoardTic):
    def __init__(self):
        super().__init__()
        self.play_now: bool = True
        

    def play(self):
        self.create_board()
        while self.play_now:
            ask_player = input("Choose number from 1-6 as your choice")

            if self.x_turn:
                if int(ask_player) == 1:
                    self.pointer = [0,0]
                    self.choose_point()
                    print(self.show_board())
                    print('naura')
                    
                elif int(ask_player) == 2:
                    self.pointer = [0,1]
                    self.choose_point()
                    print(self.show_board())
                    print('paaa')
                    continue

    def reset(self):
        pass
    

# bt = BoardTic()
# bt.create_board()
# print(bt.show_board())
gp = GamePlay()

gp.play()