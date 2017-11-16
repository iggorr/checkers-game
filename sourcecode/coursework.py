import random, time

# Defining board size and piece symbol variables
SIZE = 8
EMPTY = "·"
BLACK = "@"
BLACK_KING = "B"
WHITE = "O"
WHITE_KING = "W"

letter_row = ""
black_count = 0
white_count = 0
current_move = 0

board = []
history = []


# Function to initialise the board
def initialise_board():
    # Updating to a two-dimensional list to store the pieces
    global board
    board = [[EMPTY] * SIZE for i in range(SIZE)]

    # Populating the board with pieces based on the row and column
    for row in range(0, SIZE):
        # Black pieces in the first rows/2-1 rows
        if row < SIZE / 2 - 1:
            populate_row(row, BLACK)
        # White pieces in the last rows/2-1 rows
        elif row > SIZE / 2:
            populate_row(row, WHITE)

    # Populating the letter row
    global letter_row
    for i in range(ord('A'), ord('A') + SIZE):
        letter_row += chr(i)


# Function to add a board representation to the history list
def add_state():
    while len(history) - current_move > 1:
        history.pop()

    history.append([x[:] for x in board])


# Function to replay previous game
def replay():
    # Iterate through each board state stored in history and print it
    for state in history:
        print_board(state)
        time.sleep(1)


# Function to undo a previous move
def undo_move(turn):
    global board
    global current_move
    # Checking that the player is not at the beginning of the game
    if turn == BLACK:
        if current_move == 0:
            print("No moves to undo!")
            return
    else:
        if current_move == 1:
            print("No moves to undo!")
            return

    # Updating the number of the move
    current_move -= 2
    # Setting the current board to a previous state
    board = [x[:] for x in history[current_move]]


# Function to redo move
def redo_move():
    global board
    global current_move
    # Checking that there are moves that can be redone
    if len(history) - current_move >= 3:
        current_move += 2
        board = [x[:] for x in history[current_move]]
    else:
        print("No moves to redo!")


# Function to fill a row with pieces
def populate_row(row, piece):
    # Based on the row, put the pieces into the right cell
    if row % 2 == 0:
        for element in range(0, SIZE):
            if element % 2 != 0:
                board[row][element] = piece
    else:
        for element in range(0, SIZE):
            if element % 2 == 0:
                board[row][element] = piece


# Function to print the board with letter rows and number columns
def print_board(current=[]):
    # Optional argument for when the user is replaying a game, if not passed print the current state of the board
    if current:
        grid = current
    else:
        grid = board

    print('   ', ' '.join(letter_row))
    for row in range(0, SIZE):
        print(row + 1, ' ', ' '.join([element for element in grid[row]]), ' ', row + 1)
    print('   ', ' '.join(letter_row))


# Function for playing an actual game of checkers
def play_game(mode):

    global current_move
    # Always set the first turn to black
    turn = BLACK
    # Add the initial state of the board to move tracking
    add_state()

    # Game loop until one of the sides loses all the pieces
    while black_count > 0 and white_count > 0:
        # Printing the number of pieces for each of the sides
        print("Black: ", black_count, "White: ", white_count)
        # Printing the board
        print_board()

        if turn == BLACK:
            # If mode is Player vs Player, ask for input
            if mode == 1:
                move = input("\nBlack's move: ")

                # Check if attempt to Undo a move
                if move.upper() == 'U':
                    undo_move(turn)
                    continue

                # Check if attempt to Redo a move
                if move.upper() == 'R':
                    redo_move()
                    continue

                # If user's input is invalid, try again
                if not user_move(move, turn):
                    continue
            # If black are played by the computer, generate a move
            else:
                computer_move(turn)
                # time.sleep(1)

            # Saving the current state of the board
            add_state()
            # Incrementing the move counter
            current_move += 1
            # Give the next round to White
            turn = WHITE

        else:
            # If mode is not PC vs PC, ask for input
            if mode != 3:
                move = input("\nWhite's move: ")
                # Check if attempt to Undo a move
                if move.upper() == 'U':
                    undo_move(turn)
                    continue

                # Check if attempt to Redo a move
                if move.upper() == 'R':
                    redo_move()
                    continue

                # If user's input is invalid, try again
                if not user_move(move, turn):
                    continue
            # If white are played by the computer, generate move
            else:
                computer_move(turn)
                # time.sleep(1)

            # Saving the current state of the board
            add_state()
            # Incrementing the move counter
            current_move += 1
            # Give the next round to Black
            turn = BLACK

    # If game reaches an end, announce the winner
    else:
        print("Black: ", black_count, "White: ", white_count)
        print_board()
        if white_count == 0:
            print("Black won!")
        else:
            print("White won!")


# Function to check whether a player has available moves
def moves_available():
    return True


