import random
from git import Actor
from pgzero.keyboard import keyboard
from pgzero.game import screen

WIDTH = 650
HEIGHT = 500

TITLE = 'Space Invasion'
FPS = 30

Bg = ("galaxia")
player = Actor('player_blue', (345, 450))
enemy = []
Mode = 'Game'
Count = 0
laser = []

# MOVIMENTAÇÃO DO INIMIGO
for i in range(5):
    a = random.randint(1, 2)
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    if a == 1:
        enemy1 = Actor('enemy_red' (x, y))
    else:
        enemy1 = Actor('enemy_orange' (x, y))
        enemy1.speed = random.randint(2, 8)
        enemy.append(enemy1)

def draw():
    if Mode == "Game":
        Bg.draw()
        player.draw()
        for i in range(len(enemy)):
            enemy[i].draw()
        for i in range(len(laser)):
            laser[i].draw()
        screen.draw.text('Score:', pos = (10, 10), collor = ('white'), fontsize = (24))
        screen.draw.text(Count, pos = (150, 10), color = 'white',  fontsize = (24))
    elif Mode == "end":
        Bg.draw()
        screen.draw.text("Game over! Press Enter!", center = (300, 200), collor = 'white', fontsize = (36))

def enemy_ship():
    for i in range(len(enemy)):
        if enemy[i].y < 650:
            enemy[i].y = enemy[i].y + enemy[1].speed
        else:
            enemy.pop(i)
            new_enemy()

def new_enemy():
    a = random.randint(1, 2)
    x = random.randint(0, 400)
    y = -50

    if a == 1:
        enemy1 = Actor("enemy_red", (x, y))
    else:
        enemy1 = Actor('enemy_orange', (x, y))
        enemy1.speed = random.randint(2, 8)
        enemy.append(enemy1)

        def collisions():
            global Mode
            global Count

for i in range(len(enemy)):
    if player.colliderect(enemy[i]):
        Mode = 'end'
for j in range(len(laser)):
    if laser[j].colliderect(enemy[i]):
        enemy.pop(j)
        new_enemy()
        Count = Count+1
        break

def updade(dt):
    global Mode
    global laser
    global count

    if keyboard.left and player.x > -20:
        player.x = player.x - 5
    elif keyboard.right and player.x < 650:
        player.x = player.x + 5
    elif keyboard.up and player.y > 0:
        player.y = player.y -5
    elif keyboard.down and player.y >-10:
        player.y = player.y + 5
    elif keyboard.enter:
        Mode = 'Game'
    enemy_ship()
    collisions()

    if Mode == 'game':
            enemy_ship()
            collisions()

    for i in range(len(laser)):
        if laser[i].y < 0:
            laser.pop(i)
            break
        else:
            laser[i].y = laser[i].y - 10

def on_key_down(key):
    global Mode, player
    global Count

    if Mode == 'Game' and key == keys.space:
        laser = Actor('bomb')
        laser.pos = player.pos














