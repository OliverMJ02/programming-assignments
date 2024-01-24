# solution cell
### BEGIN SOLUTION


def print_sum_of_digits(x: int) -> str:
    a: int = x // 100
    b: int = (x - a * 100) // 10
    c: int = x - a * 100 - b * 10
    y: str = str(a + b + c)
    return print(y)


### END SOLUTION
