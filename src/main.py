import pygame
import sys

# Initialize Pygame 初始化Pygame
pygame.init()

# Constants 常量定义
SCREEN_SIZE = 300
GRID_SIZE = SCREEN_SIZE // 3
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FONT_SIZE = 36

# Initialize the screen 初始化屏幕
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Tic Tac Toe')

# Font 字体
font = pygame.font.Font(None, FONT_SIZE)

# Draw the grid 绘制棋盘
def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, GRID_SIZE * x), (SCREEN_SIZE, GRID_SIZE * x), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (GRID_SIZE * x, 0), (GRID_SIZE * x, SCREEN_SIZE), LINE_WIDTH)

# Check for a winner 检查获胜者
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return 0

# Draw X and O moves 绘制X和O
def draw_moves(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(screen, RED, (col * GRID_SIZE + 20, row * GRID_SIZE + 20), ((col + 1) * GRID_SIZE - 20, (row + 1) * GRID_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, RED, ((col + 1) * GRID_SIZE - 20, row * GRID_SIZE + 20), (col * GRID_SIZE + 20, (row + 1) * GRID_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLUE, (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2 - 20, LINE_WIDTH)

# Show the start screen 显示开始页面
def show_start_screen():
    screen.fill(WHITE)
    start_text = font.render("Start", True, BLACK)
    screen.blit(start_text, (SCREEN_SIZE // 2 - start_text.get_width() // 2, SCREEN_SIZE // 2 - start_text.get_height() // 2))
    pygame.display.flip()

# Show the end screen 显示结束页面
def show_end_screen(winner):
    screen.fill(WHITE)
    if winner != 0:
        end_text = font.render(f"Player {winner} wins!", True, BLACK)
    else:
        end_text = font.render("Draw!", True, BLACK)
    screen.blit(end_text, (SCREEN_SIZE // 2 - end_text.get_width() // 2, SCREEN_SIZE // 2 - end_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Main game loop 游戏主循环
def game_loop():
    board = [[0] * 3 for _ in range(3)]
    player_turn = 1
    running = True
    winner = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and winner == 0:
                x, y = event.pos
                col = x // GRID_SIZE
                row = y // GRID_SIZE
                if board[row][col] == 0:
                    board[row][col] = player_turn
                    player_turn = 3 - player_turn  # Switch player
                    winner = check_winner(board)

        screen.fill(WHITE)
        draw_grid()
        draw_moves(board)
        pygame.display.flip()

        if winner != 0:
            show_end_screen(winner)
            return

# Main program 主程序
def main():
    start_game = False
    while True:
        if not start_game:
            show_start_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    start_game = True
        else:
            game_loop()
            start_game = False

if __name__ == "__main__":
    main()
