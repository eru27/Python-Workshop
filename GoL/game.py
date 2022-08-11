import inout as io
import os
from copy import deepcopy
from time import sleep

START = "start.txt"

MATRIX_SIZE_1 = 20 # 43
MATRIX_SIZE_2 = 20 # 80

i_ADD = [-1, -1, -1, 0, 0, 1, 1, 1]
j_ADD = [-1, 0, 1, -1, 1, -1, 0, 1]

def main():
    global START
    global MATRIX_SIZE_1
    global MATRIX_SIZE_2
    global i_ADD
    global j_ADD

    board = io.load(START, MATRIX_SIZE_1, MATRIX_SIZE_2) # Dodatni redovi za hendlovanje izuzetaka
    board1 = [[0 for j in range(MATRIX_SIZE_2 + 2)] for i in range(MATRIX_SIZE_1 + 2)] # Dodatni redovi za hendlovanje izuzetaka

    io.printBoard(board, MATRIX_SIZE_1, MATRIX_SIZE_2)
    inp = input()

    while not inp == '0':
        for i in range(1, MATRIX_SIZE_1 + 1):
            for j in range(1, MATRIX_SIZE_2 + 1):
                liveCells = 0
                for k in range(8):
                    liveCells += board[i + i_ADD[k]][j + j_ADD[k]]

                if liveCells <= 1 or liveCells >= 4:
                    board1[i][j] = 0
                elif board[i][j] == 1 and liveCells == 2 or liveCells == 3:
                    board1[i][j] = 1
                elif liveCells == 3:
                    board1[i][j] = 1
                else:
                    board1[i][j] = 0
        
        board = deepcopy(board1)
        os.system('cls')
        io.printBoard(board, MATRIX_SIZE_1, MATRIX_SIZE_2)
        #sleep(0.5)
        inp = input()

main()