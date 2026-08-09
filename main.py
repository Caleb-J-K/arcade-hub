import pygame
from games.pong.pong import Pong

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS_LIMIT = 60
BACKGROUND_COLOR = (0, 0, 0)
ACTIVE_GAME = "Pong"

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Arcade Hub")
    clock = pygame.time.Clock()
    pong_game = Pong(screen)
    running = True



    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if ACTIVE_GAME == "Pong":
            pong_game.draw()
        else:
            screen.fill(BACKGROUND_COLOR)

        pygame.display.flip()

        clock.tick(FPS_LIMIT)

    pygame.quit()

if __name__ == "__main__":
    main()