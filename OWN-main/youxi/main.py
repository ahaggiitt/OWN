# import pygame  # 导入pygame库
#
# pygame.init()  # pygame组件初始化
# pygame.display.set_caption("测试窗口")  # 设置窗口名称
# height = 600  # 窗口高度变量
# width = 400  # 窗口宽度变量
# # 将设置窗口大小赋值给screen是方便以后贴图粘贴的方便
# screen = pygame.display.set_mode([height, width])  # 设置窗口尺寸
#
# while True: # 设置窗口循环事件
#     for event in pygame.event.get():# 利用for循环将event在pygame自带的事件中遍历
#         if event.type == pygame.QUIT: # 如果event的类型 = pygame退出事件的类型
#             pygame.quit() # 则关闭窗口

#
#
#import pygame

import pygame
import random

# 游戏模式
GAME_MODES = {
  "标准模式": "standard",
  "找茬模式": "find_the_difference",
  "速算模式": "quick_calculation",
  "古诗模式": "ancient_poetry",
}

# 游戏难度
GAME_DIFFICULTIES = {
  "简单": "easy",
  "中等": "medium",
  "困难": "hard",
}


# 初始化pygame
pygame.init()

# 设置窗口的大小
screen_width, screen_height = 800, 600

# 创建窗口
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题
pygame.display.set_caption("我的游戏")

# 定义颜色和其他常量
BLACK_COLOR = (0, 0, 0)
BORDER_WIDTH = 2
GRID_SIZE = 50
BOARD_SIZE = 10

# 你的其他代码，比如RenjuBoard类的定义和使用
# 确保在使用screen之前，它已经被定义和初始化

# 游戏主循环
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#             # 绘制你的游戏板和其他图形
#     例如: pygame.draw.rect(screen, BLACK_COLOR, ...)
# 创建一个图像
# face = pygame.Surface((60, 60), flags=pygame.HWSURFACE)
# # 填充图像
# face.fill(color='pink')
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
# # #     # 将图像添加到主屏幕上
# # #     screen.blit(face, (100, 100))
# # #     # 更新屏幕显示
# # #     pygame.display.flip()

# 游戏界面
class Game界面(pygame.sprite.Sprite):
  def __init__(self, game):
    super().__init__()

    self.game = game

    # 游戏背景
    self.background = pygame.image.load("background.png")

    # 游戏标题
    self.title = pygame.image.load("title.png")

    # 游戏按钮
    self.buttons = pygame.sprite.Group()

    # 游戏主界面
    self.main_menu = MainMenu(self)
    self.buttons.add(self.main_menu)

    # 游戏测试记录界面
    self.test_records = TestRecords(self)
    self.buttons.add(self.test_records)

  def update(self):
    # 更新游戏界面
    self.screen.blit(self.background, (0, 0))
    self.screen.blit(self.title, (0, 0))

    # 更新游戏按钮
    self.buttons.update()

# 游戏主菜单
class MainMenu(pygame.sprite.Sprite):
  def __init__(self, game_interface):
    super().__init__()

    self.game_interface = game_interface

    # 游戏模式按钮
    self.game_mode_buttons = pygame.sprite.Group()
    for game_mode in GAME_MODES:
      button = GameModeButton(self, game_mode)
      self.game_mode_buttons.add(button)

    # 游戏难度按钮
    self.game_difficulty_buttons = pygame.sprite.Group()
    for game_difficulty in GAME_DIFFICULTIES:
      button = GameDifficultyButton(self, game_difficulty)
      self.game_difficulty_buttons.add(button)

    # 开始游戏按钮
    self.start_button = pygame.sprite.Sprite()
    self.start_button.image = pygame.image.load("start_button.png")
    self.start_button.rect = self.start_button.image.get_rect()
    self.start_button.rect.center = (self.game_interface.screen.get_width() // 2, self.game_interface.screen.get_height() // 2)

  def update(self):
    # 更新游戏模式按钮
    self.game_mode_buttons.update()

    # 更新游戏难度按钮
    self.game_difficulty_buttons.update()

    # 更新开始游戏按钮
    self.screen.blit(self.start_button.image, self.start_button.rect)

# 游戏测试记录界面
class TestRecords(pygame.sprite.Sprite):
  def __init__(self, game_interface):
    super().__init__()

    self.game_interface = game_interface

    # 测试记录列表
    self.test_records_list = pygame.sprite.Group()

  def update(self):
    # 更新测试记录列表
    self.test_records_list.update()

# 游戏模式按钮
class GameModeButton(pygame.sprite.Sprite):
  def __init__(self, main_menu, game_mode):
    super().__init__()

    self.main_menu = main_menu
    self.game_mode = game_mode

    self.image = pygame.image.load("game_mode_button.png")
    self.rect = self.image.get_rect()
    self.rect.center = (self.main_menu.screen.get_width() // 2, self.main_menu.screen.get_height() // 2)

  def update(self):
    # 更新游戏模式按钮
    self.screen.blit(self.image, self.rect)

# 游戏难度按钮
class GameDifficultyButton(pygame.sprite.Sprite):
  def __init__(self, main_menu, game_difficulty):
    super().__init__()


# 退出pygame
pygame.quit()


# import pygame
# import sys
#
# pygame.init()
# # 设置主窗口
# screen = pygame.display.set_mode((800, 400))
# screen.fill('blue')
# # 设置窗口标题
# pygame.display.set_caption('小马哥不马虎')
# 创建一个图像
# face = pygame.Surface((60, 60), flags=pygame.HWSURFACE)
# # 填充图像
# face.fill(color='pink')
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     # 将图像添加到主屏幕上
#     screen.blit(face, (100, 100))
#     # 更新屏幕内容
#     pygame.display.flip()
