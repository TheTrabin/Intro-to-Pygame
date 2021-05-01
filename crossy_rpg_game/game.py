import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

# Create a game class to handle the loop
class Game:
    def __init__(self):

        #The loop - This is what makes the game go so it doesn't instantly quit out
        #Variables
        self.width = 800
        self.height = 800
        self.white_color = (255, 255, 255)
        # Game Screen - Takes in a Tuple: width, height in pixels
        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()  # The Clock, or how often things update
        
        #Game Objects
        self.background = GameObject(0,0, self.width, self.height, 'assets/background.png')
        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 10)       
        self.enemy = Enemy(50, 600, 50, 50, 'assets/enemy.png', 10)
        
        

    def draw_objects(self):

        # Update Display
        self.game_window.fill(self.white_color)  # Add color to the window
        # blit takes the image and a tuple with x,y variables
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.enemy.image, (self.enemy.x, self.enemy.y))
        

        pygame.display.update()  # The display update loop

    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False

        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False

        return True

    def run_game_loop(self):

        player_direction = 0

        while True:
            # Handle Events
            events = pygame.event.get()  # Gets a list of all events within pygame
            for event in events:
                if event.type == pygame.QUIT:  # if quit is active
                    return  # breaks out of the function and continues what's outside of the function
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1 # move player up
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1 # move player down
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0 # Stop movement

            # Execute Logic
            self.player.move(player_direction, self.height) # Move player
            self.enemy.move(self.width)
            # Update Display
            self.draw_objects()

            # Detect Collisions
            if self.detect_collision(self.player, self.enemy):
                return
            elif self.detect_collision(self.player, self.treasure):
                return
            
            # how often it updates - This is set to 60 times per second.
            self.clock.tick(60)
