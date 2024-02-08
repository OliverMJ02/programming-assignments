# solution cell
### BEGIN SOLUTION
from math import pi


class VolumeCalculator:
    def __init__(self, radius: int | float) -> None:
        self.radius: int | float = radius

    def volume(self) -> None | int | float:
        a: None | int | float = None
        if self.radius is not None:
            if self.radius > 0:
                a = (self.radius ** 3) * pi * (4 / 3)
        return a


### END SOLUTION
