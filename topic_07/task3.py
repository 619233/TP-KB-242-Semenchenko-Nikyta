class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент {self.name}, вік: {self.age}"

group = [
    Student("Андрій", 21),
    Student("Оксана", 19),
    Student("Максим", 25),
    Student("Ірина", 20)
]

sorted_group = sorted(group, key=lambda student: student.age)

print("Список студентів відсортований за віком")
for student in sorted_group:
    print(student)