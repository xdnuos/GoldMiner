from define import *
class Explosive:
    def __init__(self, pos_x, pos_y, speed):
        self.images = explosive_images
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.current_frame = 0
        self.is_exit = False
    def draw(self, screen):
        image = self.images[int(self.current_frame)]
        screen.blit(image, (self.pos_x, self.pos_y))
    def update(self, dt):
        if self.is_exit ==  False:
            # print(self.current_frame)
            self.current_frame += self.speed * dt
            if self.current_frame >= len(self.images):
                self.images = empty_images
                self.current_frame = 0
                self.is_exit = True