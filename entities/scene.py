import pygame,sys
from define import *
import random
from entities.miner import Miner
from entities.rope import Rope
from entities.gold import Gold
from entities.tnt import TNT
from entities.other import Other
from entities.rock import Rock
from entities.mole import Mole
from entities.explosive import Explosive
clock = pygame.time.Clock()
# Kiểm tra va chạm giữa dây và item
def is_collision(rope, item):
    if rope.hoo.rect.colliderect(item.rect):
        return True
    return False
def explosive_item(tnt, items):
    items_to_remove = []
    for item in items:
        if item == tnt:
            continue
        if math.sqrt(pow(abs(item.x-tnt.x),2) + pow(abs(item.y-tnt.y),2)) < 200:
            items_to_remove.append(item)
    for item in items_to_remove:
        items.remove(item)
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
        self.miner = Miner(miner_images, 620, -7, 5)
        self.rope = Rope(643, 45, 300,hoo_images)
        self.items = []
        # add item
        self.items.extend(Gold(50) for _ in range(5))
        self.items.append(TNT(700,500))

        #other
        self.play_Explosive = False
        self.explosive = None
    def render(self, screen):
        dt = clock.tick(60) / 1000
        if(self.miner.is_moving == True):
            for item in self.items:
                if is_collision(self.rope, item):
                    self.rope.item = item
                    self.rope.item.is_move = False
                    if item.is_explosive == True:
                        explosive_item(item,self.items)
                    self.rope.state = 'retracting'
                    self.items.remove(item)
                    break
        
        screen.blit(bg_top,(0,0))
        screen.blit(bgA,(0,72))
        for item in self.items:
            item.draw(dt,screen)
        if(self.play_Explosive == True and self.explosive != None):
            self.explosive.draw(screen)
            self.explosive.update(dt)
            if (self.explosive.is_exit):
                del self.explosive
                self.miner.start = 0
                self.miner.end = 3
                self.play_Explosive = False
        self.miner.update(dt)
        self.miner.draw(screen)
        self.rope.update(self.miner,dt,screen)
        self.rope.draw(screen)
    def update(self):
        pass
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                if e.key == pygame.K_SPACE:
                    self.miner.is_moving = True
                if e.key == pygame.K_c:
                    if(self.rope.have_TNT > 0 and self.rope.item != None):
                        self.rope.is_use_TNT = True
                        self.miner.time = 3
                        self.miner.start = 3
                        self.miner.end = 5
                        self.explosive = Explosive(self.rope.x2-128, self.rope.y2-128, 12)
                        self.play_Explosive = True
                        self.rope.have_TNT -=1
                        self.rope.length = 50
                