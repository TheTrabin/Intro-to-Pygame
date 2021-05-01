#import pygame to start
import pygame

# Must initialize Pygame for it to work
pygame.init()

#Variables
width = 800
height = 800
white_color = (255, 255, 255)
# Game Screen - Takes in a Tuple: width, height in pixels
game_window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock() #The Clock, or how often things update

background_image = pygame.image.load('assets/background.png') #loads the image
background = pygame.transform.scale(background_image, (width,height)) # scales the image. Takes the image as a variable, then a tuple as to what the height and width

#The loop - This is what makes the game go so it doesn't instantly quit out
def run_game_loop():
    while True:
        # Handle Events
        events = pygame.event.get() # Gets a list of all events within pygame
        for event in events:
            if event.type == pygame.QUIT: # if quit is active
                return #breaks out of the function and continues what's outside of the function

        # Execute Logic

        # Update Display  
        game_window.fill(white_color) # Add color to the window
        game_window.blit(background, (0,0)) # blit takes the image and a tuple with x,y variables
        pygame.display.update()  # The display update loop

        clock.tick(60) #how often it updates - This is set to 60 times per second.

run_game_loop() #runs the game loop

#When everything is done, make sure to call quit from pygame and then call quit itself
pygame.quit()
quit()
