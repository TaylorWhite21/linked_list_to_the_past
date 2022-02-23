import pygame
from settings import *

class UI:
  def __init__(self):
    
    self.display_surface = pygame.display.get_surface()
    self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

    # Bar setup
    # To change health and energy bar locations, change the integers and to change the size, change the variables in settings
    self.health_bar_rect = pygame.Rect(10, 10,HEALTH_BAR_WIDTH, BAR_HEIGHT)
    # self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)


    # Converts weapon dictionary into a list to be used in the weapon overlay
    self.weapon_graphics = []
    for weapon in weapon_data.values():
      path = weapon['graphic']
      weapon = pygame.image.load(path).convert_alpha()
      self.weapon_graphics.append(weapon)

    # self.ki_graphics = []
    # for ki in ki_data.values():
    #   path = ki['graphic']
    #   ki = pygame.image.load(ki['graphic']).convert_alpha()
    #   self.ki_graphics.append(ki)

  def show_bar(self, current, max_amount, bg_rect, color):
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

    # Divides current and max health then multiplies that by the pixel width of the health background to fill health bar correctly. Ex: health is an integer at 100 and the width of the health bar is in pixels at 200, therefore they need to be calculated to fit. https://youtu.be/QU1pPzEGrqw?t=11879
    ratio = current / max_amount
    current_width = bg_rect.width * ratio
    current_rect = bg_rect.copy()
    current_rect.width = current_width

    pygame.draw.rect(self.display_surface, color, current_rect)
    pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

  def selection_box(self, left, top):
    bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
    pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
    return bg_rect

  def weapon_overlay(self, weapon_index):
    bg_rect = self.selection_box(1190, 630)
    weapon_surf = self.weapon_graphics[weapon_index]
    weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
    self.display_surface.blit(weapon_surf, weapon_rect)
    
  # def ki_overlay(self, ki_index):
  #   bg_rect = self.selection_box(1105, 630)
  #   ki_surface = self.ki_graphics[ki_index]
  #   ki_rect = ki_surface.get_rect(center = bg_rect.center)
  #   self.display_surface.blit(ki_surface, ki_rect)


  # Displays player stats
  def display(self, player):

        # Calls show bar method and passes in current health, max health, the health bar location and the color
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)

        # Same as above but for energy
        # self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)

        # Box for weapon
        self.weapon_overlay(player.weapon_index)
        # Box for ki
        # self.ki_overlay(player.ki_index)
