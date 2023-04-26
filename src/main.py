import pygame
from game import *

#Make the game run

if __name__ == '__main__' :
    pygame.init()
    game = Game()
    game.run()