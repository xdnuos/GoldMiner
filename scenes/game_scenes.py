# -*- coding: utf-8 -*-
import pygame,sys
from entities.miner import Miner
from entities.rope import Rope
from entities.explosive import Explosive
from entities.button import Button
from scenes.scene import Scene
from scenes.util import *
clock = pygame.time.Clock()
    
class SceneMananger(object):
    def __init__(self):
        self.go_to(StartScene())
    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
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
class StoreScene(object):
    def __init__(self):
        super(StoreScene, self).__init__()
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