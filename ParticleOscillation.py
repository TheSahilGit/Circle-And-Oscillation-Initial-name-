import pygame
import numpy as np
import matplotlib.pyplot as plt


def calcLoop(initX, initY):
    t = 0
    xPos = initX
    yPos = initY
    xVel = 0
    yVel = 0
    dt = 0.001
    step = 100000

    xs = []
    ys = []
    time = []

    w = 1
    for i in range(step):
        xAcc = - w * w * xPos
        yAcc = - w * w * yPos

        xPos += dt * xVel
        yPos += dt * yVel

        xVel += dt * xAcc
        yVel += dt * yAcc

        t += dt

        xs.append(xPos)
        ys.append(yPos)
        time.append(t)

    return time, xs, ys


'''plt.plot(time, xs, label='x')
plt.plot(time, ys, label='y')
plt.legend()
plt.show()'''

pygame.init()

width = 800
height = 600
balck = (0, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def point(x, y):
    pygame.draw.circle(screen, balck, (int(x), int(y)), 6, 6)


xo = width / 2.
yo = height / 2.
scale = 10

time,xs,ys= calcLoop(30,0)

for i in range(len(time)):
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    point(scale * xs[i] + xo, scale * ys[i] + yo)

    pygame.display.update()
    clock.tick(1000)
