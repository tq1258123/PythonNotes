# 创建ship类，管理飞船的大部分行为
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置其初始位置'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.screen_rect = screen.get_rect()  # 获得屏幕大小参数
        self.image = pygame.image.load(r'images/ship.bmp')
        self.rect = self.image.get_rect()   # 获得飞船图像大小参数

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)  # ????

        # 移动标志,初始不可以移动
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx    

    def update(self):
        '''根据移动标志调整飞船的位置，使飞船可以移动'''
        # 更新飞船的center值，而不是rect，并且考虑飞船移动的范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
