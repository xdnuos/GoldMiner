from define import *
class QuestionBag:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 30
        self.rect = None
        self.is_move = True
        self.image = questionBag
        self.point = 0
        self.is_explosive = False
    def draw(self,dt,screen):
        # global mole_image
        self.rect = self.image.get_rect(center=(self.x,self.y))
        screen.blit(self.image, self.rect)
        #Random
        random_number = random.randint(1, 100)
        if random_number <10:
            self.point = -1 #dynamite
        elif random_number < 50:
            self.point = -2 #Strength
        else:
            self.point = random.randint(1, 500)
    def update(self,x,y):
        self.x = x
        self.y =y
    def __del__(self):
        pass