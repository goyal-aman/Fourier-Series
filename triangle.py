import pygame
from math import *
from colors import *

pygame.init()


circles = int(input('Range: '))

X, Y = 250, 250
r = 80
Q = 0

win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("SIMULATION 2")

y_cords = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    xouter, youter = 0, 0
    for i in range(1,circles):
        prevx, prevy = X + xouter, Y + youter
        # n = 2 * i + 1
        # Rotating point
        xouter += int(r * cos(i * Q) * (2 / (i * pi)))
        youter += int(r * sin(i * Q) * (2 / (i * pi)))
        pygame.draw.circle(win, white, (X + xouter, Y + youter), 1)

        # MAIN CIRCLE
        pygame.draw.circle(win, grey, (prevx, prevy), int(r * 2 / (i * pi)), 1)

        # circle connector line
        pygame.draw.line(win, white, (prevx, prevy), (X + xouter, Y + youter), 4)

    # wave connector line
    pygame.draw.line(win, white, (X + xouter, Y + youter), (5 * r, Y + youter), 4)

    y_cords.insert(0, youter)

    # wave
    for i in range(len(y_cords)):
        pygame.draw.circle(win, white, (5 * r + i // 5, Y + y_cords[i]), 2)

    pygame.display.update()
    win.fill(black)
    Q += 0.009
    if len(y_cords) > 3000:
        y_cords.pop()

pygame.quit()
