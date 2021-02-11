# Sudoku is a number-placement puzzle. 
# The objective is to fill a 9 × 9 grid with numbers in such a way that each column, 
# each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to 
# the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

# Example

# For

# grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
#         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
#         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
# the output should be
# sudoku2(grid) = true;

# For

# grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
#         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
#         ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
#         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
#         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
#         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
#         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
#         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
# the output should be
# sudoku2(grid) = false.

# The given grid is not correct because there are two 1s in the second column. 
# Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.


# Input/Output

# -[execution time limit] 4 seconds (py3)

# -[input] array.array.char grid
# A 9 × 9 array of characters, in which each character is either a digit from '1' to '9' or a period '.'.

# -[output] boolean
# Return true if grid represents a valid Sudoku puzzle, otherwise return false.

import itertools
def sudoku(grid):
    size = len(grid)
    for i in range(size):
        #Check row
        row = [element for element in grid[i] if element.isdigit()]
        if len(row) != len(set(row)):
            return False
        #Check column
        columna = [column[i] for column in grid if column[i].isdigit()]
        if len(columna) != len(set(columna)):
            return False
    #Check 3x3
    for i in range(0,9,3):
        for j in range(0,9,3):
            sub_3 = [
                element for element in itertools.chain(grid[i][j:j+3],grid[i+1][j:j+3],grid[i+2][j:j+3]) if element.isdigit()
            ]
            if len(sub_3) != len(set(sub_3)):
                return False
                
    return True
# Should return True


def sudoku2(grid):
    rows = grid
    cols = zip(*grid)
    subs = []
    
    for i in range(0,7,3):
        for j in range(0,7,3):
            subs.append([grid[r][c] for r in range(i,i+3) for c in range(j,j+3)])
    
    def isvalid(arr):
        nums = [x for x in arr if str.isdigit(x)]
        return len(nums) == len(set(nums))
    
    return all([
        all(map(isvalid, rows)),
        all(map(isvalid, cols)),
        all(map(isvalid, subs))
    ]


# #True
# grid = [[".", ".", ".", "1", "4", ".", ".", "2", "."],
#         [".", ".", "6", ".", ".", ".", ".", ".", "."],
#         [".", ".", ".", ".", ".", ".", ".", ".", "."],
#         [".", ".", "1", ".", ".", ".", ".", ".", "."],
#         [".", "6", "7", ".", ".", ".", ".", ".", "9"],
#         [".", ".", ".", ".", ".", ".", "8", "1", "."],
#         [".", "3", ".", ".", ".", ".", ".", ".", "6"],
#         [".", ".", ".", ".", ".", "7", ".", ".", "."],
#         [".", ".", ".", "5", ".", ".", ".", "7", "."]]

# #False
# grid2 = [[".", "4", ".", ".", ".", ".", ".", ".", "."],
#         [".", ".", "4", ".", ".", ".", ".", ".", "."],
#         [".", ".", ".", "1", ".", ".", "7", ".", "."],
#         [".", ".", ".", ".", ".", ".", ".", ".", "."],
#         [".", ".", ".", "3", ".", ".", ".", "6", "."],
#         [".", ".", ".", ".", ".", "6", ".", "9", "."],
#         [".", ".", ".", ".", "1", ".", ".", ".", "."],
#         [".", ".", ".", ".", ".", ".", "2", ".", "."],
#         [".", ".", ".", "8", ".", ".", ".", ".", "."]]



