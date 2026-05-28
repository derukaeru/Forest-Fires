BASE_GRID_WIDTH = 64
BASE_GRID_HEIGHT = 64

class Grid:
    def __init__(self, _width: int = BASE_GRID_WIDTH, _height: int = BASE_GRID_HEIGHT) -> None:
        self.grid_width = _width
        self.grid_height = _height

        self.generate_grid()

    def generate_grid(self) -> None:
        pass
