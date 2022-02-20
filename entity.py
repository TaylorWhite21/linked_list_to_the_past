import pygame


 #created entity.py to hold common methods shared by players and enemies e.g move and collison
class Entity(pygame.sprite.Sprite):
  def __init__(self,groups):
      super().__init__(groups)
      self.frame_index = 0
      self.animation_speed = 0.15
      self.direction = pygame.math.Vector2()


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

