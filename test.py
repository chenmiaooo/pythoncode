import pygame
from pygame.locals import *
white = 255,255,255
blue = 0,0,200
pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello Pygame",True,white)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            exit(0)
        screen.fill(blue)
        screen.blit(textImage,(100,100))
        pygame.display.update()