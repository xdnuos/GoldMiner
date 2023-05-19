import pygame
from define import *
from entities.explosive import Explosive
import math
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

class GoldMinerGame:
    def __init__(self,miner,rope,items):
        self.miner = miner
        self.items = items
        self.rope = rope
        self.explosive = None
        self.play_Explosive = False
    def run(self, screen):
        while running:
            dt = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.miner.is_moving = True
                    if event.key == pygame.K_c:
                        if(self.rope.have_TNT > 0 and self.rope.item != None):
                            self.rope.is_use_TNT = True
                            self.miner.time = 3
                            self.miner.start = 3
                            self.miner.end = 5
                            explosive = Explosive(self.rope.x2-128, self.rope.y2-128, 12)
                            play_Explosive = True
                            self.rope.have_TNT -=1
                            self.rope.length = 50
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
            if(play_Explosive == True and explosive != None):
                explosive.draw(screen)
                explosive.update(dt)
                if (explosive.is_exit):
                    del explosive
                    self.miner.start = 0
                    self.miner.end = 3
                    play_Explosive = False
            self.miner.update(dt)
            self.miner.draw(screen)
            self.rope.update(self.miner,dt,screen)
            self.rope.draw(screen)
            pygame.display.flip()