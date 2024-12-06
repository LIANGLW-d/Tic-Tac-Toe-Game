class Board:
    def __init__(self):
        # Represent the board as a list of lists, each cell initially empty
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        # Print the board with lines and separators
        for i, row in enumerate(self.grid):
            print(" | ".join(row))
            if i < 2:
                print("---------")

    def is_cell_empty(self, row, col):
        return self.grid[row][col] == ' '

    def place_mark(self, row, col, mark):
        self.grid[row][col] = mark

    def check_win(self, mark):
        # Check all rows
        for row in self.grid:
            if all(cell == mark for cell in row):
                return True
        # Check all columns
        for col in range(3):
            if all(self.grid[row][col] == mark for row in range(3)):
                return True
        # Check diagonals
        if all(self.grid[i][i] == mark for i in range(3)):
            return True
        if all(self.grid[i][2 - i] == mark for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_move(self):
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row,col): ")
                row, col = move.split(',')
                row, col = int(row), int(col)
                if row in range(3) and col in range(3):
                    if self.board.is_cell_empty(row, col):
                        return row, col
                    else:
                        print("That cell is not empty. Try again.")
                else:
                    print("Invalid input. Row and column must be between 0 and 2.")
            except ValueError:
                print("Invalid format. Please enter in the form row,col (e.g., 0,1).")

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.board.display()

        while True:
            # Get player move
            row, col = self.get_move()
            self.board.place_mark(row, col, self.current_player)
            self.board.display()

            # Check win
            if self.board.check_win(self.current_player):
                print(f"Player {self.current_player} wins!")
                break

            # Check draw
            if self.board.is_full():
                print("It's a draw!")
                break

            # Switch player and continue
            self.switch_player()


if __name__ == "__main__":
    game = Game()
    game.play()
