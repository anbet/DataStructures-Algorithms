# Problem Statement:
# you are given n * m size matrics with zeros, in each column of the matrics we need to place queen in such a way that
# they do not conflict with each other

def save_queens(board, col, size):
    # Base case
    if col >= size:
        return True

    # Loop over the row
    for i in range(size):
        # Check if its safe to place a queen in the column
        if is_safe(board, i, col, size):
            # Place the queen
            board[i][col] = 1

            if save_queens(board, col + 1, size):
                return True

            # Back Track, revert our decision
            board[i][col] = 0

    # If nothing works out then return false
    return False

def is_safe(board, row, col, size):
    # No queens should be present horizontally
    # Row will remain the same but we check up till present column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if queen is present in cross direction
    # Here we check if the queen is present in the left only as we place queen in each column from left side

    # Check the upper half
    # For upper half, we need to decrease row by one and  column by one
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for upper half
    # For the upper half row should increase and row should decrease column
    for i,j in zip(range(row, size, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]
         ]

size = len(board)

if not save_queens(board, 0, size):
    print("solution does not exists")
else:
    for i in board:
        for j in i:
            print(j, ' ', end=' ')
        print(' ')

