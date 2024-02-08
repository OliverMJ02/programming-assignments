# solution cell
### BEGIN SOLUTION
import random


def lottery_numbers(nnum: int, upb: int, lob: int) -> None | list[int]:
    li: list[int] = []
    if lob >= 0 and upb >= 1 and nnum >= 1 and upb - lob >= nnum - 1:
        for _ in range(nnum):
            b: int = random.randint(lob, upb)
            if b not in li:
                li.append(b)
            else:
                while b in li:
                    b = random.randint(lob, upb)
                li.append(b)
    else:
        return None
    return li


### END SOLUTION
