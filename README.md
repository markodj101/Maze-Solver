# Maze Solver

This project implements a maze generator and solver using the Tkinter library in Python. It visually creates a maze and then demonstrates the solving process.

## Features

- **Maze Generation:** Generates a random maze using a recursive backtracking algorithm.
- **Visual Representation:** Displays the maze graphically using Tkinter.
- **Maze Solving:** Implements a recursive backtracking algorithm to find a path through the maze.
- **Animated Solving:** Visualizes the solving process by drawing the path in red and backtracking in grey.
- **Customizable Maze Size:** Allows you to easily change the number of rows and columns in the maze.

## Dependencies

- **Python 3** 
- **Tkinter** 

## Installation

Python 3 and Tkinter library need to be installed to run this project.

## Usage

1.  Save the provided code into the following files:

    - `main.py`
    - `line.py`
    - `cell.py`
    - `maze.py`

2.  Open a terminal or command prompt.

3.  Navigate to the directory where you saved the files.

4.  Run the `main.py` script using the command:

    ```bash
    python main.py
    ```

5.  A window will appear displaying the generated maze, and the solver will automatically start finding the path. The solution path will be highlighted in red.

## Code Structure

The project is organized into the following files:

- **`main.py`:** This is the main entry point of the application. It initializes the Tkinter window, creates a `Maze` object, triggers the maze generation and solving, and keeps the window open until it is closed.
- **`line.py`:** Defines the `Point` and `Line` classes. These classes are used to represent lines on the canvas for drawing the maze walls.
- **`cell.py`:** Defines the `Cell` class. Each cell in the maze is an instance of this class. It keeps track of the cell's boundaries (walls) and whether it has been visited during maze generation or solving. It also handles drawing the cell and the movement path.
- **`maze.py`:** Defines the `Maze` class. This class is responsible for:
  - Creating a grid of `Cell` objects.
  - Randomly breaking down walls between cells to generate the maze using a recursive backtracking algorithm (`_break_walls_r`).
  - Drawing the maze on the screen.
  - Solving the maze using another recursive backtracking algorithm (`_solver_r`).
  - Animating the solving process.

## Customization

You can easily customize the maze by modifying the following parameters in the `main.py` file:

- **`screen_x` and `screen_y`:** Control the width and height of the application window.
- **`x1` and `y1`:** Determine the starting position (top-left corner) of the maze within the window.
- **`num_rows` and `num_cols`:** Set the number of rows and columns in the maze, which directly affects its size and complexity.
- **`cell_size_x` and `cell_size_y`:** Calculate the size of each cell based on the window dimensions and the number of rows and columns.

You can also adjust the animation speed in the `maze.py` file by changing the `time.sleep()` value in the `_animate()` method.

