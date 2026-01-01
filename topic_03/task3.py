student = {
     "name":"Bob", 
     "phone":"0631234567", 
     "birthday":"19.08.2004", 
     "surname":"Henderson"
}
def show_menu():
    print("\n--- Тестування методів списку ---")
    menu_items = ["update()", "del()", "clear()", "keys()", "values()", "items()"]
    for i, item in enumerate(menu_items):
        print(f"{i}. {item}")

while True:
        show_menu()
        choice = input("Вибери дію (0-5): ").strip()

        if choice == "0":
            key = input("Що саме ти хочеш оновити? ")
            value = input("Введи нове значення: ")
            student.update({key: value})
            print(f"Дані оновлено: {key}: {student[key]}")
            print(student)

        elif choice == "1":
            key = input("Що саме ти хочеш видалити? ")
            if key in student:
                del student[key]
                print(f"Ключ '{key}' успішно видалено.")
                print(student)
            else:
                print(f"Ключ '{key}' не знайдено.")
                print(student)
        elif choice == "2":
            key = input("Що саме ти хочеш очистити? ")
            if key in student:
                student[key] = ""
                print(f"Ключ '{key}' успішно очищено.")
                print(student)
            else:
                print(f"Ключ '{key}' не знайдено.")
                print(student)

        elif choice == "3":
            for i in student:
                print (i)

        elif choice == "4":
            for value in student.values():
                print(value)

        elif choice == "5":
            for k, v in student.items():
                print (k, v)