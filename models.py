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


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hole = Hole