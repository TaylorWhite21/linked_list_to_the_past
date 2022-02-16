import pygame 
from settings import * 


class Tile(pygame.sprite.Sprite): 
    def __init__(self,pos,groups):
        # Super is used to give access to methods and properties
        super().__init__(groups) 
        # Assigns the rock image
        self.image = pygame.image.load('./graphics/rock.png').convert_alpha()
        
        self.rect = self.image.get_rect(topleft = pos) 

    