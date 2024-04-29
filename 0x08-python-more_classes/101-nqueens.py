#!/usr/bin/python3

from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit((1))

if not argv[1].isdigit():
    print('N must be a number')
    exit((1))

alex = int(argv[1])

if alex < 4:
    print('N must be at least 4')
    exit((1))


def board_column_gen(board=[]):
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(alex):
            board.append([0])
    return board


def add_queen(board, row, col):
    board[row][col] = 1


def new_queen_safe(board, row, col):
    x, y = row, col
    for i in range(1, alex):
        if (y - i) >= 0:
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return (False)
            if board[x][y - i]:
                return (False)
            if (x + i) < alex:
                if board[x + i][y - i]:
                    return (False)
    return (True)


def coordinate_format(alex):
    david = []
    for x, attempt in enumerate(alex):
        david.append([])
        for i, row in enumerate(attempt):
            david[x].append([])
            for j, col in enumerate(row):
                if col:
                    david[x][i].append(i)
                    david[x][i].append(j)
    return david


candidates = []
candidates.append(board_column_gen())

for col in range(alex):
    new_candidates = []
    for matrix in candidates:
        for row in range(alex):
            if new_queen_safe(matrix, row, col):
                temp = [line[:] for line in matrix]
                add_queen(temp, row, col)
                if col < alex - 1:
                    board_column_gen(temp)
                new_candidates.append(temp)
    candidates = new_candidates

for item in coordinate_format(candidates):
    print(item)
