#import pygame to start
import pygame
# import game.py
from game import Game

# Must initialize Pygame for it to work
pygame.init()

game = Game()

game.run_game_loop() #runs the game loop

#When everything is done, make sure to call quit from pygame and then call quit itself
pygame.quit()
quit()
