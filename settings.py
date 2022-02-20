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


# Map Settings
# vertical_tile_number = 11
# tile_size = 64

# screen_height = vertical_tile_number * tile_size
# screen_width = 1200

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

# enemy
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'./audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'./audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'./audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'./audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}

# Level 0

level_0 = {
	'Bridge': '.\custom_map\level_0_Bridge.csv',
	'Buildings': '.\custom_map\level_0_Buildings.csv',
	'Constraints': '.\custom_map\level_0_Constraints.csv',
	'Enemies': '.\custom_map\level_0_Enemies.csv',
	'fauna': '.\custom_map\level_0_fauna.csv',
	'Ground': '.\custom_map\level_0_Ground.csv',
	'Player': '.\custom_map\level_0_Player.csv',
	'Rocks': '.\custom_map\level_0_Rocks.csv',
	'Trees': '.\custom_map\level_0_Trees.csv'}
