from termcolor import colored
import os

def load(addrs, mats1, mats2):
    '''
    Ucitava pocetnu tablu iz fajla. Karakter '.' se prepoznaje kao mrtvo polje, a svaki drugi karakter kao zivo polje.

    :addrs: Adresa fajla
    :mats1: Visina matrice
    :mats2: Sirina matrice

    :ret: Vraca matricu dimenzija (mats1 + 2)x(mats2 + 2) sa 1 za ziva polja, a 0 za mrtva. 
    '''
    with open(addrs, 'r') as file:
        matrix = file.readlines()
    matrix1 = []

    for line in matrix:
        matrix1.append(line.split())

    matrix2 = [[0 for j in range(mats2 + 2)] for i in range(mats1 + 2)]
    for i in range(0, mats1):
        for j in range(0, mats2):
            if matrix1[i][j] != '.':
                matrix2[i + 1][j + 1] = 1

    return matrix2

def printBoard(board, mats1, mats2):
    '''
    Stampa trenutno stanje table na konzolu.
    '''
    os.system('color')

    for i in range(1, mats1 - 1):
        for j in range(1, mats2 - 1):
            if board[i][j]:
                print(colored(u'\u25A0', 'yellow'), end = ' ') # BLACK SQUARE in the Geometric Shapes Unicode block.
            else:
                print(colored(u'\u25A0', 'grey'), end = ' ') # BLACK SQUARE in the Geometric Shapes Unicode block.
        print()