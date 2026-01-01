from functions import Calculator
from datetime import datetime

def write_log(message):

    with open("calc.log", "a", encoding="utf-8") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{current_time}] {message}\n")

def operations_start():

    my_calc = Calculator()

    write_log("=== Нова сесія користувача ===")
    
    while True:
        try:
            print("\n--- Калькулятор ---")
            a = float(input("Введіть перше число: "))
            operation = input("Вибери операцію братанчик (+, -, *, /): ")
            b = float(input("Введіть друге число: "))
            
            log_text = f"ВВЕДЕННЯ: Число_1='{a}', Операція='{operation}', Число_2='{b}'"
            write_log(log_text)
            
            result = my_calc.calculate(a, b, operation)

            write_log(f"РЕЗУЛЬТАТ: Успішно. Відповідь = {result}")

            print("Результат:", result)

        except ValueError:
            print("Введіть цифри, а не літери ")
            write_log("ПОМИЛКА: ValueError (введено літери замість цифр)")
        except SyntaxError:
            print("Вводь лише те, що тебе просять і не більше 1-го символа ")
            write_log("ПОМИЛКА: SyntaxError")
        except OverflowError:
            print("занадто велике число для розрахунку")
            write_log("ПОМИЛКА: OverflowError (занадто велике число)")
        except ZeroDivisionError:
            write_log("ПОМИЛКА: ZeroDivisionError (спроба ділення на 0)")
            print("Error: ділення на нуль, ну що ти робиш братик?")

        cont = input("Хочеш продовжити? (так/ні): ").strip().lower()
        if cont != "так":
            print("Бувай")
            write_log("=== Сесія завершена ===\n")
            break