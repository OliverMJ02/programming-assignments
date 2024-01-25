# solution cell
### BEGIN SOLUTION


def sphere_volume(x: int | float) -> str:
    v: int | float = (4 / 3) * 3.14 * (x ** 3)
    r: str = str(round(v, 3))
    print(r)
    return r


### END SOLUTION
