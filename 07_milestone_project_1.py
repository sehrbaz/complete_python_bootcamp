"""Tic Tac Toe game.

This is a Tic Tac Toe game written by Farid (@sehrbaz) as part of
Complete Python Bootcamp.
This is my first written program except some scriipts written during my
devops times and functions that I have wrtitten to solve coding bat problems.
http://www.zfarid.com
All my codes are available here: https://github.com/sehrbaz

Follow me here: https://twitter.com/sehrbaz

"""

stop = False

# Win and/or tie status at the start of the game
win = False
tie = False

# Tic tac toe board
board = [" ", " ", " ", " ", "_", "_", "_", "_", "_", "_"]

# hint board
hb = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def print_l(b):
    """Function for printing the board representation and hint board."""
    print("_" + b[7] + "_" + "|" + "_" + b[8] + "_" + "|" + "_" + b[9] + "_")
    print("_" + b[4] + "_" + "|" + "_" + b[5] + "_" + "|" + "_" + b[6] + "_")
    print(" " + b[1] + " " + "|" + " " + b[2] + " " + "|" + " " + b[3] + " ")


def reset_game():
    """Function to reset game."""
    global stop, win, tie, board
    stop = False
    win = False
    tie = False
    board = [" ", " ", " ", " ", "_", "_", "_", "_", "_", "_"]


def check_win(w):
    """Function to check if game is won."""
    global win
    if (w[7] == w[5] == w[3] or w[1] == w[5] == w[9] or w[7] == w[4] == w[1] or
            w[7] == w[4] == w[1] or w[8] == w[5] == w[2] or
            w[1] == w[2] == w[3] != ' ' or w[4] == w[5] == w[6] != '_' or
            w[8] == w[7] == w[9] != '_'):
        win = True
        print("Game is won!")


def check_tie(t):
    """Function to check if game is tie(draw)."""
    global tie
    if board.count('X') + board.count('O') == 9 and not win:
        tie = True
        print("The game is tie!")
    return tie


def moving_p(p):
    """Function for moving for both players."""
    global board
    valid = False
    print("Hint Board: ")
    print_l(hb)
    print()
    print()
    while not valid:
        try:
            move = input(
                'Player %s please select your move by selecting number: '
                % (p))
            move = int(move)
            if move >= 1 and move <= 9 and board[move] not in("X", "O"):
                board[move] = p
                print_l(board)
                print()
                print()
                break
            else:
                print('Wrong Move try again')
        except Exception:
            print(move + " is not a valid move! Please try again.\n")


# The real game starts here. :)
while not stop:
    reset_game()
    print()
    print('New Game started:')
    print_l(board)
    while not win or not tie:
        moving_p("X")
        check_win(board)
        check_tie(board)
        if tie or win:
            break
        moving_p('O')
        check_win(board)
        check_tie(board)
        if tie or win:
            break
    retry = input('"q" to quit, any other input will start a new game: ')
    if retry == 'q':
        stop = True
        break
    else:
        continue
