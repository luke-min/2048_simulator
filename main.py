# main.py

# importing the utils.py file
import utils

# Driver code
if __name__ == '__main__':
    # start
    board = utils.start_game()

while (True):
    # Take user input
    x = input("Press the command : ")

    # Directions: Up, Down, Left, Right

    # Slide up
    if (x == 'w'):

        # Get new board and current state
        board = utils.slide_up(board)
        status = utils.get_current_state(board)

        # If game not over, add a new two
        if (status == 'GAME NOT OVER'):
            utils.add_new_2(board)

        # else break the loop
        else:
            print(status)
            break

    # Repeat for slide down, left, right

    # Slide down
    elif (x == 's'):
        board = utils.slide_down(board)
        status = utils.get_current_state(board)

        if (status == 'GAME NOT OVER'):
            utils.add_new_2(board)
        else:
            print(status)
            break

    # Slide left
    elif (x == 'a'):
        board = utils.slide_left(board)
        status = utils.get_current_state(board)

        if (status == 'GAME NOT OVER'):
            utils.add_new_2(board)
        else:
            print(status)
            break

    # Slide right
    elif (x == 'd'):
        board = utils.slide_right(board)
        status = utils.get_current_state(board)

        if (status == 'GAME NOT OVER'):
            utils.add_new_2(board)
        else:
            print(status)
            break
    else:
        print("Invalid Key Pressed")

    # print the matrix after each
    # move.
    print(utils.print_board(board))
