class Sudoku():
    def __init__(self, board):
        self.board = board
    
    def prnt(self):
        for r in range(9):
            if r == 0:
                print("+-------+-------+-------+")
            for c in range(9):
                if c == 0:
                    print("| ", end = "")
                if self.board[r][c] == 0:
                    print("_ ", end = "")
                else:                
                    print(f"{self.board[r][c]} ", end="")
                if c % 3 == 2:
                    print("| ", end = "")
            print("")
            if r % 3 == 2:
                print("+-------+-------+-------+")
        

    def row_check(self, x, r, c):
        for i in range(9):
            if x == self.board[r][i]:
                return False
        return True
        
    def col_check(self, x, r, c):
        for i in range(9):
            if x == self.board[i][c]:
               return False
        return True
    
    def block_check(self, x, r, c):
        r = int(r / 3) * 3
        c = int(c / 3) * 3
        for i in range(r, r+3):
            for j in range(c, c+3):
                if x == self.board[i][j]:
                    return False
        return True
    
    def solver(self, r, c):
        if r == 9:
            return True
        if c == 9:
            return self.solver(r + 1, 0)
        if self.board[r][c] != 0:
            return self.solver(r, c + 1)
        for x in range(1, 10):
            if self.col_check(x, r, c) and self.row_check(x, r, c) and self.block_check(x, r, c):
                self.board[r][c] = x
                if self.solver(r, c + 1):
                    return True
                self.board[r][c] = 0
        return False
    
    @property
    def solve(self):
        return self.solver(0, 0)
             
    
def main():
    ask = input("Welcome User!\nDo you need instructions on how to use this Sudoku Solver?(y/n): ")
    if ask == "y":
        try:
            with open("instructions.txt", "r") as txt:
                for line in txt:
                    print(line, end="")
                ask = input("")
        except FileNotFoundError:
            print("Instruction file not found")
    
    prob = [[0 for _ in range(9)] for _ in range(9)]
    while True:
        puzzle = input("Enter the puzzle: ")
        try:
            if len(puzzle) != 81 or not puzzle.isdigit():
                raise ValueError 
            break
        except ValueError as e:
            print(f"Invalid Input: {e}")
            continue     
    puzzle = list(puzzle)
    for i in range(9):
        for j in range(9):
            prob[i][j] = int(puzzle[i * 9 + j])

    new = Sudoku(prob)
    print("Here is the sudoku puzzle:")
    new.prnt()
    if  not new.solve:
        print("No solution exists for your sudoku puzzle")
    else:
        print("Here is the solved puzzle. Thank You!")
        new.prnt()
        

if __name__ == "__main__":
    main() 