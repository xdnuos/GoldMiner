from define import shopkeeper_images
class Shopkeeper:
    def __init__(self, pos_x, pos_y):
        '''
        hehe = 0 | angry = 1
        '''
        self.images = shopkeeper_images
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.current_frame = 0
        self.state = 0
        self.list_frame = [0,1]
    def draw(self, screen):
        image = self.images[self.list_frame[int(self.current_frame)]]
        screen.blit(image, (self.pos_x, self.pos_y))
    def update(self, dt):
        match self.state:
            case 1: #angry
                self.list_frame = [1]
            case _: #Strength
                self.list_frame = [0]