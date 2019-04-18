import arcade
from random import randint

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Strike"

# Constants used to scale our sprites from their original size
PACMAN_SCALING = 0.2
STARFOX_SCALING = 0.3


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
        self.starfox_sprite = None

        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.model_list = arcade.SpriteList()
        
        # Set up the player, specifically placing it at these coordinates.
        self.pacman_sprite = arcade.Sprite("images/Pacman Green Ghost.png", PACMAN_SCALING)
        self.pacman_sprite.center_x = randint(100, SCREEN_WIDTH-100)
        self.pacman_sprite.center_y = randint(100, SCREEN_HEIGHT-100)
        self.model_list.append(self.pacman_sprite)

        self.starfox_sprite = arcade.Sprite("images/Kaimook_cut.png", STARFOX_SCALING)
        self.starfox_sprite.right = SCREEN_WIDTH
        self.starfox_sprite.center_y = randint(100, SCREEN_HEIGHT-100)
        self.model_list.append(self.starfox_sprite)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.model_list.draw()

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

        STARFOX_VELOCITY = 4
        self.starfox_sprite.center_x -= STARFOX_VELOCITY


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()