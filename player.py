from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Player's rotation angle
        self.cooldown = 0  # Cooldown for shooting
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, width=2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt) # Rotate right
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.cooldown -= dt
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        if self.cooldown <= 0:
            shot = Shot(self.position)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
            self.cooldown = SHOT_COOLDOWN  # Reset cooldown
            return shot