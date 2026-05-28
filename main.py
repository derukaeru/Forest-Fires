import pygame
pygame.init()

screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Forest Fire Simulation")
running = True

# env
BASE_SPREAD_FACTOR = 1.0
BASE_HUMIDITY = 1.0
BASE_TEMPERATURE = 1.0
BASE_WIND_STRENGTH = 1.0

CLEAR = 0
RAIN = 1
STORM = 2
DROUGHT = 3

class Environment:
    wind_strength: float = BASE_WIND_STRENGTH
    wind_direction: float = 0.0
    weather: int = CLEAR
    temperature: float = BASE_TEMPERATURE
    humidity: float = BASE_HUMIDITY

    grid_width = 64
    grid_height = 64
    grid = []

    def generate_grid(self):
        pass

# tile
BASE_BURN_TIME = 10.0
BASE_MOISTURE = 1.0
BASE_FUEL = 1.0

GROUND = 0
TREE = 1
PLANT = 2
ROCK = 3

HEALTHY = 0
BURNING = 1
BURNT = 2
WET = 3

class Tile:
    type: int = GROUND
    state: int = HEALTHY
    burn_time: float = BASE_BURN_TIME
    moisture: float = BASE_MOISTURE
    fuel: float = BASE_FUEL

    def spread(self):
        pass

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # sim
    screen.fill((32, 8, 22))
    pygame.display.flip()

pygame.quit()
