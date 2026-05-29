import environment as env
import grid as gr
import tile

import pygame
pygame.init()

screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Forest Fire Simulation")
running = True

grid = gr.Grid()
environment  = env.Environment()

# game

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # sim
    screen.fill((32, 8, 22))
    pygame.display.flip()

pygame.quit()
