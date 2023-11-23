import pygame
import random
import os
import sys
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
print(size[0])

#SNAKE_BODY = pygame.transform.scale(pygame.image.load(os.path.join(r"/Users/diegojimenez/VideoJuegoUAN/Snake_Game/images/snakebody.png")),(10,10))
SNAKE_BODY = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Snake_Game\images\snakebody.png")),(10,10))

#APPLE = pygame.transform.scale(pygame.image.load(os.path.join(r"/Users/diegojimenez/VideoJuegoUAN/Snake_Game/images/manzana.png")),(10,10))
APPLE = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Snake_Game\images\manzana.png")),(10,10))

SNAKE_HEAD = []
for x in range(1,5):
    #SNAKE_HEAD += [pygame.transform.scale(pygame.image.load(os.path.join(r"/Users/diegojimenez/VideoJuegoUAN/Snake_Game/images/SnakeHead"+str(x)+".png")),(10,10))]
    SNAKE_HEAD += [pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Snake_Game\images\SnakeHead"+str(x)+".png")),(10,10))]
    #print(x)


#EAT_SOUND = pygame.mixer.Sound("/Users/diegojimenez/VideoJuegoUAN/Snake_Game/coin.wav")
#EAT_SOUND = pygame.mixer.Sound("C:\Snake_Game\coin.wav")

screen = pygame.display.set_mode(size)
SCORE_TEXT = pygame.font.SysFont("Russo One",15)

class Snake:
    def __init__(self):
        self.body = [Vector2(10,100),Vector2(10,110),Vector2(10,120)]
        self.direccion = Vector2(0,-10)
        self.add = False
        
    def draw(self):
        for bloque in self.body:
            #pygame.draw.rect(screen,GREEN,(bloque.x,bloque.y,10,10))
            screen.blit(SNAKE_BODY,(bloque.x,bloque.y))
        if self.direccion == Vector2(0, -10):
            screen.blit(SNAKE_HEAD[0],(self.body[0].x,self.body[0].y))
            #print(SNAKE_HEAD[0])
            
        if self.direccion == Vector2(0, 10):
            screen.blit(SNAKE_HEAD[2],(self.body[0].x,self.body[0].y))
            #print(SNAKE_HEAD[2])
            
        if self.direccion == Vector2(10,0):
            screen.blit(SNAKE_HEAD[1],(self.body[0].x,self.body[0].y))
            #print(SNAKE_HEAD[1])
            
        if self.direccion == Vector2(-10, 0):
            screen.blit(SNAKE_HEAD[3],(self.body[0].x,self.body[0].y))
            #print(SNAKE_HEAD[3])
            
    def move(self):
        pass
        #[0,1,2] --> [0,1] --> [None,0,1] --> [-1,0,1]
        if self.add  == True:
            body_copy = self.body
            body_copy.insert(0,body_copy[0]+self.direccion)
            self.body = body_copy[:]
            self.add = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direccion)
            self.body = body_copy[:]
            
    def move_up(self):
        self.direccion = Vector2(0, -10)
        
    def move_down(self):
        self.direccion = Vector2(0, 10)
        
    def move_left(self):
        self.direccion = Vector2(-10, 0)
        
    def move_right(self):
        self.direccion = Vector2(10, 0)
        
        
    def die(self):
        if self.body[0].x >= size[0]+10 or self.body[0].y >= size[1]+10 or self.body[0].x <= -10 or self.body[0].y <= 10:
            print('toco el borde')
            return True
        
        #snake se toca a si misma muere
        for i in self.body[1:]:
            if self.body[0] == i:
                return True
        
        
class Apple:
    def __init__(self):
        self.generate()
        
    def draw(self):
        #pygame.draw.rect(screen,RED,(self.pos.x,self.pos.y,10,10))
        screen.blit(APPLE,(self.pos.x,self.pos.y))
        
    def generate(self):
        self.x = random.randrange(0, size[0]/10)
        self.y = random.randrange(0, size[1]/10)
        self.pos = Vector2(self.x*10,self.y*10)
        
    def check_collision(self,snake):
        if snake.body[0] == self.pos:
            self.generate()
            snake.add = True
            return True
        
        for bloque in snake.body[1:]:
            if self.pos == bloque:
                self.generate()
        
        return False

