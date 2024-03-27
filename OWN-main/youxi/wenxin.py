import pygame
import sys
import time




# 初始化pygame
pygame.init()

# 定义颜色
WHITE = (255, 105, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 设置窗口大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# 设置字体
font = pygame.font.Font(None, 36)

# 游戏状态
game_running = True
game_started = False
game_mode = 'standard'  # 可以是 'standard', 'find_differences', 'math', 'poetry' 等
board_size = (3, 3)  # 棋盘大小
current_sequence = []  # 当前游戏序列
history_scores = []  # 历史成绩
best_score = None  # 最佳成绩


# 函数：开始新游戏
def start_new_game():
    global game_started, current_sequence
    game_started = True
    current_sequence = generate_sequence(board_size)
    display_next_number()


# 函数：生成随机序列
def generate_sequence(size):
    # 生成一个随机序列，这里简化处理，仅生成数字
    return [i for i in range(1, size[0] * size[1] + 1)]


# 函数：显示下一个数字提示
def display_next_number():
    global current_sequence
    if current_sequence:
        number = current_sequence.pop(0)
        text = font.render(str(number), True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

    # 函数：检查用户点击


def check_user_click(event):
    pos = event.pos
    # 这里需要实现点击棋盘格子来检查是否正确的逻辑
    # 简化处理，仅检查是否点击了屏幕中心附近
    if SCREEN_WIDTH // 4 < pos[0] < 3 * SCREEN_WIDTH // 4 and SCREEN_HEIGHT // 4 < pos[1] < 3 * SCREEN_HEIGHT // 4:
        return True
    return False


# 游戏主循环
clock = pygame.time.Clock()
start_time = None
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and game_started:
            if check_user_click(event):
                if current_sequence:
                    # 玩家点击正确，显示下一个数字
                    display_next_number()
                else:
                    # 游戏结束，显示成绩
                    end_time = time.time()
                    game_started = False
                    score = end_time - start_time
                    history_scores.append(score)
                    if not best_score or score < best_score:
                        best_score = score
                        # 显示成绩和最佳记录的逻辑需要添加

    if game_started and not start_time:
        start_time = time.time()

        # 填充背景色
    screen.fill(BLACK)

    # 这里添加游戏界面的绘制逻辑，比如菜单、按钮等
    # ...

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)



# 退出pygame
pygame.quit()
sys.exit()



