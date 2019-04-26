import arcade
from random import randint

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Strike"

# Constants used to scale our sprites from their original size
PACMAN_SCALING = 0.15
BEAR_SCALING = 0.3

# Constants used to config velocity of the sprites

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # These are 'lists' that keep track of our sprites. Each sprite should go into a list.
        self.model_list = None

        # Separate variable that holds the player sprite
        self.pacman_sprite = None
        self.bear_sprite = None
        
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        
        # Create the Sprite lists
        self.model_list = arcade.SpriteList()
        
        # Set up the player, specifically placing it at these coordinates.
        self.pacman_sprite = arcade.Sprite("images/Pacman Green Ghost.png", PACMAN_SCALING)
        # Random mechanic for pacman
        random_pacman = randint(1, 2)
        # Still
        if random_pacman == 1:
            self.pacman_sprite.center_x = randint(100, SCREEN_WIDTH-100)
            self.pacman_sprite.center_y = randint(100, SCREEN_HEIGHT-100)
        # Straight down
        elif random_pacman == 2:
            velocity = randint(1, 4)
            direction = randint(1, 2)
            self.pacman_sprite.center_y = randint(200, SCREEN_HEIGHT)
            if direction == 1:
                self.pacman_sprite.right = 0
                self.pacman_sprite.center_y = randint(300, SCREEN_HEIGHT-50)
                self.pacman_sprite.velocity = (velocity,-1)
            else:
                self.pacman_sprite.left = SCREEN_WIDTH
                self.pacman_sprite.center_y = randint(300, SCREEN_HEIGHT-50)
                self.pacman_sprite.velocity = (-velocity,-1)
        self.model_list.append(self.pacman_sprite)

        self.bear_sprite = arcade.Sprite("images/Crossy Road Bear.png", BEAR_SCALING)
        # Random mechanic for bear
        random_bear = randint(1, 2)
        # Still
        if random_bear == 1:
            self.bear_sprite.center_x = randint(100, SCREEN_WIDTH-100)
            self.bear_sprite.center_y = randint(100, SCREEN_HEIGHT-100)
        # Straight down
        elif random_bear == 2:
            velocity = randint(1, 4)
            direction = randint(1, 2)
            self.bear_sprite.center_y = randint(200, SCREEN_HEIGHT)
            if direction == 1:
                self.bear_sprite.right = 0
                self.bear_sprite.center_y = randint(300, SCREEN_HEIGHT-50)
                self.bear_sprite.velocity = (velocity,-1)
            else:
                self.bear_sprite.left = SCREEN_WIDTH
                self.bear_sprite.center_y = randint(300, SCREEN_HEIGHT-50)
                self.bear_sprite.velocity = (-velocity,-1)
        self.model_list.append(self.bear_sprite)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.model_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for model in self.model_list:
                left_position = model.center_x - (model.width//2)
                right_position = model.center_x + (model.width//2)
                top_position = model.center_y + (model.height//2)
                bottom_position = model.center_y - (model.height//2)
                
                if left_position <= x <= right_position and bottom_position <= y <= top_position:
                    self.model_list.remove(model)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == arcade.MOUSE_BUTTON_LEFT:
            for model in self.model_list:
                left_position = model.center_x - (model.width//2)
                right_position = model.center_x + (model.width//2)
                top_position = model.center_y + (model.height//2)
                bottom_position = model.center_y - (model.height//2)
                
                if left_position <= x <= right_position and bottom_position <= y <= top_position:
                    self.model_list.remove(model)

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.model_list.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()