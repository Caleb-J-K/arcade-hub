import pygame
from games.pong import ball
from games.pong.paddle import Paddle, PADDLE_WIDTH, PADDLE_HEIGHT


PONG_BACKGROUND_COLOR = (0, 0, 0)
PONG_LINE_COLOR = (255, 255, 255)
PADDLE_X_MARGIN = 50  # Distance from the edge of the screen to the paddle
PADDLE_Y_BOUNDARY = 20  # Distance from the top and bottom of the screen to the paddle
PONG_BOUNDARY_THICKNESS = 10  # Thickness of the top and bottom boundaries
WINNING_SCORE = 1
PONG_TEXT_COLOR = (0, 255, 0)


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
        ball_x_start = screen.get_width() // 2
        ball_y_start = screen.get_height() // 2
        self.ball = ball.Ball(ball_x_start, ball_y_start)
        self.left_score = 0
        self.right_score = 0
        self.score_font = pygame.font.Font(None, 48)
        self.game_over = False
        self.winner = None


    def update(self, delta_time):


        if self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.reset_game()
            return

        
        left_direction = 0
        right_direction = 0
        keys = pygame.key.get_pressed()


        # Left paddle controls
        if keys[pygame.K_w]:
            left_direction -= 1
        if keys[pygame.K_s]:
            left_direction += 1


        # Right paddle controls
        if keys[pygame.K_UP]:
            right_direction -= 1
        if keys[pygame.K_DOWN]:
            right_direction += 1


        self.left_paddle.move(left_direction, delta_time, self.min_y, self.max_y)
        self.right_paddle.move(right_direction, delta_time, self.min_y, self.max_y)


        self.ball.move(delta_time)
        top_edge = self.ball.y - self.ball.radius
        bottom_edge = self.ball.y + self.ball.radius


        if bottom_edge > self.screen.get_height() - PONG_BOUNDARY_THICKNESS: 
            self.ball.speed_y = abs(self.ball.speed_y) * -1  # Reverse the vertical direction of the ball
            self.ball.y = self.screen.get_height() - PONG_BOUNDARY_THICKNESS - self.ball.radius # Moves ball back into play if it goes below the bottom boundary


        if top_edge < PONG_BOUNDARY_THICKNESS: 
            self.ball.speed_y = abs(self.ball.speed_y) 
            self.ball.y = PONG_BOUNDARY_THICKNESS + self.ball.radius 


        ball_rect = self.ball.get_rect()
        left_paddle_rect = self.left_paddle.get_rect()
        right_paddle_rect = self.right_paddle.get_rect()


        # Check for collision with paddles and reverse the ball's direction if it collides while also ensuring the ball is not already past the paddle to avoid multiple collisions in one frame
        if ball_rect.colliderect(left_paddle_rect) and self.ball.speed_x < 0 and self.ball.x > left_paddle_rect.right:
            self.ball.speed_x *= -1 
            self.ball.x = left_paddle_rect.right + self.ball.radius 
        if ball_rect.colliderect(right_paddle_rect) and self.ball.speed_x > 0 and self.ball.x < right_paddle_rect.left:
            self.ball.speed_x *= -1
            self.ball.x = right_paddle_rect.left - self.ball.radius


        # Check for scoring conditions and reset the ball's position if it goes past the left or right edge of the screen, while also updating the score and checking for a winner
        if self.ball.x < 0:
            self.ball.reset_position(self.screen.get_width() // 2, self.screen.get_height() // 2, x_direction=1)
            self.right_score += 1
            if self.right_score >= WINNING_SCORE:
                self.game_over = True


        elif self.ball.x > self.screen.get_width():
            self.ball.reset_position(self.screen.get_width() // 2, self.screen.get_height() // 2, x_direction=-1)
            self.left_score += 1
            if self.left_score >= WINNING_SCORE:
                self.game_over = True


    # Draws the playfield, scores, paddles, ball, and game over message if applicable
    def draw(self):
        draw_playfield(self.screen)
        left_score_text = self.score_font.render(str(self.left_score), True, PONG_LINE_COLOR)
        right_score_text = self.score_font.render(str(self.right_score), True, PONG_LINE_COLOR)
        self.screen.blit(left_score_text, (self.screen.get_width() // 4 - left_score_text.get_width() // 2, 20))
        self.screen.blit(right_score_text, (3 * self.screen.get_width() // 4 - right_score_text.get_width() // 2, 20))
        self.left_paddle.draw(self.screen)
        self.right_paddle.draw(self.screen)
        self.ball.draw(self.screen)


        if self.game_over:
            winner_text = "Left Player Wins!" if self.left_score > self.right_score else "Right Player Wins!"
            winner_surface = self.score_font.render(winner_text, True, PONG_TEXT_COLOR)
            self.screen.blit(winner_surface, (self.screen.get_width() // 2 - winner_surface.get_width() // 2, self.screen.get_height() // 4 - winner_surface.get_height() // 2))
            self.screen.blit(self.score_font.render("Press SPACE to restart", True, PONG_LINE_COLOR), (self.screen.get_width() // 2 - self.score_font.size("Press SPACE to restart")[0] // 2, self.screen.get_height() // 4 + winner_surface.get_height() // 2 + 10))


    def reset_game(self):
        self.left_score = 0
        self.right_score = 0
        self.game_over = False
        self.winner = None
        self.ball.reset_position(self.screen.get_width() // 2, self.screen.get_height() // 2, x_direction=1)
        self.left_paddle.reset_position(self.screen.get_height() // 2 - PADDLE_HEIGHT // 2)
        self.right_paddle.reset_position(self.screen.get_height() // 2 - PADDLE_HEIGHT // 2)


def draw_playfield(screen):
    
    screen.fill(PONG_BACKGROUND_COLOR)

    # Draw the center line
    pygame.draw.line(screen, PONG_LINE_COLOR, (screen.get_width() // 2, 0), (screen.get_width() // 2, screen.get_height()), 5)

    # Draw the top and bottom boundaries
    pygame.draw.rect(screen, PONG_LINE_COLOR, (0, 0, screen.get_width(), PONG_BOUNDARY_THICKNESS))
    pygame.draw.rect(screen, PONG_LINE_COLOR, (0, screen.get_height() - PONG_BOUNDARY_THICKNESS, screen.get_width(), PONG_BOUNDARY_THICKNESS))
