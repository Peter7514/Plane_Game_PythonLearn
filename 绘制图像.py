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
# 统一调用更新
pygame.display.update()
# 游戏循环：意味这游戏的正式开始
while True:
    pass

pygame.quit()