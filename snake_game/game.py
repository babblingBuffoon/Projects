#refactor game wtih oop .
#still work in progres to create game state for pause , start and end game.

import pygame , sys
from pygame.math import Vector2
import random
from settings import *
from icecream import ic

class Game:

    def __init__(self) -> None:
        self.player = Player()
        self.fruit = Fruit()
        self.score = Score()       


    def update(self):
        self.draw_elements()
        self.player.move_snake()
        if self.player.fruit_eating(self.fruit): self.score.update_score() 
        self.game_over_check() 
        
    def draw_elements(self):
        self.player.draw_snake()
        self.fruit.draw_fruit()
        self.score.draw_score_board()

    def game_over_check(self):
        for i in self.player.body[1:]:
            if self.player.body[0] == i:
                self.game_over()
        if not -1 <= self.player.body[0].x < block_no+1 or not -1 <= self.player.body[0].y <  block_no+1:
            ic(self.player.body[0].x)
            ic(self.player.body[0].y)
            self.game_over()

    def game_over(self) -> None:
        pygame.quit()
        sys.exit()


class Player:

    def __init__(self) -> None:
        self.body = [Vector2(3,3), Vector2(2,3) , Vector2(1,3)] #initial position and lenght of the snake
        self.direction = Vector2(1,0) #initial direction
        self.color = (255, 0, 0)

    def draw_snake(self):   
        for b in self.body:
            self.x_pos = b.x * block_size
            self.y_pos = b.y * block_size
            self.s = pygame.Rect(self.x_pos, self.y_pos, block_size, block_size)
            pygame.draw.rect(win , self.color, self.s)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy

    def fruit_eating(self , fruit):                      
        if fruit.position == self.body[0]:
            fruit.position = fruit.random_pos()
            self.add_to_snake(fruit.position)
            return True

    def add_to_snake(self , pos):
        self.body.append(pos)

   


class Fruit:

    def __init__(self) -> None:
        self.x = random.randrange(0 , block_no-1)
        self.y = random.randrange(0 , block_no-1)
        self.position = Vector2(self.x , self.y)
        

    def random_pos(self):
        x = random.randrange(0 , block_no-1)
        y = random.randrange(0 , block_no-1)
        p = Vector2(x, y)
        return p
    

    def draw_fruit(self):
        fruit_color = (141, 245, 66)
        f = pygame.Rect((self.position.x * block_size), (self.position.y * block_size), block_size, block_size)
        pygame.draw.rect(win , fruit_color, f)


class Score:
    
    def __init__(self) -> None:
        self.font =  pygame.font.SysFont(font , font_size)
        self.score = 0
        self.position = (1, 1)

    def draw_score_board(self) -> object:
        text = self.font.render(f'Score: {self.score}', True, (125, 124, 121))
        text.set_alpha(150)
        win.blit(text , self.position)
        
    def update_score(self) -> None:
        self.score += 1






pygame.init() 

# import valuse from settings

width = block_size * block_no
height = block_size * block_no
win = pygame.display.set_mode((width, height))
ic(width)
pygame.display.set_caption(title) 
#clock = pygame.time.Clock() 


game = Game()

############ main loop
run = True
while run: 
    pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                sys.exit()

# move snake with keys
                
        if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:                           
                       if game.player.direction.x != 1:         # <- to keep snake not backtracking into self , keep same direction unless direction is meant to be in opposite direction
                           game.player.direction = Vector2(-1, 0)
               if event.key == pygame.K_RIGHT:
                       if game.player.direction.x != -1:
                           game.player.direction = Vector2(1, 0)
               if event.key == pygame.K_UP:
                       if game.player.direction.y != 1:
                           game.player.direction = Vector2(0, -1)
               if event.key == pygame.K_DOWN:
                   if game.player.direction.y != -1:
                       game.player.direction = Vector2(0, 1)    

    win.fill((0,0,0))
    game.update()
    


    pygame.display.update()
pygame.quit()