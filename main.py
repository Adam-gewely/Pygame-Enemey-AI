import pygame
from sys import exit
import classes
import brain

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pygame Enemy AI")
player = classes.Player(100, 100)
player.surface = pygame.Surface((50, 50))
player.surface.fill("Blue")
player.rect = player.surface.get_rect()
enemy = classes.Enemy(500, 100)
enemy.surface = pygame.Surface((50, 50))
enemy.surface.fill("Red")
enemy.rect = enemy.surface.get_rect()
bg = pygame.Surface((800, 400))
bg.fill("White")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.y -= 10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.y += 10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.x += 10
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.x -= 10
    brain.react(player, enemy)
    screen.blit(bg, (0, 0))
    screen.blit(enemy.surface, (enemy.x, enemy.y))
    screen.blit(player.surface, (player.x, player.y))
    pygame.display.update()
    clock.tick(60)
