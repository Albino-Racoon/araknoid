import pygame
import random

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
vec = pygame.math.Vector2


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.image = pygame.image.load("images/ball.png")
        self.reset_position()
        self.r = 16
        self.lost = False

    # resetting position
    def reset_position(self):
        self.coordinates = vec(SCREEN_WIDTH/2, SCREEN_HEIGHT-140)
        self.position = self.image.get_rect(center=self.coordinates)
        self.vector = vec(0, -10)
        self.incline_angle = random.randrange(-30, 30)
        self.vector.rotate_ip(self.incline_angle)
        self.lost = False

    # update
    def update(self, platform):
        self.coordinates += self.vector
        self.position.center = self.coordinates
        self.check_collision(platform)

    # check all possible collisions
    def check_collision(self, platform):
        # screen edges
        if self.position.x <= 0:
            self.vector.x *= -1
        if self.position.right >= SCREEN_WIDTH:
            self.vector.x *= -1
        if self.position.top <= 0:
            self.vector.y *= -1
        if self.position.bottom >= SCREEN_HEIGHT:
            self.lost = True

        # platform
        if self.position.colliderect(platform.position):
            self.vector.y *= -1
            self.vector.x += platform.moving*5
            if self.vector.x < -10:
                self.vector.x = -10
            if self.vector.x > 10:
                self.vector.x = 10
