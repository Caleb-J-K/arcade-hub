import pygame


PADDLE_WIDTH = 10 
PADDLE_HEIGHT = 100
PADDLE_COLOR = (255, 255, 255)
PADDLE_SPEED = 240  # Pixels per second
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = PADDLE_COLOR
        self.speed = PADDLE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction, delta_time, min_y, max_y):
        self.y += direction * self.speed * delta_time
        if self.y < min_y:
            self.y = min_y
        elif self.y > max_y:
            self.y = max_y