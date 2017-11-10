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
        if row < SIZE / 2 - 1:
            populate_row(board, row, BLACK)
        # White pieces in the last rows/2-1 rows
        elif row > SIZE / 2:
            populate_row(board, row, WHITE)

    global letter_row
    for i in range(ord('A'), ord('A') + SIZE):
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
        print(row + 1, ' ', ' '.join([element for element in board[row]]), ' ', row + 1)
    print('   ', ' '.join(letter_row))


def play_players(board):
    turn = BLACK
    while turn == BLACK:
        print_board(board)
        move = input("\nBlack's move: ")
        if make_move(board, move, turn):
            turn = WHITE
    else:
        print_board(board)
        move = input("\nWhite's move: ")
        if make_move(board, move, turn):
            turn = BLACK


def make_move(board, move, piece):

    # Checking the length of the move
    if len(move) > 7:
        print("Move description too long, please try again!")
        return False
    if len(move) < 5:
        print("Move description too short, please try again!")
        return False

    # Checking the first column of the move
    first_column = ord(move[0].upper()) - 65
    if first_column not in range(0, SIZE):
        print("Wrong first column, please try again!")
        return False

    # Checking the first row of the move
    try:
        first_row = int(move[1]) - 1
        if first_row < 0:
            print("Row must be 1-9, please try again!")
            return False
    except ValueError:
        print("Wrong first row, please try again!")
        return False

    # Checking for the dash symbol
    if move[2] == '-':
        expected_dash = move[2]
    elif first_row == 0:
        try:
            first_row = int(move[1:3]) - 1
            if first_row > SIZE:
                print("Number limit exceeded, please try again!")
                return False
            expected_dash = move[3]
        except ValueError:
            expected_dash = ''
    else:
        expected_dash = ''
    if expected_dash != '-':
        print("Dash symbol not found, please try again!")
        return False

    # Checking the second column of the move
    if first_row < 9:
        second_column = ord(move[3].upper()) - 65
    else:
        second_column = ord(move[4].upper()) - 65
    if second_column not in range(0, SIZE):
        print("Wrong second column, please try again!")
        return False

    # Checking the second row of the move
    if first_row < 9:
        try:
            second_row = int(move[4]) - 1
            if second_row < 0:
                print("Row must be 1-9, please try again!")
                return False
        except ValueError:
            print("Wrong second row, please try again!")
            return False
    else:
        try:
            second_row = int(move[5]) - 1
            if second_row < 0:
                print("Row must be 1-9, please try again!")
                return False
        except ValueError:
            print("Wrong second row, please try again!")
            return False

    # Checking whether piece is present
    if board[first_row][first_column] != piece:
        print("Piece not found, please try again!")
        return False

    # Checking that the piece was moved diagonally, by one square
    column_difference = second_column - first_column
    if column_difference != 1 and column_difference != -1:
        print("Piece must be move by one square diagonally, please try again!")
        return False

    # Checking that the piece was moved in the right direction
    if piece == BLACK:
        if second_row - first_row != 1:
            print("Black piece must be moved by one square forward, please try again!")
            return False

    else:
        if second_row - first_row != -1:
            print("White piece must be moved by one square forward, please try again!")
            return False

    board[first_row][first_column] = EMPTY
    board[second_row][second_column] = piece

    return True


def main():
    board = initialise_board()
    play_players(board)


if __name__ == "__main__":
    main()
