import pygame
from icecream import ic
import random

pygame.init() 
win = pygame.display.set_mode((800 , 800)) 
pygame.display.set_caption("Pong") 


run = True
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False



pygame.display.update()
pygame.quit()