#!/usr/bin/python3


import sys


def is_safe(board, row, col, N):
    """
    Check this row on left side
    """
    for i in range(col):
        if board[row][i] == 1:
            return (False)

    """
    Check upper diagonal on left side
    """
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return (False)

    """
    Check lower diagonal on left side
    """
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return (False)

    return (True)

def solve_n_queens_util(board, col, N, queens, solutions):
    """
    If all queens are placed, append the solution
    """
    if queens == N:
        solution = []
        for i in range(N):
            row_str = ''.join(map(str, board[i]))
            solution.append(row_str)
        solutions.append(solution)
        return (True)

    """
    Consider this column & try placing this queen in 
    all rows one by one
    """
    for i in range(N):
        if is_safe(board, i, col, N):
            """
            Place this queen in board[i][col]
            """
            board[i][col] = 1

            """"
            Recur to place rest of the queens
            """
            solve_n_queens_util(board, col + 1, N, queens + 1, solutions)

            """
            If placing queen in board[i][col] doesn't lead to a 
            solution, then backtrack and remove queen 
            from board[i][col]
            """
            board[i][col] = 0

def solve_n_queens(N):
    """
    Initialize the board
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    """
    Call the recursive utility function to solve the problem
    """
    solve_n_queens_util(board, 0, N, 0, solutions)

    return (solutions)

if __name__ == "__main__":
    """
    Check if the correct number of arguments are provided
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """
    Solve the N queens problem
    """
    solutions = solve_n_queens(N)

    """
    print the solutions
    """
    for solution in solutions:
        for row in solution:
            print(row)
        print()
