import pygame 

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups): 
        super().__init__(groups)
        #gets us the player direction using status and splits the other player postions (ex. up_idle) at the _ so its just 'up'
        direction = player.status.split('_')[0]
        #test- this should appear top left of game screen
        # print(direction)




        #graphic of the weapon (2:51)
        full_path = f"../graphics/weapons/{player.weapon}/{direction}.png"
        self.image = pygame.image.load(full_path).convert_alpha()

        #weapon placement 
        if direction == 'right': 
            #sets the mid position of the player box to the middle opposite position of the weapons box + an offest to line up weapon where sprite's hand appears
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vecotr2(0,16))
        elif direction == 'left': 
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vecotr2(0,16))
        elif direction == 'down': 
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vecotr2(-10,0)) 
        else:
            #  when direction == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vecotr2(-10,0))


