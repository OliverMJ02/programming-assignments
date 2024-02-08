# solution cell
### BEGIN SOLUTION
from typing import Optional


class Person:
    def __init__(
        self,
        name: str,
        role: str,
        persn: str,
        addr: Optional[str] = None,
        phonen: Optional[str] = None,
    ) -> None:
        self.p: list[str | None] = [name, role, persn, addr, phonen]

    def __repr__(self) -> str:
        r: str = ""
        t: int = 0
        for i in self.p:
            if i is not None and t == 0:
                r = r + i
                t = 1
            elif i is not None:
                r = r + "\t" + i
        print(r)
        return r


### END SOLUTION
