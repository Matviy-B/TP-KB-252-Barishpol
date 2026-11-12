import csv

import pytest

from lab_02 import loadFromCsv, saveToCsv, findInsertPosition, findByName, addStudent, deleteStudent, updateStudent


def makeList():
    return [
        {"name": "Bob", "phone": "111", "email": "bob@gmail.com", "group": "KB-221"},
        {"name": "Emma", "phone": "222", "email": "emma@gmail.com", "group": "KB-221"},
        {"name": "Zak", "phone": "333", "email": "zak@gmail.com", "group": "KB-222"},
    ]


def makeStudent(name):
    return {"name": name, "phone": "000", "email": name.lower() + "@gmail.com", "group": "KB-221"}


def getNames(data):
    return [item["name"] for item in data]


def test_find_insert_position_begin():
    assert findInsertPosition(makeList(), "Adam") == 0


def test_find_insert_position_middle():
    assert findInsertPosition(makeList(), "Jon") == 2


def test_find_insert_position_end():
    assert findInsertPosition(makeList(), "Zed") == 3


def test_find_insert_position_empty_list():
    assert findInsertPosition([], "Bob") == 0


def test_find_by_name():
    assert findByName(makeList(), "Emma") == 1
    assert findByName(makeList(), "Nobody") == -1


def test_add_student_keeps_order():
    data = makeList()
    addStudent(data, makeStudent("Jon"))
    assert getNames(data) == ["Bob", "Emma", "Jon", "Zak"]


def test_delete_student():
    data = makeList()
    assert deleteStudent(data, "Emma") is True
    assert getNames(data) == ["Bob", "Zak"]


def test_delete_missing_student():
    data = makeList()
    assert deleteStudent(data, "Nobody") is False
    assert len(data) == 3


def test_update_student_keeps_order():
    data = makeList()
    assert updateStudent(data, "Bob", makeStudent("Zed")) is True
    assert getNames(data) == ["Emma", "Zak", "Zed"]


def test_update_student_changes_data():
    data = makeList()
    updateStudent(data, "Emma", {"name": "Emma", "phone": "999", "email": "emma@gmail.com", "group": "KB-221"})
    assert data[1]["phone"] == "999"
    assert len(data) == 3


def test_update_missing_student():
    data = makeList()
    assert updateStudent(data, "Nobody", makeStudent("Adam")) is False
    assert getNames(data) == ["Bob", "Emma", "Zak"]


def test_save_and_load(tmp_path):
    fileName = str(tmp_path / "students.csv")
    saveToCsv(fileName, makeList())
    assert loadFromCsv(fileName) == makeList()


def test_load_sorts_data(tmp_path):
    fileName = tmp_path / "students.csv"
    with open(fileName, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "phone", "email", "group"])
        writer.writerow(["Zak", "333", "zak@gmail.com", "KB-222"])
        writer.writerow(["Bob", "111", "bob@gmail.com", "KB-221"])
    assert getNames(loadFromCsv(str(fileName))) == ["Bob", "Zak"]


def test_load_missing_file():
    with pytest.raises(FileNotFoundError):
        loadFromCsv("no_such_file.csv")
