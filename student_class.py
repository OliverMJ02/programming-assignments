# solution cell
### BEGIN SOLUTION
import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    def __init__(
        self,
        name: str,
        birthdate: datetime.date,
        person_number: str,
        phone_number: Optional[str],
        address: Optional[str],
    ) -> None:
        self.nm: str = name
        self.bd: datetime.date = birthdate
        self.prsn: str = person_number
        self.phn: Optional[str] = phone_number
        self.adr: Optional[str] = address


### END SOLUTION
