
import pgzrun
import pgzero

WIDTH = 800
HEIGHT = 600

# CENÁRIO
bg = Actor("galaxia")
white = (255, 255, 255)

alien = Actor('grey') #JOGADOR
alien.pos = (400, 550)

coin = Actor('coingold')


def draw():
    screen.clear()
    bg.draw()
    alien.draw()

pgzrun.go()