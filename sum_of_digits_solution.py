# solution cell
### BEGIN SOLUTION


def sum_of_digits(x: int) -> int:
    a: int = x // 100
    b: int = (x - a * 100) // 10
    c: int = x - a * 100 - b * 10
    return a + b + c


### END SOLUTION
