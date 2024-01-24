# solution cell
### BEGIN SOLUTION


def convert_days_to_ymd(x: int) -> list[int]:
    y: int = int(x // 365.25)
    m: int = int((x - y * 365.25) // 30.4375)
    d: int = int(x - y * 365.25 - m * 30.4375)
    return [y, m, d]


### END SOLUTION
