# 《外星人入侵》主程序
import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # 初始化pygame 
    pygame.init()

    # 初始化游戏屏幕、游戏名设置，屏幕大小设置时要加括号
    ai_settings = Settings() # 初始设置类的实例化
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船、一个子弹编组和一个外星人组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button,
            ship, aliens, bullets)

        if stats.game_active:
            # 更新飞机移动
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                    aliens,bullets)
            # 更新外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship,
                aliens, bullets)

        # 填充屏幕背景，飞机，并进行刷新
        gf.update_screen(ai_settings, screen, stats, sb, ship,
            aliens, bullets, play_button)
        
run_game()
