import pygame
import sys
import random

# Размер окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Размер блока и скорость змейки
BLOCK_SIZE = 20
SNAKE_SPEED = 10


# Класс змейки
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (0, 0)

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        dx, dy = self.direction
        new_tail = (tail[0] - dx, tail[1] - dy)
        self.body.append(new_tail)

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    # проверяем на столкновение
    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return True
        for segment in self.body[1:]:
            if head == segment:
                return True
        return False


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))



# Класс игры
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = self.spawn_food()
        self.score = 0
        self.walls = []

        for _ in range(5):  # Можно задать любое количество стен
            wall = self.spawn_wall()
            self.walls.append(wall)

    def spawn_wall(self):
        while True:
            wall = Wall(random.randrange(0, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                        random.randrange(0, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)
            if wall not in self.snake.body and wall != self.food:  # Убеждаемся, что стена не находится на змейке или на еде
                return wall

    def draw_walls(self, screen):
        for wall in self.walls:
            wall.draw(screen)

    def spawn_food(self):
        while True:
            food = (random.randrange(0, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                    random.randrange(0, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)
            if food not in self.snake.body:
                return food

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Змейка')
        clock = pygame.time.Clock()

        # Загрузка шрифта для отображения счетчика
        font = pygame.font.Font(None, 36)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.direction = (0, -BLOCK_SIZE)
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = (0, BLOCK_SIZE)
                    elif event.key == pygame.K_LEFT:
                        self.snake.direction = (-BLOCK_SIZE, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = (BLOCK_SIZE, 0)

            if self.snake.body[0] == self.food:
                self.snake.grow()
                self.food = self.spawn_food()
                self.score += 1  # Увеличиваем счетчик при съедении яблока

            self.snake.move()

            # Проверка на столкновение с едой
            if self.snake.check_collision():
                pygame.quit()
                sys.exit()

            # Проверка на столкновение со стенами
            head = self.snake.body[0]
            if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
                pygame.quit()
                sys.exit()

            # Проверка на столкновение с стенами
            for wall in self.walls:
                if head[0] == wall.x and head[1] == wall.y:
                    pygame.quit()
                    sys.exit()

            screen.fill(BLACK)
            self.snake.draw(screen)
            self.draw_walls(screen)  # Отрисовка стен
            pygame.draw.rect(screen, RED, (self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))

            # отображение счетчика
            score_text = font.render(f'Счет: {self.score}', True, WHITE)
            screen.blit(score_text, (10, 10))

            pygame.display.update()
            clock.tick(SNAKE_SPEED)

        # Создаем объект игры и запускаем игровой цикл


game = Game()
game.main()
