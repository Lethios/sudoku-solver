import math
import sys
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

matrix = np.empty((9, 9), dtype=int)
SUDOKU = str(input())
X = 0
for i in range(0, 9):
    for j in range(0, 9):
        matrix[i, j] = int(SUDOKU[X])
        X += 1

def scan():
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix[i, j] == 0:
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
        is_valid = check(i, position, matrix)

        if is_valid:
            matrix[position[0], position[1]] = i

            if solve():
                return True

            else:
                matrix[position[0], position[1]] = 0

    return False

def display_grid(grid):
    lines = []

    for i, row in enumerate(grid):
        row_str = ""
        for j, cell in enumerate(row):
            val = str(cell) if cell != 0 else " "
            row_str += f" {val} "

            if j in [2, 5]:
                row_str += "|"
        lines.append(row_str)

        if i in [2, 5]:
            lines.append("" + "─" * len(row_str) + "")

    text = Text("\n".join(lines))
    panel = Panel(text, border_style="cyan", padding=(1, 2), expand=False)
    console.print(panel)

if __name__ == "__main__":
    TEST = solve()

    print()
    if TEST:
        console.print("[bold cyan] Solved Sudoku Grid [/bold cyan]")
        display_grid(matrix)
        print()
        sys.exit(0)
    else:
        print("No solutions found.")
        sys.exit(1)
