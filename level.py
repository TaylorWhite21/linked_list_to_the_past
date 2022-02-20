import pygame
from settings import *
from support import * 
from tile import *
from player import Player
from random import choice
from weapon import Weapon 
from ui import UI
from enemy import Enemy


class Level: 
    def __init__(self): 

        # Get the display surface 
        # https://www.pygame.org/docs/ref/surface.html
        self.display_surface = pygame.display.get_surface()

        # Sets up the camera group
        self.visible_sprites = YSortCameraGroup()

        # Sets up the sprite groups 
        self.obstacles_sprites = pygame.sprite.Group() 

        #attack sprites 
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

         #sprite setup
            # Creates map on initialization
        self.create_map()

        # user interface
        self.ui = UI()

    # Nested loop that goes through WORLD MAP in settings.
    # Time Stamp: 19:00
    def create_map(self): 
        layout = {
            'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('./map/map_Grass.csv'),
            'object': import_csv_layout('./map/map_Objects.csv'),
            'entities':import_csv_layout('./map/map_Entities.csv')
        }
        graphics = {
            'grass': import_folder('./graphics/Grass'),
            'objects': import_folder('./graphics/objects')
        }
        
        # # Enumerates every row
        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
             # Enumerates every column
                for col_index, col in enumerate(row):
                    if col != '-1':
                 # Assigns column and row with the TILESIZE from settings
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacles_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites],'grass',random_grass_image)
                            
                        if style == 'objects':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites,self.attackable_sprites],'object',surf)

                        if style == 'entities':
                            # number 394 comes from tile creation, It can change based on graphics
                            if col == '394':
                                 self.player = Player((x,y),[self.visible_sprites],
                                               self.obstacles_sprites,
                                               self.create_attack,
                                               self.destroy_attack,
                                               self.create_magic)
                            else:
                                if col == '390' : monster_name = 'bamboo'
                                elif col == '391' : monster_name = 'spirit'
                                elif col == '392' : monster_name = 'raccoon'
                                else: monster_name = 'squid'
                                Enemy(monster_name,(x,y),[self.visible_sprites,self.attackable_sprites],self.obstacles_sprites)


                        
       

    #this functions ties together the weapons class from weapons.py and the player so that we can get the direction of the player as well as the attack direction
    def create_attack(self): 
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites]) 

    def create_magic(self, style, strength, cost):
        print(style)
        print(strength)
        print(cost)

    def destroy_attack(self): 
        if self.current_attack(): 
            self.current_attack.kill()
        self.current_attack = None 

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprite =pygame.sprite.spritecollide(attack_sprite,self.attack_sprites,True)
                if collision_sprite:
                    for target_sprite in collision_sprite:
                        target_sprite.kill()

    def run(self): 
        # draws the player sprite 
        self.visible_sprites.custom_draw(self.player)
        # update and draw the game 
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.ui.display(self.player)

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
        self.floor_surf = pygame.image.load('./graphics/tilemap/ground.png').convert()
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

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
