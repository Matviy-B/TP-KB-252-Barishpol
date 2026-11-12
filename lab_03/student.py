class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self):
        return f"Студент: ім'я - {self.name}, телефон - {self.phone}, пошта - {self.email}, група - {self.group}"

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email, "group": self.group}
