
#game loops infinite unless quit
#every change on screen needs to update screen
#get snake movement on x , y axis with user input
#random food generator for snake inside display window
#create a counter system for snake to increase with every food block that eats
#create colision system when snake crosses itself to terminate game - work in progress
#no colision system for display
#



import pygame
from pygame.math import Vector2
import random

pygame.init() 

block_size = 30
block_no= 20

win = pygame.display.set_mode((block_size*block_no, block_size*block_no)) 
pygame.display.set_caption("Snake Game") 







######################################################### snake zone

snake_color = (255, 0, 0)
snake_body = [Vector2(1, 3), Vector2(2,3) , Vector2(3,3)] #initial position and lenght of the snake
direction = Vector2(1 ,0)

def draw_snake():
    for b in snake_body:
        x_pos = b.x * block_size
        y_pos = b.y * block_size
        s = pygame.Rect(x_pos, y_pos, block_size, block_size)
        pygame.draw.rect(win , snake_color, s)

snake_start = True

def move_snake():
    global snake_body
    body_copy = snake_body[:-1]
    body_copy.insert(0,body_copy[0] + direction)
    snake_body = body_copy

def add_to_snake(pos):
    global snake_body
    snake_body.append(pos)
    

################################################### food zone #### generate a starting position for food and draw

def randomizer():
    x = random.randrange(0 , block_no-1)
    y = random.randrange(0 , block_no-1)
    f = Vector2(x, y)
    return f


position = randomizer() # store position of the food

fruit_color = (141, 245, 66)

def draw_fruit():
    f = pygame.Rect((position.x * block_size), (position.y * block_size), block_size, block_size)
    pygame.draw.rect(win , fruit_color, f)



###################################################### check for collisions 
    

    ##check for food collision, update position and add to snake size
def food_collision_check():                      
    global position
    if position == snake_body[0]:
        position = randomizer()
        add_to_snake(position)

def snake_back_movement():
    if snake_body[0] == snake_body[1] - direction:
        return True
        

def snake_self_collision():
    for i in range(len(snake_body) - 1):
            if snake_body[0] == snake_body[i+1]:
                return True

#check edge of screen and reset position.
def boundaries_check():
    if snake_body[0].x >= block_no+1:
        snake_body[0].x = 0
    if snake_body[0].x <= -1:
        snake_body[0].x = block_no+1
    if snake_body[0].y >= block_no+1:
        snake_body[0].y = 0
    if snake_body[0].y <= -1:
        snake_body[0].y = block_no+1


######################################################  render text and update score


score = 0
score_increment = 1

font = pygame.font.Font(None, 50)

def update_score():
   global score
   global score_increment
   global position
   if position == snake_body[0]:
       score += score_increment

def score_board():
    global score
    text = font.render(f'Score: {score}', True, (125, 124, 121))
    text.set_alpha(150)
    win.blit(text, (1 , 1))


###################################################### main loop
clock = pygame.time.Clock()
run = True
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    pygame.time.delay(75)
    win.fill((0,0,0))
    score_board()
    

    
    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            direction = Vector2(-1, 0)
        if event.key == pygame.K_RIGHT:
            direction = Vector2(1, 0)
        if event.key == pygame.K_UP:
            direction = Vector2(0, -1)
        if event.key == pygame.K_DOWN:
            direction = Vector2(0, 1)    

    
    if keys[pygame.K_SPACE]:
        snake_start = not snake_start
    
    
    if snake_back_movement():
        direction = - direction
    
    if snake_self_collision():
        run = False
        print('collision')
            
    update_score()
    food_collision_check()
    boundaries_check()
    draw_fruit()
    if snake_start: move_snake()
    draw_snake()

    
    
    pygame.display.update()
    
clock.tick(30)
pygame.quit()




 