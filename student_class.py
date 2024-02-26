# solution cell
### BEGIN SOLUTION
from typing import Optional

from person_class import Person


class Student(Person):
    def __init__(
        self,
        name: str,
        person_number: str,
        program: str,
        phone_number: Optional[str] = None,
        address: Optional[str] = None,
    ) -> None:
        super().__init__(name, "Student", person_number, phone_number, address)
        self.program = program

    def print(self) -> None:
        st = super().__repr__()
        st += f"\t{self.program}"
        print(st)


### END SOLUTION
