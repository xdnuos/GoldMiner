# -*- coding: utf-8 -*-
import pygame,sys,json
from define import *
from entities.miner import Miner
from entities.rope import Rope
from entities.gold import Gold
from entities.tnt import TNT
from entities.other import Other
from entities.rock import Rock
from entities.mole import Mole
from entities.explosive import Explosive
from entities.question import QuestionBag
clock = pygame.time.Clock()
# Kiểm tra va chạm giữa dây và item
def is_collision(rope, item):
    if rope.hoo.rect.colliderect(item.rect) and rope.state == 'expanding':
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
                self.manager.go_to(GameScene(1))
class FinishScene(object):

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
                self.manager.go_to(GameScene(1))
class SceneMananger(object):
    def __init__(self):
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
def load_item(item_data):
    item_name = item_data["type"]
    x = item_data["pos"]["x"]
    y = item_data["pos"]["y"]
    item = None
    match item_name:
        case "MiniGold":
            item = Gold(x,y,30,MiniGold_point)
        case "NormalGold":
            item = Gold(x,y,70,NormalGold_point)
        case "NormalGoldPlus":
            item = Gold(x,y,90,NormalGoldPlus_point)
        case "BigGold":
            item = Gold(x,y,150,BigGold_point)
        case "MiniRock":
            item = Rock(x,y,30,MiniRock_point)
        case "NormalRock":
            item = Rock(x,y,60,NormalRock_point)
        case "QuestionBag":
            item = QuestionBag(x,y)
        case "Diamond":
            item = Other(x,y,diamond_image,Diamond_point)
        case "Mole":
            item = Mole(x,y,mole_image,Mole_point,direction=item_data["dir"])
        case "MoleWithDiamond":
            item = Mole(x,y,mole2_image,Mole_point,direction=item_data["dir"])
        case "Skull":
            item = Other(x,y,skull_image,Skull_point)
        case "Bone":
            item = Other(x,y,bone_image,Bone_point)
        case "TNT":
            item = TNT(x,y)
        case _:
            item = None
    return item
def load_items(items_data):
    items = []
    for item in items_data:
        # if(item != None):
        items.append(load_item(item))
    return items
def load_level(level):
    bg_name = None
    bg = None
    file_path = "levels.game"
    try :
        with open(file_path, "r") as file:
            data = json.load(file)
        bg_name = data[level]['type']
        match bg_name:
            case "LevelA":
                bg = bgA
            case "LevelB":
                bg = bgB
            case "LevelC":
                bg = bgC
            case "LevelD":
                bg = bgD
            case "LevelE":
                bg = bgA
            case _:
                bg = bgA
    except:
        print("No file levels.game!")
        sys.exit(0)
    return bg,load_items(data[level]['entities'])
def random_level(level_number):
    ran_level = random.randint(1, 3)
    level_text  = "L"+str(level_number)+"_"+str(ran_level)
    return level_text
def draw_point(rope,dt,miner):
    if rope.text == "dynamite" and rope.text_direction !="None":
        rope.time_text -= dt
        if rope.x_text > 500:
            rope.text_size += dt*rope.speed /(5)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.4
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed /(25)
        if rope.time_text < 0:
            if rope.text_direction == "left":
                rope.x_text -= dt * rope.speed
                if rope.x_text <= 500:  # Reached left boundary, change direction
                    rope.text_direction = "right"
            elif rope.text_direction == "right":
                rope.x_text += dt * rope.speed
                if rope.x_text >= 700:  # Reached right boundary, change direction
                    rope.text_direction = "None"
        screen.blit(dynamite_image,(rope.x_text,10))
    elif rope.text == "strength" and rope.text_direction !="None":
        rope.time_text -= dt
        miner.yeah = True
        miner.start = 6
        miner.end = 8
        miner.current_frame = 6
        if rope.x_text > 400:
            rope.text_size += dt*rope.speed /(8)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.4
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed
        if rope.time_text < 0:
            if rope.text_direction == "left":
                rope.x_text -= dt * rope.speed
                if rope.x_text <= 400:  # Reached left boundary, change direction
                    rope.text_direction = "right"
            elif rope.text_direction == "right":
                rope.text_size -= dt*rope.speed /(5)
                if rope.text_size <= 0:  # Reached right boundary, change direction
                    miner.yeah = False
                    print(miner.yeah)
                    miner.start = 0
                    miner.end = 3
                    miner.current_frame = 0
                    rope.text_direction = "None"
        text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), int(rope.text_size))
        screen.blit(text_font.render("Sức mạnh", True, (0, 15, 0)), (rope.x_text, rope.y_text))
    elif rope.text != "" and rope.x_text > 120 and rope.text_direction !="None": # show tiền
        rope.time_text -= dt
        if rope.x_text > 500:
            rope.text_size += dt*rope.speed /(5)
        elif rope.text_size > 30 and rope.text_size < 46:
            rope.time_text = 0.2
            rope.text_size -= dt*rope.speed /(5)
        elif rope.text_size > 16 and rope.time_text < 0:
            rope.text_size -= dt*rope.speed /(25)
        if rope.time_text < 0:
            rope.x_text -= dt*rope.speed
        text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), int(rope.text_size))
        screen.blit(text_font.render("+$"+rope.text, True, (0, 15, 0)), (rope.x_text, rope.y_text))
