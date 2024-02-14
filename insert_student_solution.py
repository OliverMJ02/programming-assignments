# solution cell
### BEGIN SOLUTION
import datetime
import pickle
from typing import Optional

from database_setup import db
from student_class import Student


def insert_student(
    nm: str,
    bd: datetime.date,
    prsn: str,
    phn: Optional[str],
    ad: Optional[str],
) -> int:
    existing_data = db.get("dataset")
    if existing_data:
        list_students = pickle.loads(existing_data)
    else:
        list_students = []
    student: Student = Student(nm, bd, prsn, phn, ad)
    student_exists = any(student.prsn == prsn for student in list_students)
    if student_exists:
        print("Student already exists!")
    else:
        list_students.append(student)
        db.set("dataset", pickle.dumps(list_students))
    return len(list_students)


### END SOLUTION
