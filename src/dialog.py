import pygame

class DialogBox:
    
    X_POSITION = 550
    Y_POSITION = 560

     
    def __init__(self,player):
        self.box = pygame.image.load("assets/dialog/dialog_box.png")
        self.box.set_colorkey([255,255,255])
        self.box = pygame.transform.scale(self.box,(525,150))
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("assets/dialog/dialog_font.ttf",28)
        self.reading = False
        self.dialog_name = ""
        self.player=player
        
    def render(self,screen):
        if self.reading : 
            self.letter_index +=1
            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index
                
            screen.blit(self.box,(self.X_POSITION,self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index],False,(0,0,0))
            screen.blit(text,(self.X_POSITION+60,self.Y_POSITION+60))
            name = self.font.render(self.dialog_name,False,(255,255,255))
            screen.blit(name,(self.X_POSITION+120,self.Y_POSITION+8))

        
    def next_text(self):
        self.text_index +=1
        self.letter_index = 0
        if self.text_index >= len(self.texts):
            self.reading = False 
            self.player.level_up() 

    def execute(self,dialog,name):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog
            self.dialog_name = f"{name}"

            
            
class LevelBox :

    X_POSITION = 10
    Y_POSITION = 10

    def __init__(self,player):
        self.box = pygame.image.load("assets/levelBox.png")
        self.box.set_colorkey([255,255,255])
        self.box = pygame.transform.scale(self.box,(150,50))
        self.font = pygame.font.Font("assets/dialog/dialog_font.ttf",32)
        self.player = player
        self.level = 0
        self.text = ""

    def render(self,screen):
            self.level = self.player.level
            self.text = f"Level {self.level}"
            screen.blit(self.box,(self.X_POSITION,self.Y_POSITION))
            text = self.font.render(self.text,False,(255,255,255))
            screen.blit(text,(self.X_POSITION+20,self.Y_POSITION+5))


