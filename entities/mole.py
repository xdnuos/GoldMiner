from define import *
class Mole:
    def __init__(self,x,y,image,point):
        self.x = x
        self.y = y
        self.size = 30
        self.rect = None
        self.is_move = True
        self.direction = -1 # -1 : Left | 1 : Right
        self.range = [self.x,self.x +400]
        self.image = image
        self.point = point
        self.is_explosive = False
    def draw(self,dt,screen):
        # global mole_image
        self.rect = self.image.get_rect(center=(self.x,self.y))
        if ((self.x < self.range[0] or self.x > self.range[1]) and self.is_move == True):
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = -self.direction
        screen.blit(self.image, self.rect)
        if self.is_move == True:
            self.x += 100*dt * self.direction

    def update(self,x,y):
        self.x = x
        self.y =y
    def __del__(self):
        pass