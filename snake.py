import pygame
#from rect import *
from pygame.locals import *
from pygame.math import Vector2

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
colores = [BLACK,GRAY,WHITE,RED,GREEN,BLUE,YELLOW,CYAN,MAGENTA]
key_dict = {K_k:BLACK,K_0:GRAY,K_w:WHITE,K_r:RED,K_g:GREEN,K_b:BLUE,K_y:YELLOW,K_c:CYAN,K_m:MAGENTA}

pygame.init()


size = width,height = (720,480)
screen = pygame.display.set_mode(size)


class Snake:
    def __init__(self):
        self.body = [Vector2(10,100),Vector2(10,110),Vector2(10,120)]
        self.direccion = Vector2(0,-10)
        self.add = False
        
    def draw(self):
        for bloque in self.body:
            pygame.draw.rect(screen,GREEN,(bloque.x,bloque.y,10,10))
            
    def move(self):
        pass
        #[0,1,2] --> [0,1] --> [None,0,1] --> [-1,0,1]
        
        

def main():
    
    snake = Snake()
    running = True
    while running:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        snake.draw()
        pygame.display.update()

main()

