# solution cell
### BEGIN SOLUTION


def smallest_value(
    w: int | float, x: int | float, y: int | float, z: int | float
) -> int | float:
    a: int | float
    b: int | float
    r: int | float
    if w < x:
        a = w
    else:
        a = x
    if y < z:
        b = y
    else:
        b = z
    if a < b:
        r = a
    else:
        r = b
    return r


### END SOLUTION
