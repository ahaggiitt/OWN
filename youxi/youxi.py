import pygame  # 导入pygame库


# 初始化pygame
pygame.init()

# 设置窗口的大小
screen_width, screen_height = 800, 600

# 创建窗口
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题
pygame.display.set_caption("我的游戏")


# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



EMPTY = 0
BLACK = 1
WHITE = 2
BLACK_COLOR = [0, 0, 0]
WHITE_COLOR = [255, 255, 255]
BOARD_SIZE = 15
GRID_SIZE = 40


# 五子棋棋盘类
class RenjuBoard:
    def __init__(self):
        self._board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    # 重置棋盘
    def reset(self):
        for row in range(BOARD_SIZE):
            self._board[row] = [EMPTY] * BOARD_SIZE

# 下棋
    def move(self, row, col, is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False

# 绘制棋盘与棋子
    def draw(self, screen):
        # 画棋盘线
        for h in range(1, BOARD_SIZE + 1):
            pygame.draw.line(screen, BLACK_COLOR, [GRID_SIZE, h * GRID_SIZE], [BOARD_SIZE * GRID_SIZE, h * GRID_SIZE], 1)
            pygame.draw.line(screen, BLACK_COLOR, [h * GRID_SIZE, GRID_SIZE], [h * GRID_SIZE, BOARD_SIZE * GRID_SIZE], 1)


# 画外框
        pygame.draw.rect(screen, BLACK_COLOR, [GRID_SIZE - BORDER_WIDTH, GRID_SIZE - BORDER_WIDTH, (BOARD_SIZE + 1) * GRID_SIZE, (BOARD_SIZE + 1) * GRID_SIZE], BORDER_WIDTH)

# 画棋盘特殊点位
        pygame.draw.circle(screen, BLACK_COLOR, [GRID_SIZE * 8, GRID_SIZE * 8], 5, 0)  # 天元点
        for x in [GRID_SIZE * 4, GRID_SIZE * 12]:
            for y in [GRID_SIZE * 4, GRID_SIZE * 12]:
                pygame.draw.circle(screen, BLACK_COLOR, [x, y], 3, 0)

# 画棋子
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self._board[row][col] != EMPTY:
                    color = BLACK_COLOR if self._board[row][col] == BLACK else WHITE_COLOR
                    pos = [GRID_SIZE * (col + 1), GRID_SIZE * (row + 1)]
                    pygame.draw.circle(screen, color, pos, 18, 0)

# 定义函数，传入当前棋盘上的棋子列表，输出结果，不管黑棋白棋胜，都是传回False，未出结果则为True
def is_win(board):
    for n in range(15):
        # 判断垂直方向胜利
        flag = 0
        # flag是一个标签，表示是否有连续以上五个相同颜色的棋子
        for b in board._board:
            if b[n] == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜')
                    return False
            else:
                # else表示此时没有连续相同的棋子，标签flag重置为0
                flag = 0

        flag = 0
        for b in board._board:
            if b[n] == 2:
                flag += 1
                if flag == 5:
                    print('白棋胜')
                    return False
            else:
                flag = 0

        # 判断水平方向胜利
        flag = 0
        for b in board._board[n]:
            if b == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜')
                    return False
            else:
                flag = 0

        flag = 0
        for b in board._board[n]:
            if b == 2:
                flag += 1
                if flag == 5:
                    print('白棋胜')
                    return False
            else:
                flag = 0

        # 判断正斜方向胜利

        for x in range(4, 25):
            flag = 0
            for i,b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 1:
                    flag += 1
                    if flag == 5:
                        print('黑棋胜')
                        return False
                else:
                    flag = 0

        for x in range(4, 25):
            flag = 0
            for i,b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 2:
                    flag += 1
                    if flag == 5:
                        print('白棋胜')
                        return False
                else:
                    flag = 0

        #判断反斜方向胜利
        for x in range(11, -11, -1):
            flag = 0
            for i,b in enumerate(board._board):
                if 0 <= x + i <= 14 and b[x + i] == 1:
                    flag += 1
                    if flag == 5:
                        print('黑棋胜')
                        return False
                else:
                    flag = 0

        for x in range(11, -11, -1):
            flag = 0
            for i,b in enumerate(board._board):
                if 0 <= x + i <= 14 and b[x + i] == 2:
                    flag += 1
                    if flag == 5:
                        print('白棋胜')
                        return False
                else:
                    flag = 0
    return True


