# solution cell
### BEGIN SOLUTION, "fields" was not required (defined age in __init__())
import datetime
from dataclasses import dataclass


@dataclass
class PersonAge:
    def __init__(self, name: str, job: str, birthdate: datetime.date) -> None:
        self.name: str = name
        self.job: str = job
        self.bd: datetime.date = birthdate
        self.age: int

    def compute_age(self) -> int:
        today = datetime.datetime.now().date()
        timedelta: datetime.timedelta = today - self.bd
        self.age = timedelta.days // 365
        return int(self.age)


### END SOLUTION
