# solution cell
### BEGIN SOLUTION


def validating_sum_of_squares(inp: list[int | float | str | bool]) -> list[bool]:
    outp: list[bool] = []
    for i in inp:
        z: bool = False
        try:
            i = int(i)
            if isinstance(i, int):
                for x in range(i + 1):
                    y: int = i - x
                    if ((y ** 0.5).is_integer() or y == 1) and (
                        (x ** 0.5).is_integer() or x == 1
                    ):
                        z = True
                        break
                    z = False
        except Exception:
            z = False
        outp.append(z)
    return outp


### END SOLUTION
