import pygame


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

        background_image = pygame.image.load('assets/background.png')  # loads the image
        # scales the image. Takes the image as a variable, then a tuple as to what the height and width
        self.background = pygame.transform.scale(background_image, (self.width, self.height))

        treasure_image = pygame.image.load('assets/treasure.png')
        self.treasure = pygame.transform.scale(treasure_image, (50, 50))

        enemy_image = pygame.image.load('assets/enemy.png')
        self.enemy = pygame.transform.scale(enemy_image, (50, 50))

        player_image = pygame.image.load('assets/player.png')
        self.player = pygame.transform.scale(player_image, (50, 50))

    def draw_objects(self):

        # Update Display
        self.game_window.fill(self.white_color)  # Add color to the window
            # blit takes the image and a tuple with x,y variables
        self.game_window.blit(self.background, (0, 0))
        self.game_window.blit(self.treasure, (375, 50))
        self.game_window.blit(self.enemy, (375, 375))
        self.game_window.blit(self.player, (375, 750))

        pygame.display.update()  # The display update loop


    def run_game_loop(self):
        while True:
            # Handle Events
            events = pygame.event.get()  # Gets a list of all events within pygame
            for event in events:
                if event.type == pygame.QUIT:  # if quit is active
                    return  # breaks out of the function and continues what's outside of the function

            # Execute Logic
            self.draw_objects()
            
            # how often it updates - This is set to 60 times per second.
            self.clock.tick(60)
