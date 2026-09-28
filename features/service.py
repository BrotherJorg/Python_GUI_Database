from database.database import Database
from features.model import Student
from features.repository import StudentRepository


class StudentService:
    def __init__(self, database: Database):
        self.repository = StudentRepository(database)

    def add_student(self, student: Student) -> Student:
        return self.repository.add(student)

    def get_students(self) -> list[Student]:
        return self.repository.list()
