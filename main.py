
# from settings import *
# from debug import debug
import os

# try:
#   os.environ["Display"]
# except:
#   os.environ['SDL_VIDEODRIVER']='directx'
#   os.environ['SDL_AUDIODRIVER'] = 'dsp'
# # os.environ["SDL_AUDIODRIVER"]="dummy"
import pygame, sys
pygame.init()

class Game:
  def __init__(self):
    pygame.init()    
    self.screen = pygame.display.set_mode((800,600))
    self.clock = pygame.time.Clock()

  def run(self):
    while True:
      print(pygame.display.update)
      self.screen.fill((252,0,0))
      pygame.display.update()   
      # self.screen.fill('black')
      # pygame.display.update()
      self.clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

if __name__ == '__main__':
  game = Game()
  game.run()
