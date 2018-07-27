#2048
import numpy as np
import random

board_cols = 4
board_rows = 4
score = 0

board = np.zeros((board_cols,board_rows))

def random_spawn(board):
    rand_col = random.randint(0,board_cols-1)
    rand_row = random.randint(0,board_rows-1)
    while board[rand_col,rand_row] != 0:
        rand_col = random.randint(0,board_cols-1)
        rand_row = random.randint(0,board_rows-1)
    board[rand_col,rand_row] = random.choice([2,2,2,2,2,2,2,2,2,4])


# random_spawn(board)
# print(board)
