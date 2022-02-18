import pygame 
from settings import *
from support import import_folder 

class Player(pygame.sprite.Sprite): 
    def __init__(self,pos,groups, obstacle_sprites):
        super().__init__(groups)

        # Sets the player image
        self.image = pygame.image.load('./graphics/goku.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #hitbox is slightly different size than sprite
        self.hitbox = self.rect.inflate(0,-26) 

        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # Sets the direction that the player can walk in
        self.direction = pygame.math.Vector2()

        # Attack variables
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_timer = None

        # Sets the player speed
        self.speed = 5

        #sprites that will halt player movement
        self.obstacle_sprites = obstacle_sprites

        # graphics setup
        self.import_player_assets()

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
            print(self.animations)


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
        if keys[pygame.K_SPACE] and not self.attacking:
            print('attack')
            self.attacking = True
            # Grabs time that attack was done
            self.attack_time = pygame.time.get_ticks()
        # magic input
        if keys[pygame.K_LCTRL] and not self.attacking:
            print('magic')
            self.attacking = True
            # Grabs time that attack was done
            self.attack_time = pygame.time.get_ticks()


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
