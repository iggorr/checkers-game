
# Defining board size and colour variables
SIZE = 8
EMPTY = "·"
BLACK = "@"
WHITE = "O"

letter_row = ""

# Function to initialise the board
def initialise_board():

    # Empty board
    board = [[EMPTY] * SIZE for i in range(SIZE)]

    # Populating the board with pieces based on the row and column
    for row in range(0, SIZE):
        # Black pieces in the first rows/2-1 rows
        if row < SIZE/2-1:
            populate_row(board, row, BLACK)
        # White pieces in the last rows/2-1 rows
        elif row > SIZE/2:
            populate_row(board, row, WHITE)

    global letter_row
    for i in range(ord('A'), ord('A')+SIZE):
        letter_row += chr(i)

    return board

def populate_row(board, row, piece):
    if row % 2 == 0:
        for element in range(0, SIZE):
            if element % 2 != 0:
                board[row][element] = piece
    else:
        for element in range(0, SIZE):
            if element % 2 == 0:
                board[row][element] = piece

# Function to print a board
def print_board(board):

    print('   ', ' '.join(letter_row))
    for row in range(0, SIZE):
        print(row+1, ' ', ' '.join([element for element in board[row]]), ' ', row+1)
    print('   ', ' '.join(letter_row))

def check_move(move):
    if len(move) > 7:
        print("Move description too long, please try again!")
        return False

    if len(move) < 5:
        print("Move description too short, please try again!")
        return False

    first_column = ord(move[0].upper())-65
    if first_column not in range(0, SIZE):
        print("Wrong first letter, please try again!")
        return False

    try:
        first_row = int(move[1])
    except ValueError:
        print("Wrong first number, please try again!")
        return False

    if move[2] != '-':
        if first_row == 1:
            try:
                first_row = int(move[1:3])
                if first_row > SIZE:
                    print("Number limit exceeded, please try again!")
                    return False
                # stop here...
            except ValueError:
                print("Dash symbol not found, please try again!")
                return False
        else:
            print("Dash symbol not found, please try again!")
            return False

    return True

def play_players():
    turn = BLACK
    while turn == BLACK:
        move = input("\nBlack's move: ")
        if check_move(move):
            turn = BLACK
    else:
        move = input("\nWhite's move: ")

def main():
    board = initialise_board()
    print_board(board)
    play_players()

if __name__ == "__main__":
    main()
