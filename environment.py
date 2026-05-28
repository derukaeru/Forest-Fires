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
    def __init__(self, wd: float = 0.0, w: float = CLEAR, ws: float = BASE_WIND_STRENGTH, temp: float = BASE_TEMPERATURE, hum: float = BASE_HUMIDITY) -> None:
        self.wind_strength = ws
        self.wind_direction = wd
        self.weather = w
        self.temperature = temp
        self.humidity = hum

    wind_strength: float
    wind_direction: float
