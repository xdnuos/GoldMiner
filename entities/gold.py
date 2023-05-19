from define import *

class Gold:
    def __init__(self,point):
        self.x = random.randint(50, screen_width - 50)
        self.y = random.randint(200, screen_height - 50)
        self.size = random.choice([30,70,90,150])
        self.rect = None
        self.is_move = False
        self.point = point
        self.is_explosive = False
    def draw(self,dt,screen):
        scaled_gold = pygame.transform.scale(gold_image, (self.size, self.size))
        self.rect = scaled_gold.get_rect(center=(self.x,self.y))
        screen.blit(scaled_gold, self.rect)
    def update(self,x,y):
        self.x = x
        self.y =y
    def __del__(self):
        pass