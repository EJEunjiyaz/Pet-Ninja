import arcade
from random import randint

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
        self.mouse_sprite = None

        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.pacman_list = arcade.SpriteList()
        
        # Set up the player, specifically placing it at these coordinates.
        self.pacman_sprite = arcade.Sprite("images/Pacman Green Ghost.png", PACMAN_SCALING)
        self.pacman_sprite.center_x = randint(100, 900)
        self.pacman_sprite.center_y = randint(100, 550)
        self.pacman_list.append(self.pacman_sprite)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.pacman_list.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for pacman in self.pacman_list:
                left_position = pacman.center_x - (self.pacman_sprite.width//2)
                right_position = pacman.center_x + (self.pacman_sprite.width//2)
                top_position = pacman.center_y + (self.pacman_sprite.height//2)
                bottom_position = pacman.center_y - (self.pacman_sprite.height//2)
                
                if left_position <= x <= right_position and bottom_position <= y <= top_position:
                    self.pacman_list.remove(pacman)

    #     arcade.check_for_collision(self.pacman_sprite, )

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.pacman_list.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()