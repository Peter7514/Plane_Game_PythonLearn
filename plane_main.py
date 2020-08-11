# 封装主游戏类和启动游戏
import pygame
from plane_sprites import *


class PlaneGame(object):
    """主游戏类"""
    def __init__(self):
        print("游戏初始化")
        # 创建窗口，时钟,精灵和精灵组
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create__sprites()
        # 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create__sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵和组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group()
        self.hero_group.add(self.hero)

    def start_game(self):
        print("开始游戏。。。")
        while True:
            # 设置刷新频率
            # 事件监听
            # 碰撞检测
            # 更新绘制精灵
            # 更新显示
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否为退出事件
            if event.type == pygame.QUIT:
                print(event)
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场。。。")
                # 创建敌机精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动d")
            elif event.type ==HERO_FIRE_EVENT:
                self.hero.fire()
        # 使用键盘提供的方法获取按键
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            print("向右移动")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机 完全实在调用封装的代码，用黑盒子
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group,True,True)
        # 敌机撞毁英雄
        ennemies = pygame.sprite.spritecollide(self.hero, self.enemy_group,True)
        if len(ennemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    game.start_game()
