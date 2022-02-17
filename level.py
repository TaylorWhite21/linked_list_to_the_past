import pygame
from settings import * 
from tile import *
from player import Player


class Level: 
    def __init__(self): 

        # Get the display surface 
        # https://www.pygame.org/docs/ref/surface.html
        self.display_surface = pygame.display.get_surface()

        # Sets up the camera group
        self.visible_sprites = YSortCameraGroup()

        # Sets up the sprite groups 
        self.obstacles_sprites = pygame.sprite.Group() 

         #sprite setup
         # Creates map on initialization
        self.create_map()

    # Nested loop that goes through WORLD MAP in settings.
    # Time Stamp: 19:00
    def create_map(self): 
        # # Enumerates every row
        # for row_index,row in enumerate(WORLD_MAP):
        #     # Enumerates every column
        #     for col_index, col in enumerate(row): 
        #         # Assigns column and row with the TILESIZE from settings
        #         x = col_index * TILESIZE
        #         y = row_index * TILESIZE
        #         # If the element in the WORLDMAP is an 'x', instantiate a Tile and place it there
        #         if col == 'x':
        #             Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
        #         # If the element in the WORLDMAP is an 'p', instantiate a player and place it there
        #         if col == 'p':
        #             self.player = Player((x,y),[self.visible_sprites], self.obstacles_sprites)
        self.player = Player((2000,1430),[self.visible_sprites], self.obstacles_sprites)

    def run(self): 
        # draws the player sprite 
        self.visible_sprites.custom_draw(self.player)
        # update and draw the game 
        self.visible_sprites.update()

#camera class, extends sprite group to allow z axis functionlity
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #class extends sprite groups        
        super().__init__()

        #gets a reference to the display
        self.display_surface = pygame.display.get_surface()

        #finding hlaf the height/width of the screen
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2

        #define an offset
        self.offset = pygame.math.Vector2()

        #creating the floor
        self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        #get the offset, this will render all sprites around the player to simulate a camera
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        #updates each sprite with the offset position from the player
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)