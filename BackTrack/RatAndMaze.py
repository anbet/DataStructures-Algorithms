# Recursion
def solve_maze(maze, x, y, solution, n):
    # Base condition
    if x == n-1 and y == n-1 and maze[x][y] == 1:
        solution[x][y] = 1
        return True

    # Recursion step
    if is_safe(maze, x, y, n):
        solution[x][y] = 1

        # Move in X direction to check if there is a path
        if solve_maze(maze, x+1, y, solution, n):
            return True

        # Move in Y direction to check if there is a path
        if solve_maze(maze, x, y+1, solution, n):
            return True

        # If there is no path then back track to the start of the maze
        maze[x][y] = 0

        return False

    return False

# Check if maze is valid
def is_safe(maze, x, y, n):
    if n>x>=0 and n>y>=0 and maze[x][y] == 1:
        return  True
    return False


# Solution
maze = [[1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [0, 0, 1, 1]]

solution = [[0 for j in range(4)] for i in range(4)]
n = len(maze)

if solve_maze(maze, 0, 0 ,solution, n):
    # Print solution
    for i in solution:
        for j in i:
            print(str(j), ' ', end=' ')
        print(' ')

# Time complexity
# In this problem we may move in X direction or Y direction and in worst case we may iterate through all the rows and column
# And we are only iterating through 0 or 1 time complexity should be 2^n and we do this for both the directions
# 2^n * 2^n = O(2^n^2)

# Space complexity
# Space required for n*n matrics would be
# O(n^2)

