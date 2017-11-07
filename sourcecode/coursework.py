
# Defining board size and colour variables
rows = 10
columns = rows
empty = "·"
black = "@"
white = "O"

# Function to initialise the board
def draw_board():

    # Empty board
    board = [[empty] * columns for i in range(rows)]

    # Populating the board with pieces based on the row and column
    for row in range(0, rows):
        # Black pieces in the first rows/2-1 rows
        if row < rows/2-1:
            if row % 2 == 0:
                for element in range(0, columns):
                    if element % 2 != 0:
                        board[row][element] = black
            else:
                for element in range(0, columns):
                    if element % 2 == 0:
                        board[row][element] = black

        # White pieces in the last rows/2-1 rows
        elif row > rows/2:
            if row % 2 == 0:
                for element in range(0, columns):
                    if element % 2 != 0:
                        board[row][element] = white
            else:
                for element in range(0, columns):
                    if element % 2 == 0:
                        board[row][element] = white

    return board

# Function to print a board
def print_board(board):
    for i in range(ord('A'), ord('A')+rows):
        '''if i < ord('A')+rows-1:
            print(chr(i), end=' ')
        else:
            print(chr(i))'''
        print(chr(i), end=' ')
    print('\n')
    for row in range(0, rows):
        print(' '.join([element for element in board[row]]), " ", row+1)

def main():
    board = draw_board()
    print_board(board)

if __name__ == "__main__":
    main()
