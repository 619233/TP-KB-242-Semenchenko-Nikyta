import csv
from student import Student

class Utils:
    @staticmethod
    def load_from_file(file_name, student_list):
        """Зчитує CSV і наповнює student_list об'єктами"""
        try:
            with open(file_name, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student = Student(row["name"], row["phone"], row["birthday"], row["surname"])
                    student_list.add_student(student)
            print(f"--- Loaded data from {file_name} ---")
        except FileNotFoundError:
            print(f"--- File {file_name} not found. Starting with empty list. ---")

    @staticmethod
    def save_to_file(file_name, student_list):
        """Бере об'єкти зі списку і записує їх у CSV"""
        try:
            with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
                fieldnames = ["name", "phone", "birthday", "surname"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for student in student_list.get_all():
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "birthday": student.birthday,
                        "surname": student.surname
                    })
            print(f"--- Saved data to {file_name} ---")
        except Exception as e:
            print(f"Error saving file: {e}")