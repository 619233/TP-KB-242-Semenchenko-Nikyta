import random

def main():
    options = ["stone", "scissor", "paper"]

    while True:
        user_input = input("Введи stone, scissor або paper: ").strip().lower()

        if user_input == 'exit':
            print("Гру завершено.")
            break

        if user_input not in options:
            print(f"Помилка: Вибери одне з значень: {options}")
            continue

        computer_choice = random.choice(options)
        print(f"Комп'ютер обрав: {computer_choice}")

        if user_input == computer_choice:
            print("Нічия! Спробуйте ще раз.")
            
        elif (user_input == "stone" and computer_choice == "scissor") or \
             (user_input == "scissor" and computer_choice == "paper") or \
             (user_input == "paper" and computer_choice == "stone"):
            print("Ти переміг!")
            
        else:
            print("Машина перемагає!")
main()