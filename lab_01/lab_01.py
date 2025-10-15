
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "birthday":"19.08.2004", "surname":"Henderson"},
    {"name":"Emma", "phone":"0631234567", "birthday":"24.01.2007", "surname":"Mitchell"},
    {"name":"Jon",  "phone":"0631234567", "birthday":"05.04.2003", "surname":"Carter"},
    {"name":"Zak",  "phone":"0631234567", "birthday":"16.07.2005", "surname":"Reynolds"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", birthday is " + elem["birthday"] + ", surname is " + elem["surname"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    birthday = input("Please enter student birthday: ")
    surname = input("Please enter student surname: ")
    newItem = {"name": name, "phone": phone, "birthday": birthday, "surname": surname}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    # implementation required

def changeElement():
    name = input("Please enter the name to change: ")
    
    # Знаходимо індекс студента
    indexToUpdate = -1
    for index, student in enumerate(list):
        if student.get("name") == name:
            indexToUpdate = index
            break

    if indexToUpdate == -1:
        print("Студента з таким ім’ям не знайдено.")
        return

    print("Студент знайдений!")
    print("Поточні дані: ", list[indexToUpdate])

    print("Що саме ви хочете змінити?")
    print("1 - Ім’я")
    print("2 - Телефон")
    print("3 - Дата народження")
    print("4 - Прізвище")
    print("5 - Усе")

    choice = input("Ваш вибір: ")

    if choice == "1":
        new_name = input("Нове ім’я: ")
        list[indexToUpdate]["name"] = new_name
    elif choice == "2":
        new_phone = input("Новий телефон: ")
        list[indexToUpdate]["phone"] = new_phone
    elif choice == "3":
        new_birthday = input("Нова дата народження: ")
        list[indexToUpdate]["birthday"] = new_birthday
    elif choice == "4":
        new_surname = input("Нове прізвище: ")
        list[indexToUpdate]["surname"] = new_surname
    elif choice == "5":
        new_name = input("Нове ім’я: ")
        new_phone = input("Новий телефон: ")
        new_birthday = input("Нова дата народження: ")
        new_surname = input("Нове прізвище: ")
        list[indexToUpdate] = {
            "name": new_name,
            "phone": new_phone,
            "birthday": new_birthday,
            "surname": new_surname
        }
    else:
        print("Невірний вибір.")
        return

    # Сортуємо список після зміни
    list.sort(key=lambda x: x.get("name", ""))
    print("Інформацію оновлено успішно.", len(list))
    



def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, CH change,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "CH" | "ch":
                print("Please enter the name to change")
                changeElement()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()