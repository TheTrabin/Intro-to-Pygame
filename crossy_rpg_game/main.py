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
game_window = pygame.display.set_mode((width,height))

# Add color to the window
game_window.fill(white_color)
#The display update loop
pygame.display.update()


#When everything is done, make sure to call quit from pygame and then call quit itself
pygame.quit()
quit()