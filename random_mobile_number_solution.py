# solution cell
### BEGIN SOLUTION
import random


def random_mobile_number_generator() -> str:
    pref: list[str] = ["0", "46", "+46"]
    nmbr: str = random.choice(pref) + str(random.randint(1, 9))
    i: int = 0
    while i < 8:
        nmbr = nmbr + str(random.randint(0, 9))
        i = i + 1
    return nmbr


### END SOLUTION