class GameScene(Scene):
    def __init__(self, level):
        super(GameScene, self).__init__()
        self.level = level
        self.miner = Miner(miner_images, 620, -7, 5)
        self.rope = Rope(643, 45, 300,hoo_images)
        # self.bg,self.items = load_level(random_level(self.level))
        self.bg,self.items = load_level("LDEBUG")
        self.play_Explosive = False
        self.explosive = None
        self.text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 14)
        self.timer = 0
    def render(self, screen):            
        dt = clock.tick(60) / 1000
        if(self.miner.is_moving == True):
            for item in self.items:
                if is_collision(self.rope, item):
                    self.rope.item = item
                    self.rope.item.is_move = False
                    if item.is_explosive == True:
                        pygame.mixer.stop()
                        explosive_sound.play()
                        explosive_item(item,self.items)
                    self.rope.state = 'retracting'
                    self.items.remove(item)
                    break
        if(self.miner.is_moving == True and self.rope.state =="expanding"):
            self.miner.start =2
            self.miner.end =3
        elif self.miner.is_TNT == False and self.miner.yeah == False :
            self.miner.start =0
            self.miner.end =3
        #Blit
        screen.blit(bg_top,(0,0))
        screen.blit(self.bg,(0,72))

        #Draw item
        for item in self.items:
            item.draw(dt,screen)
        if(self.play_Explosive == True and self.explosive != None):
            pygame.mixer.stop()
            explosive_sound.play()
            self.explosive.draw(screen)
            self.explosive.update(dt)
            if (self.explosive.is_exit):
                del self.explosive
                self.play_Explosive = False
                self.miner.is_TNT = False
                self.miner.start =0 
                self.miner.end = 3
                self.miner.current_frame = 0
                self.rope.is_use_TNT = False
        for i in range(self.rope.have_TNT):
            screen.blit(dynamite_image,(725+i*25,10))
        #Update sprite
        self.miner.update(dt)
        self.miner.draw(screen)
        self.rope.update(self.miner,dt,screen)
        self.rope.draw(screen)
        draw_point(self.rope,dt,self.miner)
    def update(self):
        self.timer = 60 -int(pygame.time.get_ticks()/1000)
        screen.blit(self.text_font.render("Tiền:", True, (0, 0, 0)), (5, 0))
        screen.blit(self.text_font.render("$"+str(get_score()), True, (0, 150, 0)), (55, 0))
        screen.blit(self.text_font.render("Mục tiêu:", True, (0, 0, 0)), (5, 25))
        screen.blit(self.text_font.render("$"+str(goal), True, (255, 150, 0)), (96, 25))
        screen.blit(self.text_font.render("Thời gian:", True, (0, 0, 0)), (1140, 0))
        screen.blit(self.text_font.render(str(self.timer), True, (255, 100, 7)), (1240, 0))
        screen.blit(self.text_font.render("Cấp:", True, (0, 0, 0)), (1140, 25))
        screen.blit(self.text_font.render(str(self.level), True, (255, 100, 7)), (1190, 25))
    def handle_events(self, events):
        # if(self.timer <0):
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    # pygame.quit()
                    # sys.exit(0)
                    pygame.time.wait(2000)
                if e.key == pygame.K_SPACE and self.rope.timer <=0:
                    self.miner.is_moving = True
                if e.key == pygame.K_c:
                    if(self.rope.have_TNT > 0 and self.rope.item != None):
                        self.rope.is_use_TNT = True
                        self.miner.start = 3
                        self.miner.end = 5
                        self.miner.current_frame = 3
                        self.explosive = Explosive(self.rope.x2-128, self.rope.y2-128, 12)
                        self.play_Explosive = True
                        self.rope.have_TNT -=1
                        self.rope.length = 50
                        self.miner.is_TNT = True
                