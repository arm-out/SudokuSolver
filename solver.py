# Filename: solver.py
# Description: Solves a sudoku puzzle given as a 2D array using a backtracking
#              algorithm

board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

# Prints the board


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            # Prints horizontal spacers
            print("- - - - - - - - - - -")

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                # Prints vertical spacers
                print("| ", end="")

            # Prints digits
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Backtracking algorithm basics:
# 1. Pick empty square
# 2. Try all numbers
# 3. Find one that works
# 4. Repeat
# 5. If solution cannot be completed: backtrack

# Returns a touple denoting the empty space on the board
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)   # (row, col)

    return None

# Checks if the current board is valid


def isValid(board, num, pos):
    # Checks for valid row
    for i in range(len(board[0])):
        # num already exists in the row
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Checks for valid column
    for i in range(len(board)):
        # num already exists in column
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # Checks 3x3 square
    x_box = pos[1] // 3
    y_box = pos[0] // 3

    for i in range(y_box * 3, y_box * 3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            # num already exists in box
            if board[i][j] == num and (i, j) != pos:
                return False

    # Board is valid
    return True

# Recursively solves the board using the backtracking algorithm


def solve(board):
    # Base case: board is not empty
    empty = findEmpty(board)
    if not empty:
        return True
    # Recursive step
    else:
        row, col = empty

    # Tries each digit 1-9 in the empty space
    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


# printBoard(board)
# solve(board)
# print(" ")
# print(" ")
# printBoard(board)
