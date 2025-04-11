# Sudoku Solver

A Python-based command-line Sudoku solver that uses backtracking to solve any valid 9x9 Sudoku puzzle. The puzzle is input as a single 81-digit string, and the solution is displayed in a stylized grid using the `rich` library.

## Features
- Solves any valid 9x9 Sudoku puzzle.
- Uses a recursive backtracking algorithm.
- Displays the solution in a neatly formatted `rich` grid.
- Minimal dependencies

## Installation
1. **Ensure Python is installed (Python 3.x recommended).**
2. Clone the repository and install the dependencies:
  ```bash
  git clone https://github.com/Lethios/sudoku-solver.git
  cd sudoku-solver
  ```
  ```bash
  pip install -r requirements.txt
  ```

## Usage
1. Run the solver:
   ```bash
   python sudoku-solver.py
   ```
2. Provide the Sudoku puzzle as a single string of 81 digits where 0 represents an empty cell:
   ```bash
   530070000600195000098000060800060003400803001700020006060000280000419005000080079
   ```

## Author
**Lethios**
- Github: [@Lethios](https://github.com/Lethios)
- Twitter: [@LethiosDev](https://x.com/LethiosDev)

## License
Copyright © 2025 [Lethios](https://github.com/Lethios).  
This project is licensed under the [MIT License](LICENSE).
