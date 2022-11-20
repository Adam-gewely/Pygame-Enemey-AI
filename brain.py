from classes import Player
from classes import Enemy


def react(player: Player, enemy: Enemy):
    def enemy_charge():
        movement = 4
        if enemy.x > player.x:
            enemy.x -= movement
        if enemy.x < player.x:
            enemy.x += movement
        if enemy.y > player.y:
            enemy.y -= movement
        if enemy.y < player.y:
            enemy.y += movement

    enemy_charge()
