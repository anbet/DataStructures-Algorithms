global path_x, path_y, n
path_x = [2, 1, -1, -2, -2, -1, 1, 2]
path_y = [1, 2, 2, 1, -1, -2, -2, -1]
n = 8

def knight_tour(board, row, col, step):
    # Base step
    if step ==  n**2:
        return True
    # Recursive step
    for index in range(n):
        new_row = row + path_x[index]
        new_col = col + path_y[index]

        if is_safe(board, new_row, new_col):
            board[new_row][new_col] = step
            if knight_tour(board, new_row, new_col, step+1):
                return True
            # Back track step and assign the current row col to -1
            board[new_row][new_col] = -1
    return False

def is_safe(board, row, col):
    if 0 <= row < n and 0 <= col < n and board[row][col] == -1:
        return True
    return False

board = [[-1 for i in range(n)] for i in range(n)]
board[0][0] = 0
step =1

if knight_tour(board, 0, 0, 1):
    for i in range(n):
        for j in range(n):
            print(board[i][j], ' ', end=' ')
        print(' ')
else:
    print("solution does not exists")