import sys
import pgzrun
import pygame
import random
from random import choice, randint

from pgzero.actor import Actor
from pgzero.game import screen

pygame.init()

WIDTH = 650
HEIGHT = 500

TITLE = 'Space Invasion'
FPS = 60  # Aumentei o FPS para animação mais suave
screen = pygame.display.set_mode((650, 500))
clock = pygame.time.Clock()

bg = Actor("galaxia")
player = Actor('player_blue', (WIDTH // 2, HEIGHT - 50))
enemies = []
lasers = []
score = 0
lives = 3

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def draw():
    screen.fill((0, 0, 0, ))
    bg.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for laser in lasers:
        laser.draw()
    screen.draw.text(f"Score: {score}", (10, 10), color=WHITE, fontsize=24)
    screen.draw.text(f"Lives: {lives}", (WIDTH - 100, 10), color=WHITE, fontsize=24)

def update(dt):
    global score, lives, lasers
    # Movimento do jogador
    if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5

    # Movimento dos inimigos
    for enemy in enemies:
        enemy.y += enemy.speed
        if enemy.bottom > HEIGHT:
            enemies.remove(enemy)
            lives -= 1
            if lives == 0:
                game_over()

    # Movimento dos lasers
    for laser in lasers:
        laser.y -= 10
        if laser.top < 0:
            lasers.remove(laser)

    # Colisões
    for laser in lasers.copy():
        for enemy in enemies.copy():
            if laser.colliderect(enemy):
                lasers.remove(laser)
                enemies.remove(enemy)
                score += 10

    # Criação de novos inimigos
    if random.randint(0, 100) < 2:
        new_enemy()

def new_enemy():
    enemy_type = choice(['enemy_red', 'enemy_orange'])
    x = randint(50, WIDTH - 50)
    enemy = Actor(enemy_type, pos=(x, -50))
    enemy.speed = randint(3, 5)
    enemies.append(enemy)

def on_key_press(key):
    if key == pygame.K_SPACE:
        laser = Actor('laser', pos=player.midtop)
        lasers.append(laser)

def game_over():
    screen.fill((0, 0, 0))
    screen.draw.text("Game Over!", center=(WIDTH // 2, HEIGHT // 2), fontsize=64, color=RED)
    screen.draw.text(f"Sua pontuação final: {score}", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=32, color=WHITE)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.flip()
            on_key_press(event.key)

    draw()
    update(clock)
    pygame.display.flip()
pgzrun.go()