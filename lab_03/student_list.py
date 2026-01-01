from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        insert_position = 0
        for item in self.students:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        print("New element added.")

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("Element deleted.")
                return
        print("Element not found.")

    def update_student(self, name, new_phone):
        for student in self.students:
            if student.name == name:
                student.phone = new_phone
                print("Updated.")
                return
        print("Not found.")

    def get_all(self):
        return self.students