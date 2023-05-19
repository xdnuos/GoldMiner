import pygame
from entities.scene import *

def main():
    pygame.init()
    running = True

    manager = SceneMananger()

    while running:
        if pygame.event.get(pygame.QUIT):
            running = False
            return
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()