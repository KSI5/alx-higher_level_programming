import sys

def is_safe(board, row, col):
    # Check if it is safe to place a queen at the given position
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
    # Check if there is a queen in the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    # Check if there is a queen in the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True

def solve_nqueens(N):
    # Initialize an empty chessboard
    board = [-1] * N
    solutions = []

    def backtrack(row):
        # Base case: All queens have been placed
        if row == N:
            solution = []
            for i in range(N):
                col = board[i]
                row_str = "." * col + "Q" + "." * (N - col - 1)
                solution.append(row_str)
            solutions.append(solution)
            return
        
        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    # Start backtracking from the first row
    backtrack(0)

    return solutions

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is a valid value
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem and print the solutions
    solutions = solve_nqueens(N)
    for solution in solutions:
        for row in solution:
            print(row)
        print()
