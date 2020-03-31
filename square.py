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
    for i in range(circles):
        prevx, prevy = X + xouter, Y + youter
        n = 2 * i + 1
        # Rotating point
        xouter += int(r * cos(n * Q) * (4 / (n * pi)))
        youter += int(r * sin(n * Q) * (4 / (n * pi)))
        pygame.draw.circle(win, white, (X + xouter, Y + youter), 1)

        # MAIN CIRCLE
        pygame.draw.circle(win, grey, (prevx, prevy), int(r * 4 / (n * pi)), 1)

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
    Q += 0.003
    if len(y_cords) > 2500:
        y_cords.pop()

pygame.quit()
