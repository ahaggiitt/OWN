import random
import sys
import os
import pygame

# 配置
CURPATH = os.getcwd()
SCREENSIZE = (993, 477)
# 锤子图片两张
HAMMER_IMAGEPATHS = [os.path.join(CURPATH, 'images/hammer0.png'),
                     os.path.join(CURPATH, 'images/hammer1.png')]
# 开始图片
GAME_BEGIN_IMAGEPATHS = [os.path.join(CURPATH, 'images/begin.png'),
                         os.path.join(CURPATH, 'images/begin1.png')]

# 重新开始图标
GAME_AAIN_IMAGEPATHS = [os.path.join(CURPATH, 'images/again1.png'),
                        os.path.join(CURPATH, 'images/again2.png')]

# 背景图
GAME_BG_IMAGEPATH = os.path.join(CURPATH, 'images/background.png')

# 结束背景图
GAME_END_IMAGEPATH = os.path.join(CURPATH, 'images/end.png')

MOLE_IMAGEPATHS = [os.path.join(CURPATH, 'images/mole_1.png'),
                   os.path.join(CURPATH, 'images/mole_laugh1.png'),
                   os.path.join(CURPATH, 'images/mole_laugh2.png'),
                   os.path.join(CURPATH, 'images/mole_laugh3.png')]
# 随机位置
HOLE_POSITIONS = [(90, -20), (405, -20), (720, -20), (90, 140), (405, 140), (720, 140), (90, 290), (405, 290),
                  (720, 290)]
BGM_PATH = os.path.join(CURPATH, 'audios/bgm.mp3')

# --------------------------------------------------------------------------
COUNT_DOWN_SOUND_PATH = os.path.join(CURPATH, 'audios/count_down.wav')
HAMMERING_SOUND_PATH = os.path.join(CURPATH, 'audios/hammering.wav')