class SceneManager:
    def __init__(self):
        self.current_scene = None

    def set_scene(self, new_scene):
        self.current_scene = new_scene

    def run_scene(self):
        self.current_scene.run()

class MainMenuScene:
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager

    def handle_events(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    scene_manager = SceneManager()
                    print('enter')
                    scene_manager.set_scene(GameScene(scene_manager))

    def draw(self, screen):
        # Limpia la pantalla
        screen.fill(BLACK)

        # Dibuja el texto del menú
        font = pygame.font.SysFont("Russo One", 50)
        text_play = font.render("Jugar", True, WHITE)

        play_rect = text_play.get_rect(center=(width / 2, height / 2 - 50))
        screen.blit(text_play, play_rect)

        pygame.display.flip()

    def run(self):
        while True:
            events = pygame.event.get()
            self.handle_events(events)
            self.draw(screen)
class GameScene:
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        self.snake = Snake()
        self.apple = Apple()

    def handle_events(self, events):
        for event in  events:
            if event.type == pygame.QUIT:
                running = False
                
            #metodo para mover serpiete hacia arriba
            if event.type == pygame.KEYDOWN and self.snake.direccion.y != 10:
                if event.key == pygame.K_UP:
                    self.snake.move_up()
                    
            #metodo para mover serpiete hacia abajo
            if event.type == pygame.KEYDOWN and self.snake.direccion.y != -10:
                if event.key == pygame.K_DOWN:
                    self.snake.move_down()
                    
            #metodo para mover serpiete hacia la izquierda
            if event.type == pygame.KEYDOWN and self.snake.direccion.x != 10:
                if event.key == pygame.K_LEFT:
                    self.snake.move_left()
                    
            #metodo para mover serpiete hacia la derecha
            if event.type == pygame.KEYDOWN and self.snake.direccion.x != -10:
                if event.key == pygame.K_RIGHT:
                    print('derecha')
                    self.snake.move_right()

    def draw(self, screen):
        # Limpia la pantalla
        screen.fill((175, 215, 70))
        score = 0
        # Dibuja el juego
        self.snake.draw()
        self.apple.draw()
        self.snake.move()

        if self.snake.die():
            quit()

        if self.apple.check_collision(self.snake):
            #EAT_SOUND.play()
            score+=1

        text = SCORE_TEXT.render("Score: {}".format(score), 1, WHITE)
        screen.blit(text, (width - text.get_width() - 10, 10))

        pygame.display.update()

    def run(self):
        fps = pygame.time.Clock()
        
        while True:
            fps.tick(5)
            #print("Game Scene Running")
            events = pygame.event.get()
            self.handle_events(events)
            self.draw(screen)
            
            
"""def main():
    
    snake = Snake()
    apple = Apple()
    running = True
    score = 0
    
    fps = pygame.time.Clock()
    
    while running:
        fps.tick(5)
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            #metodo para mover serpiete hacia arriba
            if event.type == pygame.KEYDOWN and snake.direccion.y != 10:
                if event.key == pygame.K_UP:
                    snake.move_up()
                    
            #metodo para mover serpiete hacia abajo
            if event.type == pygame.KEYDOWN and snake.direccion.y != -10:
                if event.key == pygame.K_DOWN:
                    snake.move_down()
                    
            #metodo para mover serpiete hacia la izquierda
            if event.type == pygame.KEYDOWN and snake.direccion.x != 10:
                if event.key == pygame.K_LEFT:
                    snake.move_left()
                    
            #metodo para mover serpiete hacia la derecha
            if event.type == pygame.KEYDOWN and snake.direccion.x != -10:
                if event.key == pygame.K_RIGHT:
                    snake.move_right()
                
                
        screen.fill((175,215,70))
        snake.draw()
        apple.draw()
        snake.move()
        
        if snake.die():
            quit()
            
        if apple.check_collision(snake):
            score+=1
            #EAT_SOUND.play()
            
        text = SCORE_TEXT.render("Score: {}".format(score),1,WHITE)
        screen.blit(text,(size[0]-text.get_width()-10,10))
        pygame.display.update()"""
        
def main():
    pygame.init()

    size = width, height = (720, 480)
    screen = pygame.display.set_mode(size)

    scene_manager = SceneManager()
    scene_manager.set_scene(GameScene(scene_manager))

    while True:
        scene_manager.run_scene()

main()

