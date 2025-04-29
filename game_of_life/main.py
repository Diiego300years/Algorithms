import random, time, copy, os

class BoardGame:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [
            [
                '#' if random.randint(0,1) == 0 else ' ' for y in range(self.height)
            ]
            for x in range(self.width)
        ]

    
    def get_board(self) -> list[list[str]]:
        return copy.deepcopy(self.board)
    
    def __str__(self) -> str:
        """Query: returns board as string."""
        # odwróć dostęp, bo chcemy rysować wierszami y=0..height-1,
        # a wewnętrznie mamy board[x][y].
        if not self.board:
            return "<empty board>"
    
        lines = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(self.board[x][y])
            lines.append(''.join(row))
        return '\n'.join(lines)
    

class GameOfLife(BoardGame):

    def __init__(self, width: int, height:int):
        super().__init__(width, height)

    def display(self) -> None:
        """Clean screen, and draw board"""
        # choose command in case of different os
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear_cmd)
        print(self)  # __str__ returns actual board
        print("działa?")

    def play(self, delay: int = 1) -> None:
        try:
            while True:
                self.display()
                self.step()
                time.sleep(delay)
        except KeyboardInterrupt:
            return " Bybe bye"



    def step(self) -> None:
        currentBoard = self.get_board()
        
        new = [[' ']*self.height for _ in range(self.width)]

        for x in range(self.width):
            for y in range(self.height):
                # take 8 neighbors
                cnt = 0
                for dx in (-1,0,1):
                    for dy in (-1,0,1):
                        if dx==dy==0: continue
                        nx = (x+dx) % self.width
                        ny = (y+dy) % self.height
                        if currentBoard[nx][ny] == '#':
                            cnt += 1
                if currentBoard[x][y] == '#' and cnt in (2,3):
                    new[x][y] = '#'
                elif currentBoard[x][y] == ' ' and cnt == 3:
                    new[x][y] = '#'
        self.board = new


if __name__ == "__main__":
    game = GameOfLife(20, 60)
    print(game)
    print(game.play())