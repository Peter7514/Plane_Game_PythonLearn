import pygame
from plane_sprites import *

pygame.init()
screen = pygame.display.set_mode((480,700))

# 绘制背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
# pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,500))
# pygame.display.update()
# 定义RECT记录初始位置
hero_rect = pygame.Rect(150,300,102,126)
# 统一调用更新
pygame.display.update()
# 游戏循环：意味这游戏的正式开始
clock = pygame.time.Clock()

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1= GameSprite("./images/enemy1.png",2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        print(event)
        # 判断是否为退出事件
        if event.type == pygame.QUIT:
            print("游戏退出。。。")
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700
    screen.blit(bg, (0,0))
    screen.blit(hero,hero_rect)
    # 让精灵组调用两个方法
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()


pygame.quit()