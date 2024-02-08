# solution cell
### BEGIN SOLUTION
import statistics


def gm_median(li: list[int | float]) -> tuple[int | float, int | float]:
    gmean: int | float = statistics.geometric_mean(li)
    median: int | float = statistics.median(li)
    res: tuple[int | float, int | float] = gmean, median
    return res


### END SOLUTION
