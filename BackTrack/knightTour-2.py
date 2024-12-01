# Global variables for board size and possible knight movements
global path_x, path_y, n
path_x = [2, 1, -1, -2, -2, -1, 1, 2]  # Possible moves in x-direction
path_y = [1, 2, 2, 1, -1, -2, -2, -1]  # Possible moves in y-direction
n = 8  # Size of the chessboard (8x8 for a standard board)


def knight_tour_optimized(board, row, col, step):
    """
    Tries to perform a Knight's Tour using Warnsdorff's Rule.

    Parameters:
    board (list of lists): The chessboard
    row (int): Current row position of the knight
    col (int): Current column position of the knight
    step (int): Current step count in the tour

    Returns:
    bool: True if the tour is completed, False otherwise
    """
    # Base case: if all squares are visited, return True
    if step == n ** 2:
        return True

    # Determine move order based on Warnsdorff's rule
    move_indices = sorted(range(n), key=lambda i: count_onward_moves(board, row + path_x[i], col + path_y[i]))

    # Try moves according to the prioritized list
    for index in move_indices:
        row_new = row + path_x[index]
        col_new = col + path_y[index]

        # Check if the new move is valid
        if move_is_valid(board, row_new, col_new):
            board[row_new][col_new] = step  # Mark the move
            # Recursively try from the new position
            if knight_tour_optimized(board, row_new, col_new, step + 1):
                return True
            board[row_new][col_new] = -1  # Backtrack if not successful

    # Return False if no valid moves lead to a solution
    return False


def move_is_valid(board, row, col):
    """
    Validates if a knight move is within bounds and to an unvisited square.

    Parameters:
    board (list of lists): The chessboard
    row (int): Row to check
    col (int): Column to check

    Returns:
    bool: True if valid, False otherwise
    """
    return 0 <= row < n and 0 <= col < n and board[row][col] == -1


def count_onward_moves(board, row, col):
    """
    Counts the number of valid onward moves from a given position.

    Parameters:
    board (list of lists): The chessboard
    row (int): Row to evaluate from
    col (int): Column to evaluate from

    Returns:
    int: Number of valid onward moves
    """
    count = 0
    # Check all possible moves for validity
    for i in range(n):
        if move_is_valid(board, row + path_x[i], col + path_y[i]):
            count += 1
    return count


# Initialize the 8x8 chessboard with all squares unvisited (-1)
board = [[-1 for i in range(n)] for i in range(n)]

# Start the tour from the top-left corner (0,0)
board[0][0] = 0  # First step

step = 1  # Initialize the step count

# Attempt to solve the Knight's Tour problem
if knight_tour_optimized(board, 0, 0, step):
    # If successful, print the board with steps
    for row in board:
        print(' '.join(f"{cell:2}" for cell in row))
else:
    # If not, inform the user
    print('Solution does not exist!')
