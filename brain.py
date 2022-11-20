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
    # For later AI
    # entity_x_difference = abs(player.x - enemy.x)
    # entity_y_difference = abs(player.y - enemy.y)
    # total_distance = entity_x_difference + entity_y_difference
    enemy_charge()
