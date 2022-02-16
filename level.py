import pygame
from settings import * 
from tile import Tile
from player import Player


class Level: 
    def __init__(self): 

        # Get the display surface 
        # https://www.pygame.org/docs/ref/surface.html
        self.display_surface = pygame.display.get_surface()

        # Sets up the sprite groups 
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group() 

         #sprite setup
         # Creates map on initialization
        self.create_map()

    # Nested loop that goes through WORLD MAP in settings.
    # Time Stamp: 19:00
    def create_map(self): 
        # Enumerates every row
        for row_index,row in enumerate(WORLD_MAP):
            # Enumerates every column
            for col_index, col in enumerate(row): 
                # Assigns column and row with the TILESIZE from settings
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                # If the element in the WORLDMAP is an 'x', instantiate a Tile and place it there
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
                # If the element in the WORLDMAP is an 'p', instantiate a player and place it there
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacles_sprites)

    def run(self): 
        # update and draw the game 
        self.visible_sprites.draw(self.display_surface) 
        self.visible_sprites.update()
