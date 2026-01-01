def show_menu():
    print("\n--- Тестування методів списку ---")
    menu_items = ["extend()", "append()", "insert(id, val)","remove(val)","clear()","sort()","reverse()","copy()","Exit" ]
    for i, item in enumerate(menu_items):
        print(f"{i}. {item}")


def main():
    my_list = ["James", "William", "Benjamin", "Alexander", "Henry", "Samuel", "Jack", "Oliver", "Ethan", "Mason", "Logan", "Caleb", "Nathan", "Owen", "Leo"]

    while True:
        show_menu()
        choice = input("Вибери дію (0-9): ").strip()

        if choice == "0":
            vals = input("Введи значення через кому: ").split(",")
            my_list.extend(vals)
            print("Ну шо ты голова, додав я твої знячення, не бійся", vals)
        
        elif choice == "1":
            val = input("Вводь, тільки одне, стримуйся: ")
            my_list.append(val)
            print("Все готово, йди гуляй:", val)

        elif choice == "2":
            try:
                index = int(input("Введи індекс, куди вставляти будемо: "))
                val = input("Що вставлятимемо: ")
                my_list.insert(index, val)
                print(f"Все готово, перевіряй: вставлено {val} на позицію {index}")
            except ValueError:
                print("Ти шо, окунь? Число пиши, Ч-И-С-Л-О, понабирають...по объявлению...")

        elif choice == "3":
            val = input("Введи значення для видалення: ")
            try:
                my_list.remove(val)
                print("remove(): видалено", val)
            except ValueError:
                print("Не знайшли цього..., може ти помилився, перевір братанчик")

        elif choice == "4":
            my_list.clear()
            print("clear(): прочистили цей список, тепер все з нуля, а треба було думати раніше, так-так")

        elif choice == "5":
            try:
                my_list.sort()
                print("sort(): відсортували цей смітник, можеш тепер не паритись")
            except TypeError:
                print("ERROR: не все ж в одну топку, як казав один філософ: https://www.youtube.com/watch?v=U9IdMWqzzZY")

        elif choice == "6":
            my_list.reverse()
            print("reverse(): прийняли перевернуту позу")

        elif choice == "7":
            copied = my_list.copy()
            print("copy(): копія зроблена, насолоджуйся плагіатом:", copied)

        elif choice == "8":
            print("Наша історія завершена на цьому, побачимось у наступрону житті <3")
            break

        else:
            print("Ну кааамооон, вибери щось зі списку, тут тобі не ювелірка...")     
main()