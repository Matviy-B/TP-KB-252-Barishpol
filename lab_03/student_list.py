class StudentList:
    def __init__(self):
        self.students = []

    def __len__(self):
        return len(self.students)

    def find_insert_position(self, name):
        position = 0
        for student in self.students:
            if name > student.name:
                position += 1
            else:
                break
        return position

    def find_position(self, name):
        for index, student in enumerate(self.students):
            if student.name == name:
                return index
        return -1

    def add(self, student):
        self.students.insert(self.find_insert_position(student.name), student)

    def delete(self, name):
        position = self.find_position(name)
        if position == -1:
            return False
        del self.students[position]
        return True

    def update(self, name, new_student):
        position = self.find_position(name)
        if position == -1:
            return False
        del self.students[position]
        self.add(new_student)
        return True

    def print_all(self):
        for student in self.students:
            print(student)
