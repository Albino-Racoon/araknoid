import pygame

from Platform import Platform
from Ball import Ball

# height and width of the screen
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
lives = 3

# pygame settings
pygame.init()
pygame.font.init()

# font, display, clock and background objects
font = pygame.font.SysFont('Comic Sans MS', 24)
display = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
background_image = pygame.image.load('images/background.png')

# platform object
platform = Platform()
# ball object
ball = Ball()

# main game loop
game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
        elif event.type == pygame.QUIT:
            game_on = False

    # platform controls
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        platform.move_platform(-1)
    if pressed_keys[pygame.K_d]:
        platform.move_platform(1)

    # ball update
    ball.update(platform)

    # checking if ball has touched the lower edge of the screen
    if ball.lost:
        lives -= 1
        if lives <= 0:
            break
        ball.reset_position()
        platform.reset_position()

    # platform update
    platform.update()

    # display background
    display.blit(background_image, (0, 0))

    # display the player and the ball
    display.blit(platform.image, platform.position)
    display.blit(ball.image, ball.position)

    # render score
    text = font.render(
        f'Lives: {lives}', False, (255, 0, 255))
    display.blit(text, (16, 16))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
