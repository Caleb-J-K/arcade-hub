import pygame

PONG_BACKGROUND_COLOR = (0, 0, 0)
PONG_LINE_COLOR = (255, 255, 255)

class Pong:
    def __init__(self, screen):
        self.screen = screen
    def draw(self):
        draw_playfield(self.screen)

def draw_playfield(screen):
    # Draw the playfield background
    screen.fill(PONG_BACKGROUND_COLOR)

    # Draw the center line
    pygame.draw.line(screen, PONG_LINE_COLOR, (screen.get_width() // 2, 0), (screen.get_width() // 2, screen.get_height()), 5)

    # Draw the top and bottom boundaries
    pygame.draw.rect(screen, PONG_LINE_COLOR, (0, 0, screen.get_width(), 10))  # Top boundary
    pygame.draw.rect(screen, PONG_LINE_COLOR, (0, screen.get_height() - 10, screen.get_width(), 10))  # Bottom boundary


