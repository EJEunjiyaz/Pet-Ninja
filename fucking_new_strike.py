import arcade
from random import randint, randrange, random

# Constants
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 850
SCREEN_TITLE = "Pet Ninja"

# Constants used to scale our sprites from their original size
BOMB_SCALING = 0.27
BEAR_SCALING = 0.5
BROWNDOG_SCALING = 0.2
BUNNY_SCALING = 0.3
CAT_SCALING = 0.3
CHICKEN_SCALING = 0.2
COW_SCALING = 0.4
DOG_SCALING = 0.26
DUCK_SCALING = 0.2
ELEPHANT_SCALING = 0.36
LION_SCALING = 0.5
PIG_SCALING = 0.5
RABBIT_SCALING = 0.2
REINDEER_SCALING = 0.5
SHEEP_SCALING = 0.3
SQUIRREL_SCALING = 0.26
UNICORN_SCALING = 0.3

HEART_SCALING = 0.1

# Constants for game config
SPAWN_SECONDS = 0.4
VELOCITY_MIN = 4
VELOCITY_MAX = 7
VELOCITY_Y = 3
PERCENTAGE_BOMB = 0.35
PREPARE_TIME = 4

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # These are 'lists' that keep track of our sprites. Each sprite should go into a list.
        self.model_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.heart_list = arcade.SpriteList()
        # Separate variable that holds the player sprite
        self.bomb_sprite = None
        self.bear_sprite = None
        self.browndog_sprite = None
        self.bunny_sprite = None
        self.cat_sprite = None
        self.chicken_sprite = None
        self.dog_sprite = None
        self.duck_sprite = None
        self.elephant_sprite = None
        self.lion_sprite = None

        self.heart1 = None
        self.heart2 = None
        self.heart3 = None
        self.heart4 = None
        self.heart5 = None
        # Count time for spawn model sprite
        self.time = 0
        # Count time before play the game
        self.prepare_count = 0
        # Keep the score
        self.score = 0
        self.state = 'stop'

        self.background_1 = None
        self.background_2 = None
        
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)
        self.background = arcade.Sprite("images/minecraft.png", center_x=SCREEN_WIDTH/2, center_y=SCREEN_HEIGHT/2, scale=1.7)
        self.main_screen = arcade.Sprite("images/main_screen.png")

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        self.bomb_sprite = arcade.Sprite("images/Cherry Bomb the Baby Boomer.png", BOMB_SCALING)
        self.bear_sprite = arcade.Sprite("images/Crossy Road Bear.png", BEAR_SCALING)
        self.browndog_sprite = arcade.Sprite("images/Crossy Road Brown Dog.png", BROWNDOG_SCALING)
        self.bunny_sprite = arcade.Sprite("images/Crossy Road Bunny.png", BUNNY_SCALING)
        self.cat_sprite = arcade.Sprite("images/Crossy Road Cat.png", CAT_SCALING)
        self.chicken_sprite = arcade.Sprite("images/Crossy Road Chicken.png", CHICKEN_SCALING)
        self.dog_sprite = arcade.Sprite("images/Crossy Road Dog.png", DOG_SCALING)
        self.duck_sprite = arcade.Sprite("images/Crossy Road Duck.png", DUCK_SCALING)
        self.elephant_sprite = arcade.Sprite("images/Crossy Road Elephant.png", ELEPHANT_SCALING)
        self.lion_sprite = arcade.Sprite("images/Crossy Road Lion Heart.png", LION_SCALING)
        self.pig_sprite = arcade.Sprite("images/Crossy Road Pig.png", PIG_SCALING)
        self.rabbit_sprite = arcade.Sprite("images/Crossy Road Rabbit.png", RABBIT_SCALING)
        self.reindeer_sprite = arcade.Sprite("images/Crossy Road Reindeer.png", REINDEER_SCALING)
        self.sheep_sprite = arcade.Sprite("images/Crossy Road Sheep.png", SHEEP_SCALING)
        self.squirrel_sprite = arcade.Sprite("images/Crossy Road Squirrel.png", SQUIRREL_SCALING)
        self.unicorn_sprite = arcade.Sprite("images/Crossy Road Unicorn.png", UNICORN_SCALING)
        
        list = [self.bear_sprite, self.browndog_sprite, self.bunny_sprite, self.cat_sprite, self.chicken_sprite,
                self.dog_sprite, self.duck_sprite, self.elephant_sprite, self.lion_sprite, self.pig_sprite,
                self.rabbit_sprite, self.reindeer_sprite, self.sheep_sprite, self.squirrel_sprite, self.unicorn_sprite]
        
        # Straight down
        # if random_number == 1:
        if self.state == 'active':
            velocity = randint(VELOCITY_MIN, VELOCITY_MAX)
            direction = randint(0, 1)
            y = randint(-VELOCITY_Y, VELOCITY_Y)
            percentage = random()
            if percentage > PERCENTAGE_BOMB: 
                random_sprite = randrange(0, len(list))
                sprite = list[random_sprite]
            else:
                sprite = self.bomb_sprite
            if direction == 0:
                sprite.right = 0
                if y < 0:
                    sprite.center_y = randint(SCREEN_HEIGHT/2, SCREEN_HEIGHT-50)
                elif y > 0:
                    sprite.center_y = randint(50, SCREEN_HEIGHT/2)
                else:
                    sprite.center_y = randint(100, SCREEN_HEIGHT-100)
                sprite.velocity = (velocity, y)
            else:
                sprite.left = SCREEN_WIDTH
                if y < 0:
                    sprite.center_y = randint(SCREEN_HEIGHT/2, SCREEN_HEIGHT-50)
                elif y > 0:
                    sprite.center_y = randint(50, SCREEN_HEIGHT/2)
                else:
                    sprite.center_y = randint(100, SCREEN_HEIGHT-100)
                sprite.velocity = (-velocity, y)
        
            if sprite != self.bomb_sprite:
                self.model_list.append(sprite)
            else:
                self.bomb_list.append(sprite)
     
    def setup_heart(self):
        self.heart1 = arcade.Sprite("images/heart.png", HEART_SCALING)
        self.heart2 = arcade.Sprite("images/heart.png", HEART_SCALING)
        self.heart3 = arcade.Sprite("images/heart.png", HEART_SCALING)
        self.heart4 = arcade.Sprite("images/heart.png", HEART_SCALING)
        self.heart5 = arcade.Sprite("images/heart.png", HEART_SCALING)

        list_heart = [self.heart1, self.heart2, self.heart3, self.heart4, self.heart5]

        for i in range(len(list_heart)):
            list_heart[i].center_x = SCREEN_WIDTH - (45*i) - 100
            list_heart[i].center_y = SCREEN_HEIGHT - 85
            self.heart_list.append(list_heart[i])
        # print(">>>", len(self.heart_list))

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()
        
        # Draw our sprites
        if self.state == 'stop':
            self.main_screen.left = 0
            self.main_screen.bottom = 0
            self.main_screen.draw()
            arcade.draw_text("PLAY", 650, 350, arcade.color.BLACK, 60)
            arcade.draw_text("HOW TO PLAY", 500, 235, arcade.color.BLACK, 60)
            arcade.draw_text("EXIT", 660, 120, arcade.color.BLACK, 60)
        elif self.state == 'prepare':
            self.background.draw()
            # if self.prepare_time < 1:
            #     arcade.draw_text('3', SCREEN_WIDTH/2, SCREEN_HEIGHT/2,)
            seconds = PREPARE_TIME - (self.prepare_count//1) - 1
            seconds = int(seconds)
            if seconds >= 1:
                arcade.draw_text(f"{seconds}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.RED_DEVIL, 120)
            else:
                arcade.draw_text("START", 600, SCREEN_HEIGHT/2, arcade.color.RED_DEVIL, 120)
        elif self.state == 'active':
            self.background.draw()
            self.model_list.draw()
            self.bomb_list.draw()
            self.heart_list.draw()
            # Draw text
            arcade.draw_text(f'SCORE {self.score}', SCREEN_WIDTH-250, SCREEN_HEIGHT-50, arcade.color.WHITE, 25, font_name='Gill Sans')
        
        elif self.state == 'dead':
            arcade.draw_text('GAME OVER', 300, SCREEN_HEIGHT/2, arcade.color.RED_ORANGE, 60, font_name='Showcard Gothic')

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.state == 'stop':
                self.state = 'prepare'
                for model in self.model_list:
                    left_position = model.center_x - (model.width//2)
                    right_position = model.center_x + (model.width//2)
                    top_position = model.center_y + (model.height//2)
                    bottom_position = model.center_y - (model.height//2)
                    
                    if left_position <= x <= right_position and bottom_position <= y <= top_position:
                        self.score += 1
                        self.model_list.remove(model)
            
                for bomb in self.bomb_list:
                    left_position = bomb.center_x - (bomb.width//2)
                    right_position = bomb.center_x + (bomb.width//2)
                    top_position = bomb.center_y + (bomb.height//2)
                    bottom_position = bomb.center_y - (bomb.height//2)
                    
                    if left_position <= x <= right_position and bottom_position <= y <= top_position:
                        if len(self.heart_list) > 0:
                            self.heart_list.pop()
                        else:
                            self.state = 'dead'
                        self.bomb_list.remove(bomb)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == arcade.MOUSE_BUTTON_LEFT:
            for model in self.model_list:
                left_position = model.center_x - (model.width//2)
                right_position = model.center_x + (model.width//2)
                top_position = model.center_y + (model.height//2)
                bottom_position = model.center_y - (model.height//2)
                    
                if left_position <= x <= right_position and bottom_position <= y <= top_position:
                    self.score += 1
                    self.model_list.remove(model)
            
            for bomb in self.bomb_list:
                left_position = bomb.center_x - (bomb.width//2)
                right_position = bomb.center_x + (bomb.width//2)
                top_position = bomb.center_y + (bomb.height//2)
                bottom_position = bomb.center_y - (bomb.height//2)
                
                if left_position <= x <= right_position and bottom_position <= y <= top_position:
                    # print(len(self.heart_list))
                    if len(self.heart_list) > 0:
                        self.heart_list.pop()
                    else:
                        self.state = 'dead'
                    # print(len(self.heart_list))
                    self.bomb_list.remove(bomb)

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.model_list.update()
        self.bomb_list.update()
        self.heart_list.update()

        if self.state == 'prepare':
            if self.prepare_count < PREPARE_TIME:
                self.prepare_count += delta_time
            else:
                self.prepare_count = 0
                self.state = 'active'

        if self.time <= SPAWN_SECONDS:
            self.time += delta_time
        else:
            self.setup()
            self.time = 0
        
        for model in self.model_list:
            if model.right < 0 or model.left > SCREEN_WIDTH or model.top < 0 or model.bottom > SCREEN_HEIGHT:
                if len(self.heart_list) > 0:
                    self.heart_list.pop()
                    self.model_list.remove(model)
                else:
                    self.state = 'dead'             
        
        for bomb in self.bomb_list:
            if bomb.right < 0 or bomb.left > SCREEN_WIDTH or bomb.top < 0 or bomb.bottom > SCREEN_HEIGHT:
                self.bomb_list.remove(bomb)


def main():
    """ Main method """
    window = MyGame()
    window.setup_heart()
    # window.setup()
    arcade.run()


if __name__ == "__main__":
    main()