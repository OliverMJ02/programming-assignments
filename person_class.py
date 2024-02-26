# solution cell
### BEGIN SOLUTION
from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    name: str
    role: str
    person_number: str
    phone_number: Optional[str] = None
    address: Optional[str] = None

    def __repr__(self) -> str:
        outp = ""
        ls = [
            self.name,
            self.role,
            self.person_number,
            self.phone_number,
            self.address,
        ]
        for item in ls:
            if item is not None:
                outp += str(item) + "\t"
        return outp.strip()


### END SOLUTION
