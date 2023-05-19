import pygame
import random
import math
# load hình ảnh vào pygame
def load_images(filepaths,is2x = False):
    images = []
    for filepath in filepaths:
        image = pygame.image.load(filepath).convert_alpha()
        if is2x:
            image = pygame.transform.scale2x(image)
        images.append(image)
    return images

screen_width = 1280
screen_height = 820
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Gold Miner Classic")

#init Gold
gold_image = pygame.image.load("./assets/images/gold.png")
#init Rock
rock_image = pygame.image.load("./assets/images/rock.png")
#init Mole
mole_image = pygame.image.load("./assets/images/mole.png")
#init Mole with Diamond
mole2_image = pygame.image.load("./assets/images/moleDiamond.png")
#init Skull
skull_image = pygame.image.load("./assets/images/skull.png")
#init Bone
bone_image = pygame.image.load("./assets/images/bone.png")
#init Diamond
diamond_image = pygame.image.load("./assets/images/diamond.png")
#init TNT
tnt_image = pygame.image.load("./assets/images/tnt.png")
# empty
empty = pygame.image.load('./assets/images/empty.png').convert()
# Question Bag
questionBag = pygame.image.load('./assets/images/question_bag.png').convert()

#init miner
miner_files = [
    "./assets/images/miner_01.png",
    "./assets/images/miner_02.png",
    "./assets/images/miner_03.png",
    "./assets/images/miner_04.png",
    "./assets/images/miner_05.png",
    "./assets/images/miner_06.png",
    "./assets/images/miner_07.png",
    "./assets/images/miner_08.png"
]
miner_images = load_images(miner_files)
#init explosive
explosive_files = [
    "./assets/images/ex1.png",
    "./assets/images/ex2.png",
    "./assets/images/ex3.png",
    "./assets/images/ex4.png",
    "./assets/images/ex5.png",
    "./assets/images/ex6.png",
    "./assets/images/ex7.png",
    "./assets/images/ex8.png",
    "./assets/images/ex9.png"
]
explosive_images = load_images(explosive_files,True)

#init empties
empty_files = [
    "./assets/images/empty.png"
]
empty_images = load_images(empty_files,True)
#init hoo
hoo_files = [
    "./assets/images/hoo_01.png",
    "./assets/images/hoo_02.png",
    "./assets/images/hoo_03.png"
]
hoo_images = load_images(hoo_files)

#init BG
bgA = pygame.image.load('./assets/images/bg_level_A.jpg').convert()
bgA = pygame.transform.scale2x(bgA)
bgB = pygame.image.load('./assets/images/bg_level_B.jpg').convert()
bgB = pygame.transform.scale2x(bgB)
bgC = pygame.image.load('./assets/images/bg_level_C.jpg').convert()
bgC = pygame.transform.scale2x(bgC)
bgD = pygame.image.load('./assets/images/bg_level_D.jpg').convert()
bgD = pygame.transform.scale2x(bgD)
bg_top = pygame.image.load('./assets/images/bg_top.png').convert()



MiniGold = 50
NormalGold  = 100
NormalGoldPlus = 250
BigGold = 500
MiniRock = 11
NormalRock = 20
BigRock = 100
Diamond = 600
Mole = 2
MoleWithDiamond = 602
Skull = 20
Bone = 7
