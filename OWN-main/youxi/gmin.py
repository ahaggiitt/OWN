import pygame
# import random

# 定义游戏屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 定义游戏模式
GAME_MODE = {
    "STANDARD": 0,
    "FIND_THE_DIFFERENCE": 1,
    "QUICK_MATH": 2,
    "ANCIENT_POETRY": 3,
}

# 定义游戏状态
GAME_STATE = {
    "RUNNING": 0,
    "PAUSED": 1,
    "OVER": 2,
}

# 定义游戏数据
game_mode = GAME_MODE["STANDARD"]
game_state = GAME_STATE["RUNNING"]
game_time = 0
best_time = 0

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("游戏")

# 定义游戏对象
class Game():
    def __init__(self):
        self.grid = [[0 for i in range(3)] for j in range(3)]
        self.current_number = 1

    def generate_grid(self):
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = random.randint(1, 9)

    def draw_grid(self):
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, (255, 255, 255), (i * 100, j * 100, 100, 100))
                pygame.draw.text(screen, str(self.grid[i][j]), (i * 100 + 50, j * 100 + 50), (0, 0, 0))

    def check_number(self, number):
        if number == self.current_number:
            self.current_number += 1
            if self.current_number == 10:
                self.game_state = GAME_STATE["OVER"]
        else:
            print("错误！")

# 创建游戏对象
game = Game()

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # 绘制你的游戏板和其他图形
    例如: pygame.draw.rect(screen, BLACK_COLOR, ...)
创建一个图像
face = pygame.Surface((60, 60), flags=pygame.HWSURFACE)
# 填充图像
face.fill(color='pink')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # # 将图像添加到主屏幕上
    # screen.blit(face, (100, 100))
    # # 更新屏幕显示
    # pygame.display.flip()



# # 游戏循环
# while True:
#     # 处理事件
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 if game_state == GAME_STATE["RUNNING"]:
#                     game_state = GAME_STATE["PAUSED"]
#                 else:
#                     game_state = GAME_STATE["RUNNING"]
#
#             if event.key == pygame.K_r:
#                 game.generate_grid()
#                 game.current_number = 1
#                 game_state = GAME_STATE["RUNNING"]
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             i = x // 100
#             j = y // 100
#             game.check_number(game.grid[i][j])
#
#     # 更新游戏状态
#     if game_state == GAME_STATE["RUNNING"]:
#         game_time += 1

    # 绘制游戏画面
    screen.fill((0, 0, 0))
    game.draw_grid()

    # 显示游戏信息
    pygame.draw.text(screen, "游戏模式：" + str(game_mode), (10, 10), (255, 255, 255))
    pygame.draw.text(screen, "游戏时间：" + str(game_time), (10, 30), (255, 255, 255))
    pygame.draw.text(screen, "最好成绩：" + str(best_time), (10, 50), (255, 255, 255))

    # 更新屏幕
    pygame.display.update()




==================================================================
# import pygame
# import random
#
# # 游戏模式
# GAME_MODES = {
#   "标准模式": "standard",
#   "找茬模式": "find_the_difference",
#   "速算模式": "quick_calculation",
#   "古诗模式": "ancient_poetry",
# }
#
# # 游戏难度
# GAME_DIFFICULTIES = {
#   "简单": "easy",
#   "中等": "medium",
#   "困难": "hard",
# }
#
# # 游戏界面
# class Game界面(pygame.sprite.Sprite):
#   def __init__(self, game):
#     super().__init__()
#
#     self.game = game
#
#     # 游戏背景
#     self.background = pygame.image.load("background.png")
#
#     # 游戏标题
#     self.title = pygame.image.load("title.png")
#
#     # 游戏按钮
#     self.buttons = pygame.sprite.Group()
#
#     # 游戏主界面
#     self.main_menu = MainMenu(self)
#     self.buttons.add(self.main_menu)
#
#     # 游戏测试记录界面
#     self.test_records = TestRecords(self)
#     self.buttons.add(self.test_records)
#
#   def update(self):
#     # 更新游戏界面
#     self.screen.blit(self.background, (0, 0))
#     self.screen.blit(self.title, (0, 0))
#
#     # 更新游戏按钮
#     self.buttons.update()
#
# # 游戏主菜单
# class MainMenu(pygame.sprite.Sprite):
#   def __init__(self, game_interface):
#     super().__init__()
#
#     self.game_interface = game_interface
#
#     # 游戏模式按钮
#     self.game_mode_buttons = pygame.sprite.Group()
#     for game_mode in GAME_MODES:
#       button = GameModeButton(self, game_mode)
#       self.game_mode_buttons.add(button)
#
#     # 游戏难度按钮
#     self.game_difficulty_buttons = pygame.sprite.Group()
#     for game_difficulty in GAME_DIFFICULTIES:
#       button = GameDifficultyButton(self, game_difficulty)
#       self.game_difficulty_buttons.add(button)
#
#     # 开始游戏按钮
#     self.start_button = pygame.sprite.Sprite()
#     self.start_button.image = pygame.image.load("start_button.png")
#     self.start_button.rect = self.start_button.image.get_rect()
#     self.start_button.rect.center = (self.game_interface.screen.get_width() // 2, self.game_interface.screen.get_height() // 2)
#
#   def update(self):
#     # 更新游戏模式按钮
#     self.game_mode_buttons.update()
#
#     # 更新游戏难度按钮
#     self.game_difficulty_buttons.update()
#
#     # 更新开始游戏按钮
#     self.screen.blit(self.start_button.image, self.start_button.rect)
#
# # 游戏测试记录界面
# class TestRecords(pygame.sprite.Sprite):
#   def __init__(self, game_interface):
#     super().__init__()
#
#     self.game_interface = game_interface
#
#     # 测试记录列表
#     self.test_records_list = pygame.sprite.Group()
#
#   def update(self):
#     # 更新测试记录列表
#     self.test_records_list.update()
#
# # 游戏模式按钮
# class GameModeButton(pygame.sprite.Sprite):
#   def __init__(self, main_menu, game_mode):
#     super().__init__()
#
#     self.main_menu = main_menu
#     self.game_mode = game_mode
#
#     self.image = pygame.image.load("game_mode_button.png")
#     self.rect = self.image.get_rect()
#     self.rect.center = (self.main_menu.screen.get_width() // 2, self.main_menu.screen.get_height() // 2)
#
#   def update(self):
#     # 更新游戏模式按钮
#     self.screen.blit(self.image, self.rect)
#
# # 游戏难度按钮
# class GameDifficultyButton(pygame.sprite.Sprite):
#   def __init__(self, main_menu, game_difficulty):
#     super().__init__()
