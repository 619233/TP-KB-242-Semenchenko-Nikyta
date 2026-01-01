import csv
import sys

student_list = [] 

def load_data(file_name):

    student_list.clear()
    try:
        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student_list.append(row)
        print(f"--- [OK] Дані завантажено з: '{file_name}' ---")
    except FileNotFoundError:
        print(f"--- [INFO] Файл '{file_name}' не знайдено. Починаємо з порожнього списку. ---")

def save_data(file_name):

    try:
        with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ["name", "phone", "birthday", "surname"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(student_list)
            print(f"--- [OK] Дані успішно збережено у '{file_name}' ---")
    except Exception as e:
        print(f"Помилка при збереженні: {e}")

def printAllList():
    if not student_list:
        print("Список порожній.")
        return
    for elem in student_list:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Birthday: {elem['birthday']}, Surname: {elem['surname']}")

def addNewElement():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    birthday = input("Enter birthday: ")
    surname = input("Enter surname: ")
    newItem = {"name": name, "phone": phone, "birthday": birthday, "surname": surname}
    
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    student_list.insert(insertPosition, newItem)
    print("New element added.")

def deleteElement():
    name = input("Enter name to delete: ")
    deletePosition = -1
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break
    if deletePosition == -1:
        print("Element not found")
    else:
        del student_list[deletePosition]
        print("Element deleted")

def changeElement():
    name = input("Enter name to update: ")
    indexToUpdate = -1
    for index, student in enumerate(student_list):
        if student.get("name") == name:
            indexToUpdate = index
            break
    
    if indexToUpdate == -1:
        print("Not found.")
        return

    print(f"Updating: {student_list[indexToUpdate]}")
    new_phone = input("Enter new phone: ")
    student_list[indexToUpdate]["phone"] = new_phone
    print("Updated.")

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print("Файл не вказано. Використовую 'lab_02/lab2.csv'")
        file_name = "lab_02/lab2.csv"

    load_data(file_name)

    while True:
        choice = input("Action [C/U/D/P/X]: ").strip().upper()
        
        match choice:
            case "C":
                addNewElement()
            case "U":
                changeElement()
            case "D":
                deleteElement()
            case "P":
                printAllList()
            case "X":
                save_data(file_name)
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()