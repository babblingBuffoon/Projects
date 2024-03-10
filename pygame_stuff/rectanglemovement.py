import pygame 
import random






pygame.init() 
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height)) 
pygame.display.set_caption("Moving rectangle") 

Height = 20
Width = 20
Color = (255 , 0, 0)
x_speed , y_speed = 1 , -1
pos_x = 300
pos_y = 257
p_list = [(pos_x , pos_y)]
snake = pygame.Rect(pos_x , pos_y, Width, Height)

x_frt = random.randrange(0 , 500 - Width)
y_frt = random.randrange(0 , 500 - Height)
fruit_color = (141, 245, 66)
fruit = pygame.Rect(x_frt, y_frt, Width, Height)

speed_increment = 1

time_delay = 5000 # 0.5 seconds
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , time_delay )


run = True

# infinite loop 
while run: 

    pygame.time.delay(5) 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False

    win.fill((0, 0, 0))

    snake.x += x_speed * speed_increment
    snake.y += y_speed

    if snake.right > win_width or snake.left < 0:
        x_speed *= -1
    if snake.bottom > 500 or snake.top < 0:
        y_speed *= -1

    

    pygame.draw.rect(win , Color , snake)
    pygame.draw.rect(win , fruit_color, fruit)
    
    pygame.display.update() 


pygame.quit() 
