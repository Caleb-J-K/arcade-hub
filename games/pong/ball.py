import pygame

BALL_RADIUS = 10
BALL_COLOR = (255, 255, 255)
BALL_SPEED = 500  # Pixels per second

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BALL_RADIUS
        self.color = BALL_COLOR
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, delta_time):
        self.x += self.speed_x * delta_time
        self.y += self.speed_y * delta_time

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def reset_position(self, x, y, x_direction):
        self.x = x
        self.y = y
        self.speed_x = abs(self.speed_x) * x_direction  # Reset the horizontal direction of the ball