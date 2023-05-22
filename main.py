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
        manager.scene.render(screen)
        manager.scene.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()