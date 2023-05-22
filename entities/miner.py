class Miner:
    def __init__(self, images, pos_x, pos_y, speed):
        self.images = images
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.current_frame = 0
        self.start = 0
        self.end = 3 #len(self.images)
        self.is_moving = False
        self.yeah = False
        self.is_TNT = False
        # self.list_frame = {0,1,2} #need fix: remove start and end, change to number of frame
    def draw(self, screen):
        image = self.images[int(self.current_frame)]
        screen.blit(image, (self.pos_x, self.pos_y))
    def update(self, dt):
        if self.is_moving or self.is_TNT or self.yeah:
            # print(self.start,self.end,self.current_frame)
            self.current_frame += self.speed * dt
            if self.current_frame >= self.end :
                self.current_frame = self.start