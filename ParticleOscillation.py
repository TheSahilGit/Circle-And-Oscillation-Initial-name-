import pygame
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi


def calcLoop(r, theta):
    t = 0
    xPos = r * np.cos(theta)
    yPos = r * np.sin(theta)
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
black = (0, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def point(x, y):
    pygame.draw.circle(screen, white, (int(x), int(y)), 6, 6)


xo = width / 2.
yo = height / 2.
scale = 10

"""time1, xs1, ys1 = calcLoop(30, 0)
time2, xs2, ys2 = calcLoop(30, pi/4)
time3, xs3, ys3 = calcLoop(30, pi/2)
time4, xs4, ys4 = calcLoop(30, pi)
time5, xs5, ys5 = calcLoop(30, 3*pi/4)"""

step = 100000
points = 5
xs = np.zeros((points, step))
ys = np.zeros((points, step))
time = np.zeros((points, step))

theta = 0
for j in range(points):
    time[j, :], xs[j, :], ys[j, :] = calcLoop(30, theta)
    theta += pi / 4.

print(len(xs[:, 0]))
print(len(xs[0, :]))

for i in range(step):
    for j in range(points):

        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        point(scale * xs[j, i] + xo, scale * ys[j, i] + yo)

        """point(scale * xs2[i] + xo, scale * ys2[i] + yo)
        point(scale * xs3[i] + xo, scale * ys3[i] + yo)
        point(scale * xs4[i] + xo, scale * ys4[i] + yo)
        point(scale * xs5[i] + xo, scale * ys5[i] + yo)"""

        pygame.display.update()
        #clock.tick(1000)
