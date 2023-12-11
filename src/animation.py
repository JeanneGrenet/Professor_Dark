import pygame

class AnimateSprite(pygame.sprite.Sprite):
    
    def __init__(self,name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'assets/sprites/{name}.png')
        self.animation_index = 0
        self.clock=0
        self.images = {
            'down' : self.get_images(0),
            'up' : self.get_images(144),
            'left' : self.get_images(48),
            'right' : self.get_images(96)     
            }
        
        self.speed=3
    #Load one image of the player    
    def get_image(self,x,y) : 
        image = pygame.Surface([32,48])
        image.blit(self.sprite_sheet,(0,0),(x,y,64,64))
        return image
    
    #Load all the images for the animation
    def get_images(self,y):
        images=[]
        for i  in range(0,4):
            x=i*32
            image = self.get_image(x,y)
            images.append(image)
        return images
        
    #Change the side of the player and put a transparent filter behind it
    def change_animation(self,name) :
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey((255,255,255))
        self.clock += self.speed*8
        
        if self.clock >= 100 :
            self.animation_index +=1
            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.clock = 0
        

            