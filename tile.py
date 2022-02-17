import pygame 
from settings import * 


class Tile(pygame.sprite.Sprite): 
    def __init__(self,pos,groups, sprite_type, surface = pygame.surface((TILESIZE,TILESIZE))):
        # Super is used to give access to methods and properties
        super().__init__(groups)
        self.sprite_type = sprite_type 
        # Assigns the rock image

        #by default, assigns it as a blank pygame surface the size of a tile
        self.image = surface        
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10) 

    