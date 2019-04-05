import arcade

class Hole:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.width = 70
        self.height = 50

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, 
                                self.width, self.height, 
                                arcade.color.ORANGE_PEEL)


class Rat:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y+30
        self.status = 1
    
    def change_status(self):
        if self.status == 1:
            self.status = 0
        else:
            self.status = 1


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hole = Hole
        self.rat = Rat(self, 200, 100)