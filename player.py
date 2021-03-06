
import pygame
from entity import Entity 
from settings import *
from support import import_folder

class Player(Entity): 

    def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack):
        super().__init__(groups)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.last = pygame.time.get_ticks()
        self.delay = 4000
        self.play_death = False
        self.death_sound =pygame.mixer.Sound('./audio/shiiiiit.wav')

        # Sets the player image
        self.image = pygame.image.load('./graphics/player/down/down_0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #hitbox is slightly different size than sprite
        self.hitbox = self.rect.inflate(0,-26) 

        # graphics setup
        self.import_player_assets()
        self.status = 'down'
        
        #defines whether player is in control of character or not
        self.player_controls = True

        #MOVEMENT
            # Sets the direction that the player can walk in
        self.direction = pygame.math.Vector2()

        # attack variables
        self.attacking = False
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

        #make the weapon timer
        self.can_switch_weapon = True 
        self.weapon_switch_time = None 
        self.switch_duration_cooldown = 200      
        
        # Stats        
        self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'ki': 4, 'speed': 6}
        # Sets the player health
        self.health = self.stats['health']
        # Sets the player energy
        self.energy = self.stats['energy']
        # Sets the player speed
        self.speed = self.stats['speed']

        # damage on timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500
        self.hit_stun_duration = 250

        #import sound
        self.weapon_attack_sound = pygame.mixer.Sound('./audio/sword.wav')
        self.weapon_attack_sound.set_volume(0.3)

    # imports player resources
    def import_player_assets(self):
        # sets the file path before importing
        character_path = './graphics/player/'
        # Dictionary of player states
        self.animations = {'up': [], 'down': [], 'left':[], 'right':[], 'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [], 'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': [], 'hit_down': [], 'hit_up': [], 'hit_left': [], 'hit_right': [], 'hit_down_idle': [], 'hit_up_idle': [], 'hit_left_idle': [], 'hit_right_idle': [], 'death': []}
        # Goes through dictionary assigns the path and fills the key with the animation
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    # Collision Detection for obstacles
    # Time stamp on tutorial: 42:00
    

    # Gets keyboard input and moves in desired direction
    # http://www.pygame.org/docs/ref/key.html
    def input(self):
        if self.player_controls == True:
            if not self.attacking: 
            
                keys = pygame.key.get_pressed()

                # Moves up or down and will stop moving if nothing is pressed
                if keys[pygame.K_UP]:
                    self.direction.y = -1
                    self.status = 'up'
                elif keys[pygame.K_DOWN]:
                    self.direction.y = 1
                    self.status = 'down'
                else:
                    if self.vulnerable:
                        self.direction.y = 0

                # Moves left or right and will stop moving if no key is pressed
                if keys[pygame.K_LEFT]:
                    self.direction.x = -1
                    self.status = 'left'
                elif keys[pygame.K_RIGHT]:
                    self.direction.x = 1
                    self.status = 'right'
                else:
                    if self.vulnerable:
                        self.direction.x = 0

                # attack input
                if keys[pygame.K_SPACE]:
                    if self.status == 'hit_down':
                        self.status = 'down'
                    if self.status == 'hit_up':
                        self.status = 'up'
                    if self.status == 'hit_left':
                        self.status = 'left'
                    if self.status == 'hit_right':
                        self.status = 'right'

                    self.attacking = True
                    # Grabs time that attack was done
                    self.attack_time = pygame.time.get_ticks()  
                    self.create_attack()
                    self.weapon_attack_sound.play()
                    
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

    def get_status(self):
        # Runs if we are not moving
        if self.direction.x == 0 and self.direction.y == 0:
            # Checks if status already contains idle
            if not 'death' in self.status:
                if not 'idle' in self.status and not 'attack' in self.status and self.vulnerable:
                    self.status = self.status + '_idle'

        if self.attacking and self.vulnerable:
            # keeps player from moving while attacking
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status and not 'death' in self.status:
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


    # Sets player cooldown in between attacks
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            # Checks if enough time has passed since attacking
            if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
                self.attacking = False
                self.destroy_attack()
        if not self.can_switch_weapon: 
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_weapon: 
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.hit_stun_duration:
                if self.status == 'hit_down':
                    self.status = 'down'
                if self.status == 'hit_up':
                    self.status = 'up'
                if self.status == 'hit_left':
                    self.status = 'left'
                if self.status == 'hit_right':
                    self.status = 'right'

                self.player_controls = True
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
        # Gets animation from dictionary based off player status
        animation = self.animations[self.status]
        
        # Loops through frame index to animate player walking
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if not 'death' in self.status:
                self.frame_index = 0
            else:
                self.frame_index = 15
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)     


    def who_hit_me(self, enemy_ref):
        enemy_vec = pygame.math.Vector2(enemy_ref)
        player_vec = pygame.math.Vector2(self.rect.center)
        
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            self.direction = (player_vec - enemy_vec).normalize() 
                  

        
    def get_hit(self):
        if not self.vulnerable:
            if self.player_controls == False:                
                if self.direction.x < 0: 
                    self.status = 'hit_right'
                if self.direction.x > 0:
                    self.status = 'hit_left'
                if self.direction.y > 0:
                    self.status = 'hit_up' 
                if self.direction.y < 0:
                    self.status = 'hit_down'
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
            self.move(self.speed*.5)            
        else:
            self.image.set_alpha(255)

    def get_full_weapon_damage(self):
        base_damage =self.stats['attack']
        weapon_damage=weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage

    def death_sequence(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(WIN_FONT, WIN_FONT_SIZE)
        text = self.font.render('You Died! Press R to restart or M for Main Menu', True, self.green, self.blue)
        textRect = text.get_rect()
        textRect.center = (600, 675)
        self.screen.fill("black")
        self.screen.blit(GAME_OVER, (150, 0))
        self.display_surface.blit(text, textRect)
        if self.play_death == False:   
            self.death_sound.play()
            self.play_death = True
            

    def your_dead(self):
        self.player_controls = False
        self.direction.x = 0 
        self.direction.y = 0
        self.status = 'death'
        now = pygame.time.get_ticks()
        if now - self.last >= self.delay:
            self.death_sequence()

    # Updates the player
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.get_hit()
        self.move(self.speed)
