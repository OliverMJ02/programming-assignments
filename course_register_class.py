# solution cell
### BEGIN SOLUTION
from student_class import Student


class CourseRegister:
    def __init__(self, name: str, code: str) -> None:
        self.list_registered_students: list[str] = []
        self.name = name
        self.code = code

    def register(self, student: str) -> None:
        if (
            isinstance(student, Student)
            and student not in self.list_registered_students
        ):
            self.list_registered_students.append(student)

    def remove(self, student: str) -> None:
        if student in self.list_registered_students:
            self.list_registered_students.remove(student)


### END SOLUTION
