import pygame
pygame.init()

screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Forest Fire Simulation")
running = True

grid_width = 64
grid_height = 64
grid_map = []

for i in range(grid_width):
    for j in range(grid_height):
        pass

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # sim

pygame.quit()