# Function to check and execute user's move
def user_move(move, turn):

    # Checking the length of the string
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

    # Checking whether piece is present on the selected square
    piece = board[first_row][first_column]
    if turn == BLACK:
        if piece != BLACK and piece != BLACK_KING:
            print("Can only move own pieces, please try again!")
            return False
    else:
        if piece != WHITE and piece != WHITE_KING:
            print("Can only move own pieces, please try again!")
            return False

    column_difference = second_column - first_column
    row_difference = second_row - first_row

    # Checking that the piece was moved in the right direction if not a king
    if piece == BLACK:
        if row_difference <= 0:
            print("Black piece must be moved forward, please try again!")
            return False

    elif piece == WHITE:
        if row_difference >= 0:
            print("White piece must be moved by one square forward, please try again!")
            return False

    # Checking that the target square is vacant
    target_square = board[second_row][second_column]
    if target_square != EMPTY:
        print("Target square is occupied, please try again!")
        return False

    # Checking if the target row is a king's row
    if piece == BLACK:
        if second_row == SIZE - 1:
            piece = BLACK_KING
    elif piece == WHITE:
        if second_row == 0:
            piece = WHITE_KING

    # Checking whether the move is a capture attempt
    if abs(column_difference) == 2 and abs(row_difference) == 2:
        piece_to_capture = board[first_row + int(row_difference / 2)][first_column + int(column_difference / 2)]

        # Checking that the piece to be captured is not empty
        if piece_to_capture == EMPTY:
            print("Piece must be moved by one square only, please try again!")
            return False

        # Checking that the piece to be captured in not of the same colour
        if turn == BLACK:
            if piece_to_capture == BLACK or piece_to_capture == BLACK_KING:
                print("Can't jump over own pieces, please try again!")
                return False
        else:
            if piece_to_capture == WHITE or piece_to_capture == WHITE_KING:
                print("Can't jump over own pieces, please try again!")
                return False

        # Proceed with the capture
        board[first_row][first_column] = EMPTY
        board[first_row + int(row_difference / 2)][first_column + int(column_difference / 2)] = EMPTY
        board[second_row][second_column] = piece
        if turn == BLACK:
            global white_count
            white_count -= 1
        else:
            global black_count
            black_count -= 1

    else:
        # If a regular move, check that the piece was moved diagonally by one square
        if abs(column_difference) != 1 or abs(row_difference) != 1:
            print("Piece must be move by one square diagonally, please try again!")
            return False

        board[first_row][first_column] = EMPTY
        board[second_row][second_column] = piece

    return True


# Function to generate a move for the computer
def computer_move(turn):

    # This needs reworked obvy

    while True:
        first_column = chr(random.choice(range(0, SIZE)) + 65)
        first_row = random.choice(range(0, SIZE)) + 1
        second_column = chr(random.choice(range(0, SIZE)) + 65)
        second_row = random.choice(range(0, SIZE)) + 1

        move = "{}{}-{}{}".format(first_column, first_row, second_column, second_row)
        if computer_check(move, turn):
            print(move)
            break
    return


# Function to check and execute computer's move
def computer_check(move, turn):

    first_column = ord(move[0].upper()) - 65
    first_row = int(move[1]) - 1

    if first_row < 9:
        second_column = ord(move[3].upper()) - 65
    else:
        second_column = ord(move[4].upper()) - 65

    if first_row < 9:
        second_row = int(move[4]) - 1
    else:
        second_row = int(move[5]) - 1

    # Checking whether piece is present on the selected square
    piece = board[first_row][first_column]
    if turn == BLACK:
        if piece != BLACK and piece != BLACK_KING:
            return False
    else:
        if piece != WHITE and piece != WHITE_KING:
            return False

    column_difference = second_column - first_column
    row_difference = second_row - first_row

    # Checking that the piece was moved in the right direction if not a king
    if piece == BLACK:
        if row_difference <= 0:
            return False

    elif piece == WHITE:
        if row_difference >= 0:
            return False

    # Checking that the target square is vacant
    target_square = board[second_row][second_column]
    if target_square != EMPTY:
        return False

    # Checking if the target row is a king's row
    if piece == BLACK:
        if second_row == SIZE - 1:
            piece = BLACK_KING
    elif piece == WHITE:
        if second_row == 0:
            piece = WHITE_KING

    # Checking whether the move is a capture attempt
    if abs(column_difference) == 2 and abs(row_difference) == 2:
        piece_to_capture = board[first_row + int(row_difference / 2)][first_column + int(column_difference / 2)]

        # Checking that the piece to be captured is not empty
        if piece_to_capture == EMPTY:
            return False

        # Checking that the piece to be captured in not of the same colour
        if turn == BLACK:
            if piece_to_capture == BLACK or piece_to_capture == BLACK_KING:
                return False
        else:
            if piece_to_capture == WHITE or piece_to_capture == WHITE_KING:
                return False

        # Proceed with the capture
        board[first_row][first_column] = EMPTY
        board[first_row + int(row_difference / 2)][first_column + int(column_difference / 2)] = EMPTY
        board[second_row][second_column] = piece
        if turn == BLACK:
            global white_count
            white_count -= 1
        else:
            global black_count
            black_count -= 1

    else:
        # If a regular move, check that the piece was moved diagonally by one square
        if abs(column_difference) != 1 or abs(row_difference) != 1:
            return False

        board[first_row][first_column] = EMPTY
        board[second_row][second_column] = piece

    return True


def main():
    # Prompting for the size of the board
    while True:
        global SIZE
        SIZE = int(input("Please select board size (even number > 2): "))
        if SIZE % 2 == 0 and SIZE > 2:
            break

    # Setting the piece counters
    global black_count
    black_count = int((SIZE - 2) * 0.25 * SIZE)
    global white_count
    white_count = int((SIZE - 2) * 0.25 * SIZE)

    # Initialise the board
    initialise_board()
    # Prompt the user for game type
    while True:
        try:
            mode = int(input("Player vs Player (1)"
                             "\nPlayer vs PC (2)"
                             "\nPC vs PC (3)"
                             "\nYour Choice: "))
        except ValueError:
            continue

        if mode in range(0, 4):
            break

    if mode in range (1, 3):
        print("\nTo move a piece, specify the starting column + row, "
              "followed by the dash and target column + row"
              "\nE.g. b3-c4\n")
    # Play the game in selected mode
    play_game(mode)

    while (input("Replay game (Y/N)?: ").upper()) == "Y":
        replay()


if __name__ == "__main__":
    main()
