import pygame
from games.pong.paddle import Paddle, PADDLE_WIDTH, PADDLE_HEIGHT

PONG_BACKGROUND_COLOR = (0, 0, 0)
PONG_LINE_COLOR = (255, 255, 255)
PADDLE_X_MARGIN = 50  # Distance from the edge of the screen to the paddle
PADDLE_Y_BOUNDARY = 20  # Distance from the top and bottom of the screen to the paddle


class Pong:
    def __init__(self, screen):
        self.screen = screen
        paddle_y = screen.get_height() // 2 - PADDLE_HEIGHT // 2
        left_paddle_x = PADDLE_X_MARGIN
        self.left_paddle = Paddle(left_paddle_x, paddle_y)
        right_paddle_x = screen.get_width() - PADDLE_X_MARGIN - PADDLE_WIDTH
        self.right_paddle = Paddle(right_paddle_x, paddle_y)
        self.max_y = screen.get_height() - PADDLE_HEIGHT - PADDLE_Y_BOUNDARY
        self.min_y = PADDLE_Y_BOUNDARY

    def update(self, delta_time):
        self.left_paddle.move(-1, delta_time, self.min_y, self.max_y)  # Move left paddle up

    def draw(self):
        draw_playfield(self.screen)
        self.left_paddle.draw(self.screen)
        self.right_paddle.draw(self.screen)

def draw_playfield(screen):
    # Draw the playfield background
    screen.fill(PONG_BACKGROUND_COLOR)

    # Draw the center line
    pygame.draw.line(screen, PONG_LINE_COLOR, (screen.get_width() // 2, 0), (screen.get_width() // 2, screen.get_height()), 5)

    # Draw the top and bottom boundaries
    pygame.draw.rect(screen, PONG_LINE_COLOR, (0, 0, screen.get_width(), 10))  # Top boundary
    pygame.draw.rect(screen, PONG_LINE_COLOR, (0, screen.get_height() - 10, screen.get_width(), 10))  # Bottom boundary


