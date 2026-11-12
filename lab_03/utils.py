import csv

from student import Student
from student_list import StudentList

FIELDS = ["name", "phone", "email", "group"]


class Utils:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        student_list = StudentList()
        with open(self.file_name, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_list.add(Student(row["name"], row["phone"], row["email"], row["group"]))
        return student_list

    def save(self, student_list):
        with open(self.file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            for student in student_list.students:
                writer.writerow(student.to_dict())
