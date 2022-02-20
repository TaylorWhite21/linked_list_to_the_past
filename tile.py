import pygame 
from settings import * 

class Tile(pygame.sprite.Sprite): 
    def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type 
        # Assigns the rock image

        #by default, assigns it as a blank pygame surface the size of a tile
        self.image = surface 
        if sprite_type == 'object':
            self.rect= self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10) 

class Test_Tile(pygame.sprite.Sprite):
    def __init__(self, size, x,y):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = (x,y))
    
    def update(self, shift):
        self.rect.x += shift

class StaticTile(Test_Tile):
    def __init__(self, size,x,y,surface):
        super().__init__(size, x,y)
        self.image = surface



    