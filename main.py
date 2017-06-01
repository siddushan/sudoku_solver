__author__ = 'Sidd'

sudoku_grid = [
    [4, 0, 0, 0, 0, 0, 8, 0, 5],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 3, 0, 7, 0],
    [5, 0, 0, 2, 0, 0, 0, 0, 0],
    [1, 0, 4, 0, 0, 0, 0, 0, 0]]

"""
sudoku_grid = [
    [0, 1, 2, 0, 0, 0, 8, 0, 5],
    [4, 3, 8, 0, 0, 0, 0, 0, 0],
    [9, 5, 7, 7, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 3, 0, 7, 0],
    [5, 0, 0, 2, 0, 0, 0, 0, 0],
    [1, 0, 4, 0, 0, 0, 0, 0, 0]]
"""

possible_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def check_box(x_val, y_val):
     remove_set = set()
    col = (x_val / 3) * 3
    row = (y_val / 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku_grid[row + i][col + j] != 0:
                remove_set.add(sudoku_grid[row + i][col + j])
    return possible_set - remove_set


def check_row(x_val):
    remove_set = set()
    for elements in sudoku_grid[x_val]:
        if elements != 0:
            remove_set.add(elements)
    return possible_set - remove_set


def check_col(y_val):
    remove_set = set()
    for i in range(9):
        if sudoku_grid[i][y_val] != 0:
            remove_set.add(sudoku_grid[i][y_val])
    return possible_set - remove_set

def is_solved():
    for i in range(9):
        for j in range(9):
            if sudoku_grid[i][j] == 0:
                return False
    return True

def solve():
    i = 0
    j = 0
    solved = False
    possible = list()
    while not solved:
        if sudoku_grid[i][j] == 0:
            print 'i', i
            print 'j', j
            box = check_box(i, j)
            row = check_row(i)
            col = check_col(j)
            if len(list(box & row & col)) == 1:
                sudoku_grid[i][j] = list(box & row & col)[0]
            else:
                sudoku_grid[i][j] = list(box & row & col)
        if i == 8 and j == 8:
            i = 0
            j = 0
        elif j < 8:
            j += 1
        else:
            i += 1
            j = 0
        solved = is_solved()

solve()
print sudoku_grid
