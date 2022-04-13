import sys,pygame
from typing import TypeGuard

pygame.init()

size = width, height = 800,600
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.Rect(10, 10, 10, 10)


while 1:
    speed = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN :
        
            if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_z]:
                speed[1] = -10
            if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
                speed[1] = 10
            if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_q]:
                speed[0] = -10
            if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
                speed[0] = 10
            
    ball = ball.move(speed)

    screen.fill((255, 255, 255))
    test = pygame.draw.rect(screen, (255, 0, 0), ball)
    pygame.display.flip()