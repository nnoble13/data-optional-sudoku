# pylint: disable=missing-docstring


# def sudoku_validator(grid):
#     counter = 0
#     for row in grid[counter]:
#         if sorted(row) == [1,2,3,4,5,6,7,8,9]:
#             counter += 1
#     if counter > 8:
#         print("Rows are okay")


def check_sudoku(grid):
    """ Return True if grid is a valid Sudoku square, otherwise False. """
    for i in range(9):
        # j, k index top left hand corner of each 3x3 tile
        j, k = (i // 3) * 3, (i % 3) * 3
        if len(set(grid[i,:])) != 9 or len(set(grid[:,i])) != 9 or len(set(grid[j:j+3, k:k+3].ravel())) != 9:
            return False
    return True

'''https://scipython.com/book/chapter-6-numpy/examples/checking-a-sudoku-grid-for-validity/'''
