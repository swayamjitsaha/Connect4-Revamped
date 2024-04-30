import numpy as np
import pygame
import sys
import math

# DEFINING THE COLOURS IN TERMS OF RGB VALUES
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

# DECLARING DIMENSIONS OF THE CONNECT 4 BOARD MATRIX
ROW_COUNT = 7
COLUMN_COUNT = 14
count = 0
## Some issues : Match does not register, Green colour vanishes

# FUNCTION - CREATE BOARD
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

# FUNCTION TO DROP A SINGLE DISC PIECE
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# FUNCTION TO CHECK IF LOCATION VALID
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

# FUNCTION TO CHECK THE NEXT LOCATION IS OPEN OR NOT
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# FUNCTION TO PRINT THE BOARD ON EXECUTION
def print_board(board):
    print(np.flip(board, 0))

# FUNCTION TO CHECK WHETHER THERE IS A MATCH HORIZONTALLY/ VERTICALLY/ DIAGONALLY
def winning_move(board, piece, count):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                count = count + 1
                return [count, True]

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                count = count + 1
                return [count, True]

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                count = count + 1
                return [count, True]

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                count = count + 1
                return [count, True]

# FUNCTION TO DRAW BOARD
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, PURPLE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 3:
                pygame.draw.circle(screen, GREEN, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 4:
                pygame.draw.circle(screen, BLUE, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


if __name__ == '__main__':
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 50

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("bitstreamverasans", 50)  # monospace
    #count = 0
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                elif turn == 1:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                elif turn == 2:
                    pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE / 2)), RADIUS)
                elif turn == 3:
                    pygame.draw.circle(screen, BLUE, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                        drop_piece(board, row, col, 2)
                        drop_piece(board, row, col, 3)
                        drop_piece(board, row, col, 4)
                        if winning_move(board, 1, count):
                            #label = myfont.render("Total no. of matches: ", 1, RED)
                            #screen.blit(label, (40, 10))
                            count += 1
                            #print(count)
                            game_over = True


                pygame.display.update()

                print_board(board)
                draw_board(board)

                if turn <= 3:
                    turn += 1

                if turn == 4:
                    turn = 0
                # turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)
