'''hello'''
def sudoku_validator(grid):
    """ Return True if grid is a valid Sudoku square, otherwise False."""
    for i in range(9): #i will be your index
        # j, k index top left hand corner of each 3x3 tile
        j = (i // 3) * 3 #the first run will be 0 obvs
        k = (i % 3) * 3

        # Check row, column, and 3x3 subgrid for duplicates
        if (
            len(set(grid[i])) != 9
            or len(set(row[i] for row in grid)) != 9 #
            or len(set(grid[row][col] for row in range(j, j + 3) for col in range(k, k + 3))) != 9
        ):
            return False
    return True
