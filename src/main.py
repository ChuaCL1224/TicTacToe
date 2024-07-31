import pygame
import sys

# 初始化Pygame
pygame.init()

# 常量定义
SCREEN_SIZE = 300
GRID_SIZE = SCREEN_SIZE // 3
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 初始化屏幕
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Tic Tac Toe')

# 绘制棋盘
def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, GRID_SIZE * x), (SCREEN_SIZE, GRID_SIZE * x), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (GRID_SIZE * x, 0), (GRID_SIZE * x, SCREEN_SIZE), LINE_WIDTH)

# 检查获胜者
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

# 绘制X和O
def draw_moves(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(screen, RED, (col * GRID_SIZE + 20, row * GRID_SIZE + 20), ((col + 1) * GRID_SIZE - 20, (row + 1) * GRID_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, RED, ((col + 1) * GRID_SIZE - 20, row * GRID_SIZE + 20), (col * GRID_SIZE + 20, (row + 1) * GRID_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLUE, (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2 - 20, LINE_WIDTH)

# 游戏主循环
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
                player_turn = 3 - player_turn  # 切换玩家
                winner = check_winner(board)

    screen.fill(WHITE)
    draw_grid()
    draw_moves(board)
    pygame.display.flip()

    if winner != 0:
        print(f"Player {winner} wins!")
        pygame.time.wait(2000)
        running = False

pygame.quit()
sys.exit()
