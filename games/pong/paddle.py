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

    def move(self, screen,direction, delta_time):
        if direction == "up":
            self.y -= self.speed * delta_time
        elif direction == "down":
            self.y += self.speed * delta_time

        # Ensure the paddle stays within the screen bounds
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > screen.get_height():
            self.y = screen.get_height() - self.height