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
from entities.button import Button
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
class StartScene(object):
    def __init__(self):
        super(StartScene, self).__init__()
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 48)
        self.button = Button(120,20,gold_image,2)
        self.higt_score_btn = Button(80,500,hight_score,1)
    def render(self, screen):
        screen.blit(start_BG,(0,0))
        if self.button.draw(screen):
            self.start()
        if self.higt_score_btn.draw(screen):
            pass
        screen.blit(miner_menu,miner_menu_rect)
        text = self.font.render('Chơi', True, (255, 255, 255))
        screen.blit(text, (250, 160))
    def update(self):
        pass
    def start(self):
        set_time(pygame.time.get_ticks()/1000)
        self.manager.go_to(GameScene(get_level()))
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.start()
class FinishScene(object):
    def __init__(self):
        super(FinishScene, self).__init__()
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 28)
    def render(self, screen):
        screen.blit(cut_scene,(0,0))
        screen.blit(panel_image,panel_image.get_rect(center = (screen_width/2,screen_height/2)))
        text = self.font.render('Level Up!', True, (255, 255, 255))
        screen.blit(text, text.get_rect(center = (screen_width/2,screen_height/2-28)))
        text2 = self.font.render('Nhấn phím Space để tiếp tục', True, (255, 255, 255))
        screen.blit(text2, text2.get_rect(center = (screen_width/2,screen_height/2 +28)))
    def update(self):
        pass
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                set_time(pygame.time.get_ticks()/1000)
                self.manager.go_to(GameScene(get_level()))
class FailureScene(object):
    def __init__(self):
        super(FailureScene, self).__init__()
        self.font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 24)
    def render(self, screen):
        screen.blit(cut_scene,(0,0))
        screen.blit(panel_image,panel_image.get_rect(center = (screen_width/2,screen_height/2)))
        text = self.font.render('Bạn đã không đạt đủ điểm yêu cầu!', True, (255, 255, 255))
        text2 = self.font.render('Bấm phím Space để chơi lại', True, (255, 255, 255))
        screen.blit(text, text.get_rect(center = (screen_width/2,screen_height/2 - 20 )))
        screen.blit(text2, text2.get_rect(center = (screen_width/2,screen_height/2 + 20)))
    def update(self):
        pass
    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.manager.go_to(StartScene())
class SceneMananger(object):
    def __init__(self):
        self.go_to(StartScene())
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
            item = Mole(x,y,mole2_image,MoleWithDiamond_point,direction=item_data["dir"])
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
        miner.state = 3
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
                    miner.state = 3
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
    def __init__(self, level,tnt=0,speed=1):
        super(GameScene, self).__init__()
        self.level = level
        self.miner = Miner(miner_images, 620, -7, 5)
        self.rope = Rope(643, 45, 300,hoo_images)
        self.bg,self.items = load_level(random_level(self.level))
        # self.bg,self.items = load_level("LDEBUG")
        self.play_Explosive = False
        self.explosive = None
        self.text_font = pygame.font.Font(os.path.join("assets", "fonts", 'Fernando.ttf'), 14)
        self.timer = 0
        self.pause_time = 0
        self.pause = False
    def render(self, screen):            
        dt = clock.tick(60) / 1000
        if(self.miner.state == 1):
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
        if self.rope.state == 'retracting' and not(self.rope.is_use_TNT):
            self.miner.state = 2
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
                self.miner.state = 0
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
        self.timer = 60 - 10*int(pygame.time.get_ticks()/1000 - get_time())
        screen.blit(self.text_font.render("Tiền:", True, (0, 0, 0)), (5, 0))
        screen.blit(self.text_font.render("$"+str(get_score()), True, (0, 150, 0)), (55, 0))
        screen.blit(self.text_font.render("Mục tiêu:", True, (0, 0, 0)), (5, 25))
        screen.blit(self.text_font.render("$"+str(get_goal()), True, (255, 150, 0)), (96, 25))
        screen.blit(self.text_font.render("Thời gian:", True, (0, 0, 0)), (1140, 0))
        screen.blit(self.text_font.render(str(self.timer), True, (255, 100, 7)), (1240, 0))
        screen.blit(self.text_font.render("Cấp:", True, (0, 0, 0)), (1140, 25))
        screen.blit(self.text_font.render(str(self.level), True, (255, 100, 7)), (1190, 25))
    def next_level(self):
        if get_score() > get_goal():
            set_level(get_level()+1)
            set_goal(get_goal()+get_level()*goalAddOn)
            self.manager.go_to(FinishScene())
        else:
            set_level(1)
            set_goal(650)
            self.manager.go_to(FailureScene())
    def handle_events(self, events):
        if(self.timer <0):
            self.next_level()
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE: #PAUSE and UNPAUSE
                    self.pause = not(self.pause)
                    if self.pause: #PAUSE
                        self.pause_time = pygame.time.get_ticks()/1000
                        set_pause(True)
                    else: #UNPAUSE
                        set_pause(False)
                        set_time(get_time() + pygame.time.get_ticks()/1000 - self.pause_time)
                if e.key == pygame.K_ESCAPE: #ESC -->tesst
                    self.next_level()
                if e.key == pygame.K_DOWN and self.rope.timer <=0: # expanding
                    self.miner.state = 1
                if e.key == pygame.K_UP: # retracting
                    if(self.rope.have_TNT > 0 and self.rope.item != None):
                        self.rope.is_use_TNT = True
                        self.miner.state = 4
                        self.explosive = Explosive(self.rope.x2-128, self.rope.y2-128, 12)
                        self.play_Explosive = True
                        self.rope.have_TNT -=1
                        self.rope.length = 50
                        self.miner.is_TNT = True
                