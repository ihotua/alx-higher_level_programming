#!/usr/bin/python3


import sys

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return (False)
    return (True)

def solve_n_queens(n, row, board):
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board)

def print_solution(board):
    for col in board:
        row_str = ['.'] * len(board)
        row_str[col] = 'Q'
        print(' '.join(row_str))
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit((1))
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit((1))
    if n < 4:
        print("N must be at least 4")
        sys.exit((1))
    solve_n_queens(n, 0, [-1]*n)

if __name__ == "__main__":
    main()
