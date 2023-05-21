class Miner:
    def __init__(self, images, pos_x, pos_y, speed):
        self.images = images
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.current_frame = 0
        self.list_frame = {0,1,2}
        self.is_moving = False
        self.time = 0
    def draw(self, screen):
        image = self.images[int(self.current_frame)]
        screen.blit(image, (self.pos_x, self.pos_y))

    def update(self, dt):
        if self.is_moving==True:
            self.current_frame += self.speed * dt
            if self.current_frame >= self.end :
                self.current_frame = self.start
            if self.time > 0:
                self.time -= self.speed * dt
            else:
                self.start = 0
                self.end = 3