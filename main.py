import pygame, sys
from settings import *
from level import Level
from buttons import *

# from debug import debug

class Game:
  def __init__(self):
    pygame.init()
     
    # Sets the size of the game screen. Sizes are grabbed from settings.py
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.MAIN_MENU_MUSIC = pygame.mixer.Sound('./audio/menu_music.wav')
    # Sets the name at the top left of the game window
    pygame.display.set_caption("Linked List To The Past")

    # Creates an object to track time
    self.clock = pygame.time.Clock()
    
    # Instantiates the Level
    self.level = Level() 
  
  def get_font(self, size):
    return pygame.font.Font('./graphics/font/Capture_it.ttf', size)

  def play(self):
      self.MAIN_MENU_MUSIC.stop()
      main_sound =pygame.mixer.Sound('./audio/main.wav')
      main_sound.set_volume(0.3)
      main_sound.play(loops = -1)
      while True:
          game.run()

  def main_menu(self):
      self.MAIN_MENU_MUSIC.play()
      while True:

          self.MAIN_MENU_MUSIC.set_volume(0.2)
          self.screen.blit(BACKGROUND, (150, 0))

          MENU_MOUSE_POS = pygame.mouse.get_pos()

          PLAY_BUTTON = Button(image=pygame.image.load('./graphics/title/Options Rect.png'), pos=(375, 675), 
                              text_input="PLAY", font=self.get_font(25), base_color="#d7fcd4", hovering_color="Gold")
          OPTIONS_BUTTON = Button(image=pygame.image.load('./graphics/title/Options Rect.png'), pos=(675, 675), 
                              text_input="Credits", font=self.get_font(25), base_color="#d7fcd4", hovering_color="Gold")
          QUIT_BUTTON = Button(image=pygame.image.load('./graphics/title/Options Rect.png'), pos=(975, 675), 
                              text_input="QUIT", font=self.get_font(25), base_color="#d7fcd4", hovering_color="Gold")

          for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
              button.changeColor(MENU_MOUSE_POS)
              button.update(self.screen)

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              if event.type == pygame.MOUSEBUTTONDOWN:
                  if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                      self.play()
                  if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                      self.credits()
                  if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                      pygame.quit()
                      sys.exit()

          pygame.display.update()

  def credits(self):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        self.screen.fill("black")

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(self.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    self.main_menu()

        pygame.display.update()

  # Runs the game and checks if the player has exited
  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      # Determines what color the screen background will be
      self.screen.fill(WATER_COLOR)

      # Calls the run method inside of the level class in level.py
      self.level.run()

      # Updates portions of the screen for software displays
      pygame.display.update()

      # Sets our FPS, imported from settings
      self.clock.tick(FPS)


if __name__ == '__main__':
  game = Game()
  game.main_menu()