FONT_PATH = os.path.join(CURPATH, 'font/Gabriola.ttf')
BROWN = (150, 75, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RECORD_PATH = os.path.join(CURPATH, 'score.rec')

'''地鼠'''


class Mole(pygame.sprite.Sprite):
    # 4张地鼠图片，随机位置
    def __init__(self, image_paths, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 缩放图片第一张和最后一张
        self.images = [pygame.transform.scale(pygame.image.load(image_paths[0]), (101, 103)),
                       pygame.transform.scale(pygame.image.load(image_paths[-1]), (101, 103))]

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        # 用于快速实现完美的碰撞检测，Mask可以精确到1个像素级别的判断
        self.mask = pygame.mask.from_surface(self.image)
        self.setPosition(position)

        self.is_mole = False

    '''设置位置'''

    def setPosition(self, pos):
        self.rect.left, self.rect.top = pos

    '''设置被击中'''

    def setBeHammered(self):
        self.is_mole = True

    '''显示在屏幕上'''

    def draw(self, screen):
        if self.is_mole:
            self.image = self.images[1]
        screen.blit(self.image, self.rect)

    '''重置'''

    def reset(self):
        self.image = self.images[0]
        self.is_mole = False


'''锤子类'''


class Hammer(pygame.sprite.Sprite):
    def __init__(self, image_paths, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load(image_paths[0]), pygame.image.load(image_paths[1])]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.images[1])
        self.rect.left, self.rect.top = position
        self.is_hammering = False

    '''设置位置'''

    def setPosition(self, pos):
        self.rect.centerx, self.rect.centery = pos

    '''显示在屏幕上'''

    def draw(self, screen):
        if self.is_hammering:
            self.image = self.images[1]
        else:
            self.image = self.images[0]
        screen.blit(self.image, self.rect)


'''游戏初始化'''


def initGame():
    pygame.init()
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption('打地鼠')
    return screen


'''游戏开始界面'''


def startInterface(screen, begin_image_paths):
    begin_images = [pygame.image.load(begin_image_paths[0]), pygame.image.load(begin_image_paths[1])]
    begin_image = begin_images[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                # 获取鼠标光标的位置。
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] in list(range(419, 574)) and mouse_pos[1] in list(range(374, 416)):
                    begin_image = begin_images[1]
                else:
                    begin_image = begin_images[0]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and mouse_pos[0] in list(range(419, 574)) and mouse_pos[1] in list(
                        range(374, 416)):
                    return True
        screen.blit(begin_image, (0, 0))
        pygame.display.update()


# '''结束界面'''				背景图
def endInterface(screen, end_image_path, score_info, font_path, font_colors, screensize):
    end_image = pygame.image.load(end_image_path)
    font = pygame.font.Font(font_path, 50)
    # 分数
    your_score_text = font.render('Your Score: %s' % score_info['your_score'], True, font_colors[0])
    your_score_rect = your_score_text.get_rect()
    your_score_rect.left, your_score_rect.top = (screensize[0] - your_score_rect.width) / 2, 215

    best_score_text = font.render('Best Score: %s' % score_info['best_score'], True, font_colors[1])
    best_score_rect = best_score_text.get_rect()
    best_score_rect.left, best_score_rect.top = (screensize[0] - best_score_rect.width) / 2, 275

    text = font.render('Game over', True, font_colors[1])
    text_rect = text.get_rect()
    text_rect.left, text_rect.top = 415, 370

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(end_image, (0, 0))
        screen.blit(your_score_text, your_score_rect)
        screen.blit(best_score_text, best_score_rect)
        screen.blit(text, text_rect)
        pygame.display.update()


'''主函数'''


def main():
    # 初始化
    screen = initGame()
    # 加载背景音乐和其他音效
    pygame.mixer.init()
    pygame.mixer.music.load(BGM_PATH)
    pygame.mixer.music.play(-1)
    # 音效
    audios = {
        'count_down': pygame.mixer.Sound(COUNT_DOWN_SOUND_PATH),
        'hammering': pygame.mixer.Sound(HAMMERING_SOUND_PATH)
    }
    # # 加载字体
    font = pygame.font.Font(FONT_PATH, 40)
    # # 加载背景图片
    bg_img = pygame.image.load(GAME_BG_IMAGEPATH)
    # 开始界面
    startInterface(screen, GAME_BEGIN_IMAGEPATHS)

    # 地鼠改变位置的计时         随机选择位置
    hole_pos = random.choice(HOLE_POSITIONS)

    # # 创建一个事件
    change_hole_event = pygame.USEREVENT
    # # 放在计时器里触发一次
    pygame.time.set_timer(change_hole_event, 800)

    # # 地鼠		4张图片       随机位置
    mole = Mole(MOLE_IMAGEPATHS, hole_pos)
    # # 锤子
    hammer = Hammer(HAMMER_IMAGEPATHS, (500, 250))
    your_score = 0
    flag = False
    # # 游戏主循环
    while True:
        # 	# --游戏时间为60s
        time_remain = round((61000 - pygame.time.get_ticks()) / 1000)
        # # 	# --游戏时间减少, 地鼠变位置速度变快
        if time_remain == 40 and not flag:
            # 随机拿到位置
            pygame.time.set_timer(change_hole_event, 650)
            flag = True
        elif time_remain == 20 and flag:
            pygame.time.set_timer(change_hole_event, 500)
            flag = False
        # --倒计时音效
        elif 0 < time_remain <= 10:
            audios['count_down'].play()
        # --游戏结束
        elif time_remain < 0:
            break
        count_down_text = font.render('Time: ' + str(time_remain), True, WHITE)

        # 	# --按键检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 鼠标事件，拿到鼠标的位置，让锤子在鼠标位置处
            elif event.type == pygame.MOUSEMOTION:
                mou_position = pygame.mouse.get_pos()
                hammer.setPosition(mou_position)
            # 鼠标按键，改变锤子的状态
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    hammer.is_hammering = True

            # 鼠标按键抬起 改变锤子图片
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    hammer.is_hammering = False

            # 自定义事件 拿到地鼠图片 放在随机位置处
            elif event.type == change_hole_event:
                hole_pos = random.choice(HOLE_POSITIONS)
                mole.reset()
                mole.setPosition(hole_pos)

        # # --碰撞检测  锤子击下并且地鼠为False的时候
        if hammer.is_hammering and not mole.is_mole:
            is_hammer = pygame.sprite.collide_mask(hammer, mole)
            if is_hammer:
                # 播放声音
                audios['hammering'].play()
                # 变换造型
                mole.setBeHammered()
                your_score += 10
        # 	# --分数
        your_score_text = font.render('Score: ' + str(your_score), True, BROWN)

        # 	# --绑定必要的游戏元素到屏幕(注意顺序)
        screen.blit(bg_img, (0, 0))
        # 记录时间
        screen.blit(count_down_text, (875, 8))
        # 记录分数
        screen.blit(your_score_text, (800, 430))

        mole.draw(screen)
        hammer.draw(screen)
        pygame.display.flip()
    # # 读取最佳分数(try块避免第一次游戏无.rec文件)
    try:
        best_score = int(open(RECORD_PATH).read())
    except:
        best_score = 0
    # 若当前分数大于最佳分数则更新最佳分数
    if your_score > best_score:
        f = open(RECORD_PATH, 'w')
        f.write(str(your_score))
        f.close()
    # # 结束界面
    score_info = {'your_score': your_score, 'best_score': best_score}
    endInterface(screen, GAME_END_IMAGEPATH, score_info, FONT_PATH, [WHITE, RED], SCREENSIZE)


main()