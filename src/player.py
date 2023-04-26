import pygame

class Player(pygame.sprite.Sprite) :
    
    def __init__(self,x,y) :
        super().__init__()
        #Load the different positions of the player 
        self.sprite_sheet = pygame.image.load('assets/spritesheets/player.png')
        self.image = self.get_image(0,128)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.images = {
            'down' : self.get_image(0,128),
            'up' : self.get_image(0,0),
            'left' : self.get_image(64,64),
            'right' : self.get_image(64,192)     
            }
        self.feet = pygame.Rect(0,0,self.rect.width*0.5,12)
        self.old_position = self.position.copy()
    
    #Load the image of the player    
    def get_image(self,x,y) : 
        image = pygame.Surface([64,64])
        image.blit(self.sprite_sheet,(0,0),(x,y,64,64))
        return image
    
    #Save the location of the player before his move
    def save_location(self) : self.old_position = self.position.copy()
    
    #Change the side of the player and put a transparent filter behind it
    def change_animation(self,name) :
        self.image = self.images[name]
        self.image.set_colorkey((0,0,0))
    
    #Change the position of the player
    def move_right(self) : self.position[0] += 3 
    
    def move_left(self) : self.position[0] -= 3
    
    def move_up(self) : self.position[1] -= 3
    
    def move_down(self) : self.position[1] += 3 
    
    #Update the position of the player
    def update(self) :
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom 
    
    #Put the player on his previous position
    def move_back(self) : 
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
            