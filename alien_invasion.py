import sys

import pygame

from settings import Settings

def fun_game():
    pass


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置固定颜色
    # bg_color = (230,230,230)
    

    # 开始设计游戏的主循环
    while True:
 
        # 监视键盘和鼠标的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕

        # 调用设置功能选择初始颜色
        screen.fill(ai_settings.bg_color)

        # 保持最近绘制的屏幕可见
        pygame.display.flip()

run_game()
