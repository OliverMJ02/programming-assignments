# solution cell
### BEGIN SOLUTION
from collections import deque


def deque_intersection(d_one: deque[str], d_two: deque[str]) -> deque[str] | None:
    if isinstance(d_one, deque) and isinstance(d_two, deque):
        queue: deque[str] = deque()
        item_one: str
        item_two: str
        for item_one in d_one:
            for item_two in d_two:
                if item_one == item_two:
                    queue.append(item_one)
    else:
        return None
    return queue


### END SOLUTION
