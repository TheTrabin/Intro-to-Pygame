#import pygame to start
import pygame

# Must initialize Pygame for it to work
pygame.init()

#Variables
width = 800
height = 800
white_color = (255, 255, 255)

#The Game Window itself

# Game Screen - Takes in a Tuple: width, height in pixels
game_window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock() #The Clock, or how often things update

#The loop - This is what makes the game go so it doesn't instantly quit out
while True:
    # Handle Events

    # Execute Logic

    # Update Display  
    game_window.fill(white_color) # Add color to the window
    pygame.display.update()  # The display update loop

    clock.tick(60) #how often it updates - This is set to 60 times per second.

#When everything is done, make sure to call quit from pygame and then call quit itself
pygame.quit()
quit()
