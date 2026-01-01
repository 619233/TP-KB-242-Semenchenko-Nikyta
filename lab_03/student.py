class Student:
    def __init__(self, name, phone, birthday, surname):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.surname = surname

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Birthday: {self.birthday}, Surname: {self.surname}"