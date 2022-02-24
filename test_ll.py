import pytest
from support import import_csv_layout
from player import Player
from enemy import Enemy
from level import Level
from weapon import Weapon
from main import Game
from particles import ParticleAnimationPlayer

# pytestmark = [pytest.mark.version_1, pytest.mark.version_2]

# @pytest.mark.skip('Pygame Dependence')
def test_create_map():
    terrain_map = import_csv_layout('./map/custom_map/level_1_objects.csv')
    assert terrain_map

@pytest.mark.skip('Pygame Dependence')
def test_create_player():
    player = Player(pos,groups,obstacle_sprites,create_attack,destroy_attack)
    assert player

@pytest.mark.skip('Pygame Dependence')
def test_create_enemy():
    enemy = enemy(monster_name,pos,groups,obstacle_sprite,damage_player, trigger_sword_slash_particles)
    assert enemy

@pytest.mark.skip('Pygame Dependence')
def test_create_level():
    level = Level()
    assert level

@pytest.mark.skip('Pygame Dependence')
def test_create_weapon():
    weapon = Weapon(player,groups)
    assert weapon

@pytest.mark.skip('Pygame Dependence')
def test_run_game():
    game = Game()
    assert game.run()

@pytest.mark.skip('Pygame Dependence')
def test_particles():
    animation_player = ParticleAnimationPlayer()
    assert animation_player.create_grass_particles(pos, spr_groups)
    assert animation_player.create_particles(anim_type, pos, spr_groups)