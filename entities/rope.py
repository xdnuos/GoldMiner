from define import *
from entities.hoo import Hoo

class Rope:
    def __init__(self, x1, y1, speed,hoo_images):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1
        self.length = 50
        self.speed = speed
        self.buff_speed = 1
        self.weight = 1
        self.speed_swinging = 50
        self.direction = 90
        self.state = 'swinging'
        self.hoo_images = hoo_images
        self.hoo_image = 0
        self.hoo = Hoo(self.hoo_images,self.x2, self.y2)
        self.item = None
        self.is_taking = False
        self.have_TNT = 5
        self.is_use_TNT = False
    def draw(self, screen):
        pygame.draw.line(screen, (51, 51, 51), (self.x1, self.y1), (self.x2, self.y2), 3)
        self.hoo.draw(screen)
    def update(self, miner, dt,screen):
        if self.state == 'swinging':
            self.direction += self.speed_swinging * dt
            if self.direction > 155 or self.direction < 25:
                self.speed_swinging = -self.speed_swinging

            self.x2 = self.x1 + self.length * math.cos(math.radians(self.direction))
            self.y2 = self.y1 + self.length * math.sin(math.radians(self.direction))

            if miner.is_moving:
                self.state = 'expanding'
        elif self.state == 'expanding':
            self.length += self.speed * dt * self.buff_speed
            self.x2 = self.x1 + self.length * math.cos(math.radians(self.direction))
            self.y2 = self.y1 + self.length * math.sin(math.radians(self.direction))

            if self.x2 <= 0 or self.x2 >= screen_width or self.y2 <= 0 or self.y2 >= screen_height:
                self.state = 'retracting'
        elif self.state == 'retracting':
            self.length -= (self.speed * dt * self.buff_speed) / self.weight
            self.x2 = self.x1 + self.length * math.cos(math.radians(self.direction))
            self.y2 = self.y1 + self.length * math.sin(math.radians(self.direction))
            if(self.item != None): #nếu đụng trúng vật phẩm
                self.weight = int(self.item.size/30)
                self.item.draw(dt,screen)
                if (self.direction < 90):
                    new_x2 = self.x2
                else:
                    new_x2 = self.x2 - int(self.item.size/5)
                self.item.update(new_x2 ,self.y2 + int(self.item.size/2.2))
                self.hoo_image = 1 #hinh anh keo vật phẩm
            else:
                self.hoo_image = 2 #hinh anh keo k co gì
            if self.length <= 50:
                del self.item
                self.item = None
                self.hoo_image = 0
                self.weight = 1
                self.state = 'swinging'
                miner.is_moving = False
                miner.current_frame = 0
        self.hoo.update(self.hoo_image,self.x2,self.y2,self.direction)