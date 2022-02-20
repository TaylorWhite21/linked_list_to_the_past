#1280 960
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

# UI Settings
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = './graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111' 
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#weapon
weapon_data = { 
'sword': {'cooldown':100, 'damage': 15, 'graphic': './graphics/weapons/sword/full.png'},
'lance' : {'cooldown':400, 'damage': 30, 'graphic': './graphics/weapons/lance/full.png'},
'sai' : {'cooldown':400, 'damage': 30, 'graphic': './graphics/weapons/sai/full.png'}
}

# magic
ki_data = {
  'ki_blast': {'strength': 5, 'cost': 30, 'graphic': './graphics/particles/ki_blasts/ki_blast_right.png'},
  # 'heal': {'strength': 5, 'cost': 30, 'graphic': './graphics/particles/ki_blast.png'}
}
