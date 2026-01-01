import sys
from student import Student
from student_list import StudentList
from utils import Utils

def main():
    my_list = StudentList()

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "lab3.csv"

    Utils.load_from_file(file_name, my_list)

    while True:
        choice = input("Action [C create, U update, D delete, P print, X exit]: ").strip().upper()
        
        match choice:
            case "C":
                print("--- Creating new student ---")
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                birthday = input("Enter birthday: ")
                surname = input("Enter surname: ")
                new_student = Student(name, phone, birthday, surname)
                my_list.add_student(new_student)

            case "U":
                print("--- Updating student ---")
                name = input("Enter name to update: ")
                new_phone = input("Enter new phone: ")
                my_list.update_student(name, new_phone)

            case "D":
                print("--- Deleting student ---")
                name = input("Enter name to delete: ")
                my_list.delete_student(name)

            case "P":
                print("--- Student List ---")
                for student in my_list.get_all():
                    print(student)

            case "X":
                Utils.save_to_file(file_name, my_list)
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()