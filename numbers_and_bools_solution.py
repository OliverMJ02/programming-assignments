# solution cell
### BEGIN SOLUTION
from typing import Sequence


def numbers_and_bools(
    data: Sequence[bool | int | float],
) -> tuple[list[bool], list[int | float]]:
    bool_list: list[bool] = []
    number_list: list[int | float] = []
    for item in data:
        if isinstance(item, bool):
            bool_list.append(item)
        elif isinstance(item, int | float):
            number_list.append(item)
    return bool_list, number_list


### END SOLUTION
