import pygame
from asteroidfield import *
from constants import *
from player import *
from asteroid import *
from shot import *
shots = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Shot.containers = (drawable, updatable, shots)
AsteroidField.containers = (updatable)
Asteroid.containers = (asteroids, drawable, updatable)
def main():
        dt = 0
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock_variable = pygame.time.Clock()
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        updatable.add(player)
        drawable.add(player)
        asteroid_field = AsteroidField()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
            screen.fill((0, 0, 0))
            for item in drawable:
                item.draw(screen)
            pygame.display.flip()
            dt = clock_variable.tick(60) / 1000
            updatable.update(dt)
            for asteroid in asteroids:
                 if asteroid.collision(player) == True:
                      print("Game Over!")
                      running = False
        pygame.quit()

if __name__ == "__main__":
    main()