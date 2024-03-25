import pygame  # 导入pygame库

pygame.init()  # pygame组件初始化
pygame.display.set_caption("测试窗口")  # 设置窗口名称
height = 600  # 窗口高度变量
width = 400  # 窗口宽度变量
# 将设置窗口大小赋值给screen是方便以后贴图粘贴的方便
screen = pygame.display.set_mode([height, width])  # 设置窗口尺寸

while True: # 设置窗口循环事件
    for event in pygame.event.get():# 利用for循环将event在pygame自带的事件中遍历
        if event.type == pygame.QUIT: # 如果event的类型 = pygame退出事件的类型
            pygame.quit() # 则关闭窗口

#
#
# import pygame
#
# # 初始化pygame
# pygame.init()
#
# # 设置窗口的大小
# screen_width, screen_height = 800, 600
#
# # 创建窗口
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# # 设置窗口标题
# pygame.display.set_caption("我的游戏")
#
# # 定义颜色和其他常量
# BLACK_COLOR = (0, 0, 0)
# BORDER_WIDTH = 2
# GRID_SIZE = 50
# BOARD_SIZE = 10
#
# # 你的其他代码，比如RenjuBoard类的定义和使用
# # 确保在使用screen之前，它已经被定义和初始化
#
# # 游戏主循环
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#             # 绘制你的游戏板和其他图形
#     # 例如: pygame.draw.rect(screen, BLACK_COLOR, ...)
#
#     # 更新屏幕显示
#     pygame.display.flip()
#
# # 退出pygame
# pygame.quit()
