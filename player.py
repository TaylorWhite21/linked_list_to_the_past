import pygame 
from settings import * 

class Player(pygame.sprite.Sprite): 
    def __init__(self,pos,groups, obstacle_sprites):
        super().__init__(groups)

        # Sets the player image
        self.image = pygame.image.load('./graphics/goku.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #hitbox is slightly different size than sprite
        self.hitbox = self.rect.inflate(0,-26) 

        # Sets the direction that the player can walk in
        self.direction = pygame.math.Vector2()

        # Sets the player speed
        self.speed = 5

        #sprites that will halt player movement
        self.obstacle_sprites = obstacle_sprites

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
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # Moves left or right and will stop moving if no key is pressed
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

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

    # Updates the player
    def update(self):
        self.input()
        self.move(self.speed)
