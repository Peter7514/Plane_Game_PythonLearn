import pygame

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

while True:
    clock.tick(60)
    # 监听事件
    even_list = pygame.event.get()
    if len(even_list) > 0:
        print(even_list)
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700
    screen.blit(bg, (0,0))
    screen.blit(hero,hero_rect)
    pygame.display.update()


pygame.quit()