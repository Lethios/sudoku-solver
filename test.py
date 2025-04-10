import math
import numpy as np

matrix = "THIS IS A TEST SUDOKU MATRIX"
matrix_copy = matrix

def scan():
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix_copy[i, j] == 0:
                position = (i, j)
                return position 
    
    return None

def check(num, position, sudoku_grid):
    x = position[0]
    y = position[1]
    
    for a in range(0, 9):
        if sudoku_grid[x, a] == num:
            return False
            
    for a in range(0, 9):
        if sudoku_grid[a, y] == num:
            return False
    
    tl_x = math.floor(x / 3) * 3
    tl_y = math.floor(y / 3) * 3
    
    for i in range(tl_x, tl_x + 3):
        for j in range(tl_y, tl_y + 3):
            if sudoku_grid[i, j] == num:
                return False
                
    return True
    
def solve():
    position = scan()
    
    if position is None:
        return True
    
    for i in range(1, 10):
        is_valid = check(i, position, matrix_copy)
        
        if is_valid:
            matrix_copy[position[0], position[1]] = num
            solve()
            
            
            
            
            
            
            
            
