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
        

        self.level = 1.0

        self.reset_map()


    def reset_map(self):
        # Redraw character
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 10)

        # Reset Speed
        speed = 5 + (self.level * 5)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, 600, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 400, 50, 50, 'assets/enemy.png', speed),
                Enemy(0, 200, 50, 50, 'assets/enemy.png', speed),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, 600, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 400, 50, 50, 'assets/enemy.png', speed),
            ]
        else:
            self.enemies = [
                Enemy(0, 600, 50, 50, 'assets/enemy.png', speed),
            ]

    def draw_objects(self):

        # Update Display
        self.game_window.fill(self.white_color)  # Add color to the window
        # blit takes the image and a tuple with x,y variables
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        # adding each enemy in the list of enemies
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        

        pygame.display.update()  # The display update loop

    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)  # Move player

        for enemy in self.enemies:
            enemy.move(self.width)

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False    

    def detect_collision(self, object_1, object_2):
        if object_1.y < (object_2.y + object_2.height) and (object_1.y + object_1.height) > object_2.y and object_1.x < (object_2.x + object_2.width) and (object_1.x + object_1.width) > object_2.x:
            return True
        return False

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
            self.move_objects(player_direction)

            # Update Display
            self.draw_objects()

            # Detect Collisions
            if self.check_if_collided():
                self.reset_map()
            
            # how often it updates - This is set to 60 times per second.
            self.clock.tick(60)
