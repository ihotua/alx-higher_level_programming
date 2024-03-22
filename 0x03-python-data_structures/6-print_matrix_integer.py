#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in range(len(matrix)):
        for mun in range(len(matrix[num])):
            if mun != 0:
                print(" ", end="")
            print("{:d}".format(matrix[num][mun]), end="")
        print()
