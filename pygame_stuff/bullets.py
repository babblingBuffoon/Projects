import pygame
import math
import time
import sys
# bullet movement and draw
#
#
#
#

pygame.init() 

display_width = 640
display_height = 480
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Vectors") 
player_speed  = 5
bullet_speed = 5

x = 340
y = 440


player_size = 30


    

bullet_list = []



def collision():
    if b.colliderect(enemy) or round(bullet[1]) < 0 :
        return True


   
last_time = time.time()

clock = pygame.time.Clock()
run = True
while run: 
    delta_t = time.time() - last_time
    delta_t *= 120
    last_time = time.time()
    display.fill((100,100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_list.append([x , y])
    
    g = pygame.key.get_pressed()
    if g[pygame.K_RIGHT]:
        x += player_speed*delta_t
        if x > display_width-player_size/2:
            x = display_width - player_size/2
    if g[pygame.K_LEFT]:
        x -= player_speed*delta_t
        if x <= player_size/2:
            x = player_size/2

    

        

    

    for bullet in bullet_list:
        bullet[1] -= bullet_speed*delta_t
        b = pygame.Rect(bullet[0] ,bullet[1], 10 , 8)
        pygame.draw.rect(display , (255 , 0 , 0) , b )

        if collision():
            bullet_list.remove(bullet)
    
    player = pygame.Rect(x-13 ,y , player_size , player_size)
    pygame.draw.rect(display, (73, 235, 52) , player , )
    
    enemy = pygame.Rect(300, 100 , 30 , 30)
    pygame.draw.rect(display, (80, 60, 40) , enemy)
    
    
    pygame.draw.line(display , (52, 235, 58) , (0 , 400 ) , (640 ,400), width=3)
    




    pygame.display.update()
clock.tick(60)
pygame.quit()
quit()
