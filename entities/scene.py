import pygame
from define import *
import random
from game import GoldMinerGame
clock = pygame.time.Clock()

class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError
class TitleScene(object):

    def __init__(self):
        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 56)
        self.sfont = pygame.font.SysFont('Arial', 32)

    def render(self, screen):
        # beware: ugly! 
        screen.fill((0, 200, 0))
        text1 = self.font.render('Crazy Game', True, (255, 255, 255))
        text2 = self.sfont.render('> press space to start <', True, (255, 255, 255))
        screen.blit(text1, (200, 50))
        screen.blit(text2, (200, 350))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                print("ok")
                self.manager.go_to(GameScene(0))
class SceneMananger(object):
    def __init__(self):
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
class GameScene(Scene):
    def __init__(self, level):
        super(GameScene, self).__init__()
        items = []
        items.extend(Gold(50) for _ in range(5))
        # items.append(Mole(500,200,mole_image,50))
        items.append(TNT(700,500))
        miner = Miner(miner_images, 620, -7, 5)
        rope = Rope(643, 45, 300,hoo_images)
        self.game = GoldMinerGame(miner,rope,items)
    def render(self, screen):
        self.game.run(screen)
    def update(self):
        pass
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pass #somehow go back to menu