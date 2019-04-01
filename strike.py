import arcade
from models import *
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()


class HoleDrawer():
    def __init__(self):
        self.hole1 = Hole(self, 200, 100)
        self.hole2 = Hole(self, 450, 100)
        self.hole3 = Hole(self, 700, 100)
        self.hole4 = Hole(self, 325, 350)
        self.hole5 = Hole(self, 575, 350)
        self.hole6 = Hole(self, 200, 600)
        self.hole7 = Hole(self, 450, 600)
        self.hole8 = Hole(self, 700, 600)
    
    def draw(self):
        self.hole1.draw()
        self.hole2.draw()
        self.hole3.draw()
        self.hole4.draw()
        self.hole5.draw()
        self.hole6.draw()
        self.hole7.draw()
        self.hole8.draw()


class StrikeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.PINK_PEARL)
        self.background = arcade.load_texture("images/background.png")
        self.hole = HoleDrawer()
 
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.hole.draw()


def main():
    window = StrikeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()