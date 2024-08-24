import pygame
import constants
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
while (1 + 1) == 2:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return
    screen.fill(000)
    pygame.display.flip()