# utils.py
import random

def start_game():
    # Initialize empty board
    board = []
    for i in range(4):
        board.append(['.'] * 4)

    # Print controls
    print("Enter commands : ")
    print("'w' : Slide Up")
    print("'s' : Slide Down")
    print("'a' : Slide Left")
    print("'d' : Slide Right")

    add_new_2(board)
    return board

def add_new_2(board):
    # Randomly generate row and column
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while (board[r][c] != '.'):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    # Place the piece at the randomly generated
    # new position
    board[r][c] = '2'

def get_current_state(board):
    # If any cell has 2048, win
    for i in range(4):
        for j in range(4):
            if (board[i][j] == '2048'):
                return 'WON'

    # Any empty cells left?
    for i in range(4):
        for j in range(4):
            if (board[i][j] == '.'):
                return 'GAME NOT OVER'

    # No empty cells, but can be merged
    for i in range(3):
        for j in range(3):
            if (board[i][j] == board[i + 1][j] or board[i][j] == board[i][j + 1]):
                return 'BOARD FULL!'

    # No empty cells, but can be merged
    for j in range(3):
        if (board[3][j] == board[3][j + 1]):
            return 'BOARD FULL!'

    # No empty cells, but can be merged
    for i in range(3):
        if (board[i][3] == board[i + 1][3]):
            return 'BOARD FULL!'

    # Otherwise lost
    return 'LOST'


# Helper functions

# Passing board as list of lists within functions.
# print_board() converts it to a single string
def print_board(board):
    output = ""
    for i, row in enumerate(board):
        output += ",".join(row)
        if i < len(board)-1:
            output += "\n"
    return output

'''
Two functions compress and merge are based on
the slide_left() action.

The slide_up slide_down slide_right functions
are in turn based on the slide_left function
'''

def compress(board):
    new_board = [['.'] * 4 for _ in range(4)]

    for i in range(4):
        # New pos for each row
        pos = 0
        for j in range(4):
            if board[i][j] != '.':
                new_board[i][pos] = board[i][j]
                pos += 1
    return new_board

def merge(board):

    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1] and board[i][j] != '.':
                board[i][j] = str(int(board[i][j])+int(board[i][j+1]))
                board[i][j+1] = '.'

    return board

'''
slide_left() function is the main implementation
- compress
- merge
- compress again
'''

def slide_left(board):
    return compress(merge(compress(board)))

'''
Implement helpers to get right up and down
'''

def reverse(board):
    # For each row, reverse the order
    new_board = [[0]*4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            new_board[i][j] = board[i][3-j]

    return new_board

def transpose(board):
    # swap row and column indices
    new_board = [[0]*4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            new_board[i][j] = board[j][i]

    return new_board

def slide_right(board):
    return reverse(slide_left(reverse(board)))

def slide_up(board):
    return transpose(slide_left(transpose(board)))

def slide_down(board):
    return transpose(slide_right(transpose(board)))


