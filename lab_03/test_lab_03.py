import csv

import pytest

from student import Student
from student_list import StudentList
from utils import Utils


def make_list():
    student_list = StudentList()
    student_list.add(Student("Zak", "333", "zak@gmail.com", "KB-222"))
    student_list.add(Student("Bob", "111", "bob@gmail.com", "KB-221"))
    student_list.add(Student("Emma", "222", "emma@gmail.com", "KB-221"))
    return student_list


def get_names(student_list):
    return [student.name for student in student_list.students]


def test_student_attributes():
    student = Student("Bob", "111", "bob@gmail.com", "KB-221")
    assert student.name == "Bob"
    assert student.phone == "111"
    assert student.email == "bob@gmail.com"
    assert student.group == "KB-221"


def test_student_str():
    student = Student("Bob", "111", "bob@gmail.com", "KB-221")
    assert str(student) == "Студент: ім'я - Bob, телефон - 111, пошта - bob@gmail.com, група - KB-221"


def test_student_to_dict():
    student = Student("Bob", "111", "bob@gmail.com", "KB-221")
    assert student.to_dict() == {"name": "Bob", "phone": "111", "email": "bob@gmail.com", "group": "KB-221"}


def test_add_keeps_order():
    assert get_names(make_list()) == ["Bob", "Emma", "Zak"]


def test_find_insert_position():
    student_list = make_list()
    assert student_list.find_insert_position("Adam") == 0
    assert student_list.find_insert_position("Jon") == 2
    assert student_list.find_insert_position("Zed") == 3


def test_find_position():
    student_list = make_list()
    assert student_list.find_position("Emma") == 1
    assert student_list.find_position("Nobody") == -1


def test_delete():
    student_list = make_list()
    assert student_list.delete("Emma") is True
    assert get_names(student_list) == ["Bob", "Zak"]


def test_delete_missing():
    student_list = make_list()
    assert student_list.delete("Nobody") is False
    assert len(student_list) == 3


def test_update_keeps_order():
    student_list = make_list()
    assert student_list.update("Bob", Student("Zed", "000", "zed@gmail.com", "KB-221")) is True
    assert get_names(student_list) == ["Emma", "Zak", "Zed"]


def test_update_changes_data():
    student_list = make_list()
    student_list.update("Emma", Student("Emma", "999", "emma@gmail.com", "KB-221"))
    assert student_list.students[1].phone == "999"


def test_update_missing():
    student_list = make_list()
    assert student_list.update("Nobody", Student("Adam", "0", "a@gmail.com", "KB-221")) is False
    assert len(student_list) == 3


def test_save_and_load(tmp_path):
    utils = Utils(str(tmp_path / "students.csv"))
    utils.save(make_list())
    loaded = utils.load()
    assert get_names(loaded) == ["Bob", "Emma", "Zak"]
    assert loaded.students[0].phone == "111"


def test_load_sorts_data(tmp_path):
    file_name = tmp_path / "students.csv"
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "phone", "email", "group"])
        writer.writerow(["Zak", "333", "zak@gmail.com", "KB-222"])
        writer.writerow(["Bob", "111", "bob@gmail.com", "KB-221"])
    assert get_names(Utils(str(file_name)).load()) == ["Bob", "Zak"]


def test_load_missing_file():
    with pytest.raises(FileNotFoundError):
        Utils("no_such_file.csv").load()
