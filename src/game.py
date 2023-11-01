import pygame, pytmx, pyscroll
from player import *
from map import *
from dialog import DialogBox

class Game :
    def __init__(self) :
        #Creation of the window
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("Professor Dark")
        
        
        #Creation of the player in the game
        self.player = Player()
        self.map_manager = MapManager(self.screen,self.player)
        self.dialog_box = DialogBox()

    
    
    #Make the player move and turn when a key is pressed on the keyboard
    def handle_input(self) :
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] :
            self.player.move_up()
        elif pressed[pygame.K_DOWN] :
            self.player.move_down()
        elif pressed[pygame.K_LEFT] :
            self.player.move_left()
        elif pressed[pygame.K_RIGHT] :
            self.player.move_right()
  
    
    
    #Update the player position      
    def update(self) : 
        self.map_manager.update()

                
    #Event in the game when it runs                   
    def run(self) :
        clock = pygame.time.Clock()
        #Boucle du jeu
        running = True
        while running :
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    running = False
                elif event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)
            clock.tick(60)
        pygame.quit()
        
