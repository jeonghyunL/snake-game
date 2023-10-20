import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
PIXEL_SIZE = 20
LINE_WIDTH = 1

DIRECTION = {
    pygame.K_UP: 'UP',
    pygame.K_DOWN: 'DOWN',
    pygame.K_LEFT: 'LEFT',
    pygame.K_RIGHT: 'RIGHT',
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('VERITROSS Snake')

clock = pygame.time.Clock()

ToF = False

font = pygame.font.SysFont("arial", 30)
font.set_bold(True)
score = 0



class Snake():
    def __init__(self):
        self.snake_positions = [(15, 26), (15, 27), (15, 28), (15, 29)]
        self.snake_direction = 'UP'
    
    def snake_image(self):
        """뱀 이미지 생성"""
        snakeimage = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
        snakeimage.fill(RED)
        for bit in self.snake_positions:
            screen.blit(snakeimage, (bit[0] * PIXEL_SIZE, bit[1] * PIXEL_SIZE))
    
    def move(self):
        """뱀 움직임에 대한 함수"""
        head = self.snake_positions[0]
        x, y = head
        if self.snake_direction == 'UP':
            self.snake_positions = [(x, y-1)] + self.snake_positions[:-1]
        elif self.snake_direction == 'DOWN':
            self.snake_positions = [(x, y+1)] + self.snake_positions[:-1]
        elif self.snake_direction == 'LEFT':
            self.snake_positions = [(x-1, y)] + self.snake_positions[:-1]
        elif self.snake_direction == 'RIGHT':
            self.snake_positions = [(x+1, y)] + self.snake_positions[:-1]
   
    def eat(self):
            """과일을 먹었을 때 뱀 길이 증가에 대한 함수"""
            tail = self.snake_positions[-1]
            x, y = tail
            if self.snake_direction == 'UP':
                self.snake_positions.append((x, y-1))
            elif self.snake_direction == 'DOWN':
                self.snake_positions.append((x, y+1))
            elif self.snake_direction == 'LEFT':
                self.snake_positions.append((x-1, y))
            elif self.snake_direction == 'RIGHT':
                self.snake_positions.append((x+1, y))
   


class Fruit():
    def __init__(self):
        self.fruit_position = (0,0)
        self.place_fruit()
        
    def place_fruit(self):
        """과일 위치 랜덤 지정"""
        self.fruit_position = (random.randint(0, (SCREEN_WIDTH/PIXEL_SIZE)-1), random.randint(0, (SCREEN_WIDTH/PIXEL_SIZE)-1))
            
    def fruit_image(self):
        """과일 이미지 생성"""
        appleimage = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
        appleimage.fill(GREEN)
        screen.blit(appleimage, (self.fruit_position[0] * PIXEL_SIZE, self.fruit_position[1] * PIXEL_SIZE))
        


def run():
    global ToF, score

    snake = Snake()
    fruit = Fruit()
    
    while not ToF:
        clock.tick(FPS)
        
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [0, 0, SCREEN_WIDTH, LINE_WIDTH])
        pygame.draw.rect(screen, WHITE, [0, SCREEN_HEIGHT-LINE_WIDTH, SCREEN_WIDTH, LINE_WIDTH])
        pygame.draw.rect(screen, WHITE, [0, 0, LINE_WIDTH, SCREEN_HEIGHT])
        pygame.draw.rect(screen, WHITE, [SCREEN_WIDTH-LINE_WIDTH, 0, LINE_WIDTH, SCREEN_HEIGHT+LINE_WIDTH])
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ToF = True
            elif e.type == pygame.KEYDOWN:
                    # Key Quit
                    if e.key == pygame.K_ESCAPE:
                        ToF = True
                    elif e.key in DIRECTION:
                        snake.snake_direction = DIRECTION[e.key]

        snake.move()

        if snake.snake_positions[0] == fruit.fruit_position:
            snake.eat()
            fruit.place_fruit()
            score += 1
            
        score_text = font.render(str(score), False, WHITE)
        screen.blit(score_text, (5, 5))

        if snake.snake_positions[0] in snake.snake_positions[1:]:
            ToF = True           

        snake.snake_image()
        fruit.fruit_image()
    
        pygame.display.update()
    
run()
pygame.quit()