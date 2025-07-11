
import pygame
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)
FPS = 60

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.SysFont("Rubik", 40)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ארבע בשורה - Connect Four")
clock = pygame.time.Clock()

def create_board():
    return np.zeros((BOARD_HEIGHT, BOARD_WIDTH))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[BOARD_HEIGHT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(BOARD_HEIGHT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(BOARD_WIDTH-3):
        for r in range(BOARD_HEIGHT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(BOARD_WIDTH):
        for r in range(BOARD_HEIGHT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(BOARD_WIDTH-3):
        for r in range(BOARD_HEIGHT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(BOARD_WIDTH-3):
        for r in range(3, BOARD_HEIGHT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(BOARD_WIDTH):
        for r in range(BOARD_HEIGHT):
            pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
    
    for c in range(BOARD_WIDTH):
        for r in range(BOARD_HEIGHT):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), HEIGHT-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), HEIGHT-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
    pygame.display.update()

def show_message(message, color):
    text = font.render(message, True, color)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.update()
    pygame.time.wait(3000)

def main():
    board = create_board()
    game_over = False
    turn = 0
    
    draw_board(board)
    pygame.display.update()
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, WIDTH, SQUARE_SIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE/2)), RADIUS)
            pygame.display.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, WIDTH, SQUARE_SIZE))
                
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(posx // SQUARE_SIZE)
                    
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                        
                        if winning_move(board, 1):
                            show_message("שחקן 1 ניצח!", RED)
                            game_over = True
                
                # Ask for Player 2 Input
                else:               
                    posx = event.pos[0]
                    col = int(posx // SQUARE_SIZE)
                    
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)
                        
                        if winning_move(board, 2):
                            show_message("שחקן 2 ניצח!", YELLOW)
                            game_over = True
                
                print_board(board)
                draw_board(board)
                
                turn += 1
                turn = turn % 2
                
                if game_over:
                    pygame.time.wait(3000)
                    board = create_board()
                    game_over = False
                    draw_board(board)
                    turn = 0

if __name__ == "__main__":
    # Define prettier colors
    BG_COLOR = (30, 30, 60)
    BOARD_COLOR = (80, 120, 200)
    PLAYER1_COLOR = (255, 80, 80)
    PLAYER2_COLOR = (255, 220, 90)
    EMPTY_COLOR = (220, 220, 220)

    def draw_board(board, wins1, wins2):
        screen.fill(BG_COLOR)
        # Draw win counters
        win_text = font.render(f"ניצחונות: שחקן 1 - {wins1}   שחקן 2 - {wins2}", True, WHITE)
        screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, 10))
        # Draw board
        for c in range(BOARD_WIDTH):
            for r in range(BOARD_HEIGHT):
                pygame.draw.rect(screen, BOARD_COLOR, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.circle(screen, EMPTY_COLOR, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
        for c in range(BOARD_WIDTH):
            for r in range(BOARD_HEIGHT):      
                if board[r][c] == 1:
                    pygame.draw.circle(screen, PLAYER1_COLOR, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), HEIGHT-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
                elif board[r][c] == 2: 
                    pygame.draw.circle(screen, PLAYER2_COLOR, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), HEIGHT-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
        pygame.display.update()

    def main():
        board = create_board()
        game_over = False
        turn = 0
        wins1 = 0
        wins2 = 0

        draw_board(board, wins1, wins2)
        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BG_COLOR, (0,0, WIDTH, SQUARE_SIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, PLAYER1_COLOR, (posx, int(SQUARE_SIZE/2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, PLAYER2_COLOR, (posx, int(SQUARE_SIZE/2)), RADIUS)
                    pygame.display.update()
                
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    pygame.draw.rect(screen, BG_COLOR, (0,0, WIDTH, SQUARE_SIZE))
                    posx = event.pos[0]
                    col = int(posx // SQUARE_SIZE)
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, turn+1)
                        if winning_move(board, turn+1):
                            if turn == 0:
                                wins1 += 1
                                show_message("שחקן 1 ניצח!", PLAYER1_COLOR)
                            else:
                                wins2 += 1
                                show_message("שחקן 2 ניצח!", PLAYER2_COLOR)
                            game_over = True
                        print_board(board)
                        draw_board(board, wins1, wins2)
                        turn += 1
                        turn = turn % 2
                        pygame.time.wait(2000)  # Wait 2 seconds before next turn
                        if game_over:
                            pygame.time.wait(2000)
                            board = create_board()
                            game_over = False
                            draw_board(board, wins1, wins2)
                            turn = 0

    main()