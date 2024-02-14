# solution cell
### BEGIN SOLUTION
import statistics


def gm_calculation(inp: list[int | float | str]) -> str | None:
    num: list[float] = []
    for i in inp:
        try:
            i = float(i)
            if isinstance(i, float):
                num.append(i)
        except Exception:
            pass
    if not num:
        return None
    gm: float = statistics.geometric_mean(num)
    outp: str = f"{gm:.2f}"
    return outp


### END SOLUTION
