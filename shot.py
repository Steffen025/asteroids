from constants import *
from circleshape import CircleShape
import pygame


class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position[0], position[1], SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        