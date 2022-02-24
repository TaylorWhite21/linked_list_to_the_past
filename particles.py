import pygame
from support import import_folder
from random import choice

class ParticleAnimationPlayer:
  def __init__(self):
    self.frames = {
    #monster attacks
    'claw': import_folder('./graphics/particles/claw'),
    'slash': import_folder('./graphics/particles/slash'),
    'sparkle': import_folder('./graphics/particles/sparkle'),
    'leaf_attack': import_folder('./graphics/particles/leaf_attack'),
    'thunder': import_folder('./graphics/particles/thunder'),

    #player attack
    'sword_slash': import_folder('./graphics/particles/sword_slash'),

    #grass destroyed
    'leaf_explode': import_folder('./graphics/particles/leaf_explode')
    }

  def reflect_images(self, frames):
    new_frames = []
    for frame in frames:
      flipped_frame = pygame.transform.flip(frame, True, False)
      new_frames.append(flipped_frame)
    return new_frames

  def create_particles(self, anim_type, pos, spr_groups):
    animation_frames = self.frames[anim_type]
    ParticleEffect(pos, animation_frames, spr_groups)

  def create_grass_particles(self, pos, spr_groups):
    animation_frames = self.frames['leaf_explode']
    ParticleEffect(pos, animation_frames, spr_groups)

class ParticleEffect(pygame.sprite.Sprite):
  def __init__(self, pos, animation_frames, spr_groups):
    super().__init__(spr_groups)
    self.frame_index = 0
    self.animation_speed = 0.6
    self.frames = animation_frames
    self.image = self.frames[self.frame_index]
    self.rect = self.image.get_rect(center = pos)

  def animate(self):
    self.frame_index += self.animation_speed
    if self.frame_index >= len(self.frames):
      self.kill()
    else:
      self.image = self.frames[int(self.frame_index)]

  def update(self):
    self.animate()