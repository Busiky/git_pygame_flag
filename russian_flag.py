import math

import pygame

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
# final version

def draw():
    # fon
    pygame.draw.rect(screen, pygame.Color(200, 200, 200), (0, 0, 500, 500))

    pygame.draw.rect(screen, pygame.Color('#65350f'), (20, 20, 30, 460))
    pygame.draw.rect(screen, pygame.Color('white'), (50, 20, 430, 100))
    pygame.draw.rect(screen, pygame.Color('red'), (50, 220, 430, 100))
    pygame.draw.rect(screen, pygame.Color('blue'), (50, 120, 430, 100))
    # drawing smiling face
    pygame.draw.ellipse(screen, pygame.Color('yellow'), (400, 400, 80, 80))
    pygame.draw.arc(screen, pygame.Color('black'), (420, 440, 40, 25), math.pi, 0, 2)
    # draw eyes
    pygame.draw.ellipse(screen, pygame.Color('black'), (420, 430, 6, 6), 2)
    pygame.draw.ellipse(screen, pygame.Color('black'), (455, 430, 6, 6), 2)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
