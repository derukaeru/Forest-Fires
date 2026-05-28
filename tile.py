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

    def spread(self) -> None:
        pass
