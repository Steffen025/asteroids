import pygame
from constants import *

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        Clock.tick(60) # Limit the frame rate to 60 FPS
        dt = Clock.tick(60) / 1000.0
        # Here you would typically update game state and draw objects
        pygame.display.flip()
        
    

if __name__ == "__main__":
    main()
