import pygame 
import pytmx
import pyscroll
from player import *

class Game :
    def __init__(self) :
        #Creation of the window
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("Professor Dark")
        
        #Load and draw the map
        tmx_data = pytmx.util_pygame.load_pygame('assets/Map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        
        #Creation of the player in the game
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y)
        
        #Creation of the collision list
        self.walls = []
        for obj in tmx_data.objects : 
            if obj.name == "collision" :
                self.walls.append(pygame.Rect(obj.x,obj.y,obj.width,obj.height))
        
    
        #Manage the layer group
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer = 99)
        self.group.add(self.player)
    
    #Make the player move and turn when a key is pressed on the keyboard
    def handle_input(self) :
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] :
            self.player.move_up()
            self.player.change_animation('up')  
        elif pressed[pygame.K_DOWN] :
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT] :
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT] :
            self.player.move_right()
            self.player.change_animation('right')
     
     #Update the player position when he entered into a wall       
    def update(self) : 
        self.group.update()
        for sprite in self.group.sprites() : 
            if sprite.feet.collidelist(self.walls) > -1 :
                sprite.move_back()
                
    #Event in the game when it runs                   
    def run(self) :
        clock = pygame.time.Clock()
        #Boucle du jeu
        running = True
        while running :
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect) 
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    running = False
            clock.tick(60)
        pygame.quit()
        
