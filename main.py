from scenes.game_scenes import *

def main():
    pygame.init()
    running = True
    manager = SceneMananger()
    font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 28)
    while running:
        if pygame.event.get(pygame.QUIT):
            running = False
            return
        manager.scene.handle_events(pygame.event.get())
        if get_pause() == False:
            manager.scene.render(screen)
            manager.scene.update(screen)
        else:
            screen.blit(panel_image,panel_image.get_rect(center = (screen_width/2,screen_height/2)))
            text = font.render('Bấm phím Space để tiếp tục', True, (255, 255, 255))
            screen.blit(text,text.get_rect(center = (screen_width/2,screen_height/2)))
        pygame.display.flip()

if __name__ == "__main__":
    main()