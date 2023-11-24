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

#SNAKE_BODY = pygame.transform.scale(pygame.image.load(os.path.join(r"/Users/diegojimenez/VideoJuegoUAN/Snake_Game/images/snakebody.png")),(20,20))
SNAKE_BODY = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Snake_Game\images\snakebody.png")),(20,20))

#APPLE = pygame.transform.scale(pygame.image.load(os.path.join(r"/Users/diegojimenez/VideoJuegoUAN/Snake_Game/images/manzana.png")),(20,20))
APPLE = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Snake_Game\images\manzana.png")),(20,20))

SNAKE_HEAD = []
for x in range(1,5):
    #SNAKE_HEAD += [pygame.transform.scale(pygame.image.load(os.path.join(r"/Users/diegojimenez/VideoJuegoUAN/Snake_Game/images/SnakeHead"+str(x)+".png")),(20,20))]
    SNAKE_HEAD += [pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Snake_Game\images\SnakeHead"+str(x)+".png")),(20,20))]
    #print(x)


#EAT_SOUND = pygame.mixer.Sound("/Users/diegojimenez/VideoJuegoUAN/Snake_Game/coin.wav")
#EAT_SOUND = pygame.mixer.Sound("C:\Snake_Game\coin.wav")

screen = pygame.display.set_mode(size)
SCORE_TEXT = pygame.font.SysFont("Russo One",15)

class Snake:
    def __init__(self):
        self.body = [Vector2(20,100),Vector2(20,110),Vector2(20,120)]
        self.direccion = Vector2(0,-20)
        self.add = False
        
        
    def draw(self):
        for bloque in self.body:
            #pygame.draw.rect(screen,GREEN,(bloque.x,bloque.y,20,20))
            screen.blit(SNAKE_BODY,(bloque.x,bloque.y))
        if self.direccion == Vector2(0, -20):
            screen.blit(SNAKE_HEAD[0],(self.body[0].x,self.body[0].y))
            #print(SNAKE_HEAD[0])
            
        if self.direccion == Vector2(0, 20):
            screen.blit(SNAKE_HEAD[2],(self.body[0].x,self.body[0].y))
            #print(SNAKE_HEAD[2])
            
        if self.direccion == Vector2(20,0):
            screen.blit(SNAKE_HEAD[1],(self.body[0].x,self.body[0].y))
            #print(SNAKE_HEAD[1])
            
        if self.direccion == Vector2(-20, 0):
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
        self.direccion = Vector2(0, -20)
        
    def move_down(self):
        self.direccion = Vector2(0, 20)
        
    def move_left(self):
        self.direccion = Vector2(-20, 0)
        
    def move_right(self):
        self.direccion = Vector2(20, 0)
        
        
    def die(self):
        if self.body[0].x >= size[0]+20 or self.body[0].y >= size[1]+20 or self.body[0].x <= -20 or self.body[0].y <= 20:
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
        #pygame.draw.rect(screen,RED,(self.pos.x,self.pos.y,20,20))
        screen.blit(APPLE,(self.pos.x,self.pos.y))
        
    def generate(self):
        self.x = random.randrange(0, size[0]/20)
        self.y = random.randrange(0, size[1]/20)
        self.pos = Vector2(self.x*20,self.y*20)
        
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
        while True:
            self.current_scene.run()
           

class MainMenuScene:
    def __init__(self, scene_manager, high_score):
        self.scene_manager = scene_manager
        self.high_score = high_score
        self.background_image = pygame.image.load(r"C:\Snake_Game\images\snake.png")

    def handle_events(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
    def draw(self, screen):
        # Limpia la pantalla
        screen.fill((175, 215, 70))
        #screen.blit(self.background_image, (0, 0))

        # Dibuja el texto del menú
        font = pygame.font.SysFont("Russo One", 50)
        font2 = pygame.font.SysFont("Russo One", 20)
        text_play = font.render("Snake Game UAN", True, MAGENTA)
        
        text_high_score = font2.render("High Score: {}".format(self.high_score), True, BLACK)
        text_enter = font2.render("Puedes superar el High Score ponte a prueba..presiona ENTER para jugar", True, BLACK)
        text_diego = font2.render("Por: Diego Jimenez", True, BLACK)

        play_rect = text_play.get_rect(center=(width / 2, height / 2 + 120))
        high_score_rect = text_high_score.get_rect(center=(width / 2, height / 2 + 160))
        enter_rect = text_enter.get_rect(center=(width / 2, height / 2 + 180))
        image_rect = self.background_image.get_rect(center=(width / 2, height / 2 - 70))
        
        screen.blit(text_play, play_rect)
        screen.blit(text_diego, (10, 460))
        screen.blit(text_enter, enter_rect)
        screen.blit(self.background_image, image_rect)
        screen.blit(text_high_score, high_score_rect)
        

        pygame.display.flip()

    def run(self):
        while True:
            events = pygame.event.get()
            self.handle_events(events)
            self.draw(screen)
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == K_RETURN:
                    # Transition to the GameScene
                    self.scene_manager.set_scene(GameScene(self.scene_manager))
                    return
                
class GameScene:
    
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.load_high_score()
        self.collision_time = 0
        
    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))
        
    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            # Si el archivo no existe, establece un récord inicial.
            self.high_score = 0

    def handle_events(self, events):
        for event in  events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                
            #metodo para mover serpiete hacia arriba
            if event.type == pygame.KEYDOWN and self.snake.direccion.y != 20:
                if event.key == pygame.K_UP:
                    self.snake.move_up()
                    
            #metodo para mover serpiete hacia abajo
            if event.type == pygame.KEYDOWN and self.snake.direccion.y != -20:
                if event.key == pygame.K_DOWN:
                    self.snake.move_down()
                    
            #metodo para mover serpiete hacia la izquierda
            if event.type == pygame.KEYDOWN and self.snake.direccion.x != 20:
                if event.key == pygame.K_LEFT:
                    self.snake.move_left()
                    
            #metodo para mover serpiete hacia la derecha
            if event.type == pygame.KEYDOWN and self.snake.direccion.x != -20:
                if event.key == pygame.K_RIGHT:
                    print('derecha')
                    self.snake.move_right()

    def draw(self, screen):
        # Limpia la pantalla
        screen.fill((175, 215, 70))
        
       

        if self.snake.die():
            if pygame.time.get_ticks() % 1000 < 500:  
                elapsed_time = pygame.time.get_ticks() - self.collision_time
                if elapsed_time % 1100 < 500:  
                    self.snake.draw()

                if elapsed_time > 2000:  
                    self.scene_manager.set_scene(GameOverScene(self.scene_manager, self.score))
                    return 
                
        else:
            self.snake.draw()
            self.apple.draw()
            self.snake.move()

            if self.apple.check_collision(self.snake):
                #EAT_SOUND.play()
                
                self.score += 1
                

            text = SCORE_TEXT.render("Score: {}".format(self.score), 1, WHITE)
            screen.blit(text, (width - text.get_width() - 20, 20))
            
            high_score_text = SCORE_TEXT.render("High Score: {}".format(self.high_score), 1, WHITE)
            screen.blit(high_score_text, (20, 20))
            
            print(self.score)
        pygame.display.update()

    def run(self):
        fps = pygame.time.Clock()
        
        while True:
            fps.tick(5)
            #print("Game Scene Running")
            events = pygame.event.get()
            self.handle_events(events)
            self.draw(screen)
            
            if self.snake.die():
                pygame.time.delay(2000) 
                self.scene_manager.set_scene(GameOverScene(self.scene_manager, self.score))
                break
                
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            
      
      
class GameOverScene:
    def __init__(self, scene_manager, score):
        self.scene_manager = scene_manager
        self.score = score
        self.background_image = pygame.image.load(r"C:\Snake_Game\images\gameover.png")
        self.background_image = pygame.transform.scale(self.background_image, (200, 200))

    def handle_events(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Manejar eventos adicionales según sea necesario

    def draw(self, screen):
        # Limpia la pantalla
        screen.fill((175, 215, 70))

        # Dibuja el texto de Game Over y el puntaje
        font = pygame.font.SysFont("Russo One", 50)
        font2 = pygame.font.SysFont("Russo One", 30)
        text_game_over = font.render("Game Over", True, WHITE)
        text_score = font2.render("Score: {}".format(self.score), True, BLACK)
        text_enter = font2.render("Presiona ENTER para reintentarlo", True, BLACK)

        game_over_rect = text_game_over.get_rect(center=(width / 2, height / 2 - 140))
        score_rect = text_score.get_rect(center=(width / 2, height / 2 + 100))
        image_rect = self.background_image.get_rect(center=(width / 2, height / 2 - 20))
        enter_rect = text_enter.get_rect(center=(width / 2, height / 2 + 180))

        screen.blit(text_game_over, game_over_rect)
        screen.blit(text_score, score_rect)
        screen.blit(text_enter, enter_rect)
        screen.blit(self.background_image, image_rect)

        pygame.display.flip()

    def run(self):
        while True:
            events = pygame.event.get()
            self.handle_events(events)
            self.draw(screen)
            high_score = 0  # Puedes establecer un valor predeterminado si es necesario
            with open("high_score.txt", "r") as file:
                try:
                    high_score = int(file.read())
                except ValueError:
                    pass

            for event in events:
                if event.type == pygame.KEYDOWN and event.key == K_RETURN:
                    # Volver a la escena del menú principal al presionar Enter
                    self.scene_manager.set_scene(MainMenuScene(self.scene_manager,high_score))
                    return  
        
def main():
    pygame.init()
    

    size = width, height = (720, 480)
    screen = pygame.display.set_mode(size)

    scene_manager = SceneManager()
    
    high_score = 0  # Puedes establecer un valor predeterminado si es necesario
    with open("high_score.txt", "r") as file:
        try:
            high_score = int(file.read())
        except ValueError:
            pass
        
    scene_manager.set_scene(MainMenuScene(scene_manager, high_score))

    while True:
        scene_manager.run_scene()

main()

