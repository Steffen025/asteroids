import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
            
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()  # Remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        pos_ateroid = Asteroid(self.position[0], self.position[1], new_radius)
        pos_ateroid.velocity = pygame.Vector2(self.velocity).rotate(random_angle) * 1.3
        neg_ateroid = Asteroid(self.position[0], self.position[1], new_radius)
        neg_ateroid.velocity = pygame.Vector2(self.velocity).rotate(-random_angle) * 1.3