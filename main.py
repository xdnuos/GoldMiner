import pygame
from entities.scene import *

# def main():
#     items = []
#     items.extend(Gold(50) for _ in range(5))
#     # items.append(Mole(500,200,mole_image,50))
#     items.append(TNT(700,500))
#     miner = Miner(miner_images, 620, -7, 5)
#     rope = Rope(643, 45, 300,hoo_images)
#     explosive = None
#     play_Explosive = False
#     running = True
#     while running:
#         dt = clock.tick(60) / 1000
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     miner.is_moving = True
#                 if event.key == pygame.K_c:
#                     if(rope.have_TNT > 0 and rope.item != None):
#                         rope.is_use_TNT = True
#                         miner.time = 3
#                         miner.start = 3
#                         miner.end = 5
#                         explosive = Explosive(rope.x2-128, rope.y2-128, 12)
#                         play_Explosive = True
#                         rope.have_TNT -=1
#                         rope.length = 50
#         if(miner.is_moving == True):
#             for item in items:
#                 if is_collision(rope, item):
#                     rope.item = item
#                     rope.item.is_move = False
#                     if item.is_explosive == True:
#                         explosive_item(item,items)
#                     rope.state = 'retracting'
#                     items.remove(item)
#                     break
        
#         screen.blit(bg_top,(0,0))
#         screen.blit(bgA,(0,72))
#         for item in items:
#             item.draw(dt,screen)
#         if(play_Explosive == True and explosive != None):
#             explosive.draw(screen)
#             explosive.update(dt)
#             if (explosive.is_exit):
#                 del explosive
#                 miner.start = 0
#                 miner.end = 3
#                 play_Explosive = False
#         miner.update(dt)
#         miner.draw(screen)
#         rope.update(miner,dt,screen)
#         rope.draw(screen)
#         pygame.display.flip()
#     pygame.quit()
#     sys.exit()
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