
import pygame
from settings import *
from entity import Entity
from support import *
from player import *

class Enemy(Entity):
  def __init__(self, monster_name,pos,groups,obstacle_sprite,damage_player):
      super().__init__(groups)
      self.sprite_type = 'enemy'

      # grphics setup
      self.import_graphics(monster_name)
      self.status = 'idle'
      self.image = self.animations[self.status][self.frame_index]

      # movement
      self.rect = self.image.get_rect(topleft = pos)
      self.hitbox = self.rect.inflate(0,-10)
      self.obstacle_sprites = obstacle_sprite

      #stats
      self.not_dead = True
      self.monster_name = monster_name 
      monster_info = monster_data[self.monster_name]
      self.health = monster_info['health']
      self.exp = monster_info['exp']
      self.speed = monster_info['speed']
      self.attack_damage = monster_info['damage']
      self.resistance = monster_info['resistance']
      self.attack_radius = monster_info['attack_radius']
      self.notice_radius = monster_info['notice_radius']
      self.attack_type = monster_info['attack_type']

      # player interaction
      self.can_attack = True
      self.attact_time = None
      self.attact_cooldown = 400
      self.damage_player = damage_player

      #timer
      self.vulnerable = True
      self.hit_time = None
      self.invincibility_duration = 300
      self.death_timer = 900



  # importing different graphic for enemies in different states
  def import_graphics(self,name):
    self.animations = {'idle':[],'move':[],'attack':[], 'skull':[]}
    main_path = f'./graphics/monsters/{name}/'
    for animation in self.animations.keys():
      self.animations[animation] = import_folder(main_path + animation)

  # get the location of player
  def get_player_distance_direction(self,player):
    enemy_vec = pygame.math.Vector2(self.rect.center)
    player_vec = pygame.math.Vector2(player.rect.center)
    distance = (player_vec - enemy_vec).magnitude()

    if distance >0:
      direction =(player_vec - enemy_vec).normalize()

    else:
      direction = pygame.math.Vector2()

    return (distance, direction)

  # track status of player
  def get_status(self,player):
    distance = self.get_player_distance_direction(player)[0]

    if self.status != 'skull':
      if distance <= self.attack_radius and self.can_attack:
        if self.status != 'attack':
          self.frame_index = 0
        self.status = 'attack'
      elif distance <= self.notice_radius:
        self.status = 'move'
      else:
        self.status = 'idle'

  def actions(self,player):
    if self.status == 'attack':
      if player.vulnerable:
        self.attact_time = pygame.time.get_ticks()
        
        self.damage_player(self.attack_damage, self.attack_type,self.rect.center)
        self.direction.x = 0
        self.direction.y = 0
    elif self.status == 'move':
      self.direction = self.get_player_distance_direction(player)[1]
    else:
      self.direction = pygame.math.Vector2()


  def animate(self):
    
    animation = self.animations[self.status]
    self.frame_index += self.animation_speed
    if self.frame_index >= len(animation):
      if self.status == 'attack':
        self.can_attack = False
      self.frame_index = 0

    self.image = animation[int(self.frame_index)]
    self.rect = self.image.get_rect(center = self.hitbox.center)

    if not self.vulnerable:
      alpha =self.wave_value()
      self.image.set_alpha(alpha)

    else:
      self.image.set_alpha(255)

  def cooldowns(self):
    current_time = pygame.time.get_ticks()
    if not self.can_attack:
      current_time = pygame.time.get_ticks()
      if current_time - self.attact_time > self.attact_cooldown:
        self.can_attack = True
    if not self.vulnerable:
      if current_time - self.hit_time >= self.invincibility_duration:
        self.vulnerable = True


  def get_damage(self,player,attack_type):
    if self.vulnerable:
      self.direction = self.get_player_distance_direction(player)[1]
      if attack_type == 'weapon':
        self.health -= player.get_full_weapon_damage()
      else:
        pass
      self.hit_time = pygame.time.get_ticks()
      self.vulnerable = False

  def check_death(self):
    current_time = pygame.time.get_ticks()

    if self.health <=0:
      if self.not_dead == True:
        self.dead_time = pygame.time.get_ticks()
        self.not_dead = False
      self.status = 'skull'
      print(f'my status: {self.status}')
      if current_time - self.dead_time >= self.death_timer:
        self.kill()

  def hit_reaction(self):
    if not self.vulnerable:
      self.direction *= -self.resistance

  def update(self):
    self.hit_reaction()
    self.move(self.speed)
    self.animate()
    self.cooldowns()
    self.check_death()

  def enemy_update(self,player):
    self.get_status(player)
    self.actions(player)


