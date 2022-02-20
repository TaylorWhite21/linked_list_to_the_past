import pygame,sys
from settings import *
from support import import_folder 

class Player(pygame.sprite.Sprite): 

    def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack,create_ki):
        super().__init__(groups)

        # Sets the player image
        self.image = pygame.image.load('./graphics/goku.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #hitbox is slightly different size than sprite
        self.hitbox = self.rect.inflate(0,-26) 

        # graphics setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        #MOVEMENT
            # Sets the direction that the player can walk in
        self.direction = pygame.math.Vector2()

            # attack variables
        self.attacking = False
        #400************************
        self.attack_cooldown = 200
        self.attack_timer = None

            #sprites that will halt player movement
        self.obstacle_sprites = obstacle_sprites
        
        # WEAPONS
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
            #tells us which weapon is selected from our weapon data which is a list
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        # print(f"This is weapon: {self.weapon}") 
            #make the weapon timer
        self.can_switch_weapon = True 
        self.weapon_switch_time = None 
        self.switch_duration_cooldown = 200      
   
        # ki
        self.create_ki = create_ki
        self.ki_index = 0
        self.ki = list(ki_data.keys())[self.ki_index]
        self.can_switch_ki = True
        self.ki_switch_time = None
        
        # Stats
        
        self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'ki': 4, 'speed': 6}
        # Sets the player health
        self.health = self.stats['health']
        # Sets the player energy
        self.energy = self.stats['energy']
        # Sets the player speed
        self.speed = self.stats['speed']
        # full_heart = pygame.image.load('.\graphics\heart.png') 


    # imports player resources
    def import_player_assets(self):
        # sets the file path before importing
        character_path = './graphics/player/'
        # Dictionary of player states
        self.animations = {'up': [], 'down': [], 'left':[], 'right':[], 'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [], 'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}
        # Goes through dictionary assigns the path and fills the key with the animation
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
            #this is printing that surface stuff:
            # print(self.animations)

    # Collision Detection for obstacles
    # Time stamp on tutorial: 42:00
    def collision(self, direction):
        
        # If the player is moving left or right, checks for collisions, then stops player on that side of the obstacle
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: 
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        # If the player is moving up or down, checks for collisions, then stops player on that side of the obstacle
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: 
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    # Gets keyboard input and moves in desired direction
    # http://www.pygame.org/docs/ref/key.html
    def input(self):

        # if not self.attacking: 
        
        keys = pygame.key.get_pressed()

        # Moves up or down and will stop moving if nothing is pressed
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        # Moves left or right and will stop moving if no key is pressed
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

        # attack input
        if keys[pygame.K_SPACE]:
            self.attacking = True
            # Grabs time that attack was done
            self.attack_time = pygame.time.get_ticks()  
            self.create_attack()
            print('attack')

        # ki input
        if keys[pygame.K_LCTRL]:
            self.attacking = True
            # Grabs time that attack was done
            self.attack_time = pygame.time.get_ticks()
            style = list(ki_data.keys())[self.ki_index]
            strength = list(ki_data.values())[self.ki_index]['strength']
            cost = list(ki_data.values())[self.ki_index]['cost']

            self.create_ki(style, strength, cost)
            
        #weapons cycle
        if keys[pygame.K_q] and self.can_switch_weapon:
            self.can_switch_weapon = False 
            self.weapon_switch_time = pygame.time.get_ticks()
            #starts the weapons wheel from the 0 index and moves through weapons list (unidirectional)
            if self.weapon_index < len(list(weapon_data.keys())) - 1:
                self.weapon_index += 1
            else:
                #reset the list once at the end
                self.weapon_index = 0
            self.weapon = list(weapon_data.keys())[self.weapon_index]


        # ki cycling
        if keys[pygame.K_e] and self.can_switch_ki:
            self.can_switch_ki = False 
            self.ki_switch_time = pygame.time.get_ticks()
            #starts the weapons wheel from the 0 index and moves through weapons list (unidirectional)
            if self.ki_index < len(list(ki_data.keys())) - 1:
                self.ki_index += 1
            else:
                #reset the list once at the end
                self.ki_index = 0
            self.ki = list(ki_data.keys())[self.ki_index]
            

    def get_status(self):
        # Runs if we are not moving
        if self.direction.x == 0 and self.direction.y ==0:
            # Checks if status already contains idle
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            # keeps player from moving while attacking
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                # If idle is in status, replace it with attack
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                # add attack to status
                else:
                    self.status = self.status + '_attack'
        # Removes attack string from status if player goes idle 
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')


    # Move method that tells the player how to move
    def move(self, speed):
        # Normalizes the diagonal movement of the player so that they aren't zooming around when going diagonal
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Rect stores and manipulates rectangular areas
        # https://www.pygame.org/docs/ref/rect.html
        self.hitbox.x += self.direction.x * speed
        # Collision detection if the player is moving horizontally
        self.collision('horizontal')

        self.hitbox.y += self.direction.y * speed
        # Collision detection if the player is moving vertically
        self.collision('vertical')

        #recenter rect on hitbox
        self.rect.center = self.hitbox.center

    # Sets player cooldown in between attacks
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            # Checks if enough time has passed since attacking
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

                print(f'destroy:{self.destroy_attack}')

        if not self.can_switch_weapon: 
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_ki: 
            if current_time - self.ki_switch_time >= self.switch_duration_cooldown:
                self.can_switch_ki = True

        if not self.can_switch_weapon: 
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True
    def animate(self):
        # Gets animation from dictionary based off player status
        animation = self.animations[self.status]
        
        # Loops through frame index to animate player walking
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    
    # Updates the player
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
