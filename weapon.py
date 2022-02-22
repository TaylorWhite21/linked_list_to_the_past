import pygame 

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups): 
        super().__init__(groups)

        # gets us the player direction using status and splits the other player postions (ex. up_idle) at the _ so its just 'up'
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]

        # #graphic of the weapon (2:51)
        full_path = f"./graphics/weapons/{player.weapon}/{direction}.png"
        self.image = pygame.image.load(full_path).convert_alpha()

        # #weapon placement 
        #     #sets the mid position of the player box to the middle opposite position of the weapons box + an offest to line up weapon where sprite's hand appears
        if direction == 'right': 
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-10,6))
        elif direction == 'left': 
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(10,6))
        elif direction == 'down': 
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(11,-4)) 
        else:
        #     #  when direction == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-15,7))


