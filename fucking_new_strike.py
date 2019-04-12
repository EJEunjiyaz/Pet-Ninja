import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Strike"

# Constants used to scale our sprites from their original size
PACMAN_SCALING = 0.2


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should go into a list.
        self.pacman_list = None

        # Separate variable that holds the player sprite
        self.pacman_sprite = None

        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.pacman_list = arcade.SpriteList()
        
        # Set up the player, specifically placing it at these coordinates.
        self.pacman_sprite = arcade.Sprite("images/Pacman Green Ghost.png", PACMAN_SCALING)
        self.pacman_sprite.center_x = 300
        self.pacman_sprite.center_y = 300
        self.pacman_list.append(self.pacman_sprite)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.pacman_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()