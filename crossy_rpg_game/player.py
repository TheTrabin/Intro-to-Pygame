from gameObject import GameObject

class Player(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed

    #movement, just up and down for now
    def move(self, direction):
        self.y += (direction * self.speed)