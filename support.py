import pygame
from csv import reader
from os import walk
from settings import TILESIZE

def import_csv_layout(path):
  terrain_map=[]
  with open(path) as level_map:
    layout = reader(level_map,delimiter = ',')
    for row in layout:
      terrain_map.append(list(row))
    return terrain_map


def import_folder(path):
  surface_list = []

  for _,__,img_files in walk(path):
    for image in img_files:
      full_path = path + '/' + image
      image_surf = pygame.image.load(full_path).convert_alpha()
      surface_list.append(image_surf)
  
  return surface_list

def import_cut_graphics(path):
  surface = pygame.image.load(path).convert_alpha()
  #get size return a tuple
  tile_num_x = int(surface.get_size()[0] / TILESIZE)
  print(f'tile_num_x:{tile_num_x}')
  tile_num_y = int(surface.get_size()[1] / TILESIZE)
  print(f'tile_num_y:{tile_num_y}')

  cut_tiles = []
  print('I am in import cut graphics')
  for row in range(tile_num_y):
    # print('i am in the row loop')
    for col in range(tile_num_x):
      x = col * TILESIZE
      y = row * TILESIZE
      new_surface = pygame.Surface((TILESIZE,TILESIZE))
      #https://www.pygame.org/docs/ref/surface.html
      # https://youtu.be/wJMDh9QGRgs?t=4536
      new_surface.blit(surface, (0,0), pygame.Rect(x,y,TILESIZE,TILESIZE))
      cut_tiles.append(new_surface)
      # print('i completed a blit')
  return cut_tiles








