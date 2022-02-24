import pygame
from settings import *
import enemy_count

class UI:
  def __init__(self):
    
    self.display_surface = pygame.display.get_surface()
    self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
    self.white = (255, 255, 255)
    self.black = (0, 0, 0)
    self.green = (0, 255, 0)
    self.blue = (0, 0, 128)
    self.X = 700
    self.Y = 700

    # Bar setup
    # To change health and energy bar locations, change the integers and to change the size, change the variables in settings
    self.health_bar_rect = pygame.Rect(10, 10,HEALTH_BAR_WIDTH, BAR_HEIGHT)

    # Converts weapon dictionary into a list to be used in the weapon overlay
    self.weapon_graphics = []
    for weapon in weapon_data.values():
      path = weapon['graphic']
      weapon = pygame.image.load(path).convert_alpha()
      self.weapon_graphics.append(weapon)
  
  def enemies_left(self, enemy_count):
    self.display_surface = pygame.display.get_surface()
    font = pygame.font.Font('./graphics/font/joystix.ttf', 18)
    text = font.render(str(enemy_count)+ ' Enemie(s) left', True, self.green, self.white)
    textRect = text.get_rect()
    textRect.center = (self.X, self.Y)
    self.display_surface.blit(text, textRect)

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

  # Displays player stats
  def display(self, player):
        # Calls show bar method and passes in current health, max health, the health bar location and the color
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)

        # Box for weapon
        self.weapon_overlay(player.weapon_index)
        self.enemies_left(enemy_count.enemy_count)
