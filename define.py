import pygame
import random
import math
import os
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
empty = pygame.image.load('./assets/images/empty.png')
# Question Bag
questionBag = pygame.image.load('./assets/images/question_bag.png')
#dynamite
dynamite_image = pygame.image.load('./assets/images/dynamite.png')
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

pygame.mixer.pre_init(frequency=11025, size=-16, channels=2, buffer=2048)
pygame.init()
explosive_sound = pygame.mixer.Sound('./assets/audios/explosive.wav')
goal_sound = pygame.mixer.Sound('./assets/audios/goal.wav')
grab_back_sound = pygame.mixer.Sound('./assets/audios/grab_back.wav')
grab_start_sound = pygame.mixer.Sound('./assets/audios/grab_start.wav')
hook_reset_sound = pygame.mixer.Sound('./assets/audios/hook_reset.wav')
high_value_sound = pygame.mixer.Sound('./assets/audios/high_value.wav')
normal_value_sound = pygame.mixer.Sound('./assets/audios/normal_value.wav')
money_sound = pygame.mixer.Sound('./assets/audios/money.wav')
MiniGold_point = 50
NormalGold_point  = 100
NormalGoldPlus_point = 250
BigGold_point = 500
MiniRock_point = 11
NormalRock_point = 20
BigRock_point = 100
Diamond_point = 600
Mole_point = 2
MoleWithDiamond_point = 602
Skull_point = 20
Bone_point = 7

score = 0
goal = 650
# goalAddOn = 270
def get_score():
    return score

def set_score(new_score):
    global score
    score = new_score
