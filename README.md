# Connect4-Revamped
Modified Connect-4 game using Pygame library (2 more players Added!)

# Libraries Used
. NumPy - NumPy is a which adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level  mathematical functions to operate on these arrays.
. PyGame - Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
. Math - Math is a built-in module in the Python 3 standard library that provides standard mathematical constants and functions. You can use the math module to perform various mathematical calculations, such as numeric, trigonometric, logarithmic, and exponential calculations.
. Sys - The sys library in Python provides access to information about the Python runtime environment. It also provides functions for interacting with the operating system. For example: sys.exit() for exiting the Python interpreter.

# Methodology
Creating a Connect Four game in Python involves several components, such as the game board, player input, and win condition checking. Here's a simplified algorithm to get you started:
Step 1: Initialize the game board: Create a 6x7 grid (7 rows and 14 columns) to represent the game board. 
	You can use a 2D list to represent the grid, where each cell can be empty, contain a player's token (e.g., 'X' or 'O’), 	or be marked as an invalid move.
Step 2: Create a function to display the game board: This function should display the current state of the game board.
Step 3: Implement player input: Allow two players to take turns. Get the column where the player wants to drop their token. Ensure the selected column is not full.
Step 4: Update the game board: Update the board with the player's token in the selected column.
Step 5: Check for a win condition: After each move, check if the current player has won. Check for horizontal, vertical, and diagonal runs of four tokens.
Step 6: Main game loop: Continue taking turns until a player wins or the board is full (a draw).
Step 7: End the game: Display the result (win, draw), and ask if the players want to play again.

<p align="center">
  <img width="40%" src="instance1.jpg">
 </p>
 
# References
[1] PyGame (2023, October 31). PyGame Documentation. https://www.pygame.org/docs/
[2] NumPy (2023, October 31). NumPy Documentation. https://numpy.org/doc/stable/
[3] Bradley, M., and Hasbro (2023, October 31). Connect Four. Wikipedia. https://en.wikipedia.org/wiki/Connect_Four



