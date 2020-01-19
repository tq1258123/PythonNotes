# 创建设置类
class Settings():
    '''存储《外星人入侵》的所有初始设置的参数'''
    def __init__(self):
        '''初始化游戏的设置'''
        '''初始化游戏的静态设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 设置游戏命数，这样已经是有三条命
        self.ship_limit = 2
        # 设置飞船移动速度
        self.ship_speed_factor = 1.5
        
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 屏幕上可以同时出现多少颗子弹
        self.bullets_allowed = 6

        # 外星人设置
        self.fleet_drop_speed = 10

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        
        # 提高外星人分值
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # 消灭飞船得分
        self.alien_points = 50
        
        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度和外星人分值设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        


        
