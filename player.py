import pygame 
from settings import * 

class Player(pygame.sprite.Sprite): 
    def __init__(self,pos,groups, obstacle_sprites):
        super().__init__(groups) 
        # Sets the player image
        self.image = pygame.image.load('./graphics/goku.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)  

        # Sets the direction that the player can walk in
        self.direction = pygame.math.Vector2()

        # Sets the player speed
        self.speed = 5


        self.obstacle_sprites = obstacle_sprites

    # Collision Detection for obstacles
    # Time stamp on tutorial: 42:00
    def collision(self, direction):
        
        # If the player is moving left or right, checks for collisions, then stops player on that side of the obstacle
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: 
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        # If the player is moving up or down, checks for collisions, then stops player on that side of the obstacle
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: 
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

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
        self.rect.x += self.direction.x * speed
        # Collision detection if the player is moving horizontally
        self.collision('horizontal')

        self.rect.y += self.direction.y * speed
        # Collision detection if the player is moving vertically
        self.collision('vertical')
        # self.rect.center += self.direction * speed

    # Updates the player
    def update(self):
        self.input()
        self.move(self.speed)
