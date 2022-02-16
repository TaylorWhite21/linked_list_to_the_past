import pygame, sys
from settings import *
from level import Level

# from debug import debug

class Game:
  def __init__(self):
    pygame.init()
    
    # Sets the size of the game screen. Sizes are grabbed from settings.py
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Sets the name at the top left of the game window
    pygame.display.set_caption("Linked List To The Past")

    # Creates an object to track time
    self.clock = pygame.time.Clock()

    # Instantiates the Level
    self.level = Level() 
  
  # Runs the game and checks if the player has exited
  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      # Determines what color the screen background will be
      self.screen.fill('black')

      # Calls the run method inside of the level class in level.py
      self.level.run()

      # Updates portions of the screen for software displays
      pygame.display.update()

      # Sets our FPS, imported from settings
      self.clock.tick(FPS)


if __name__ == '__main__':
  game = Game()
  game.run()
