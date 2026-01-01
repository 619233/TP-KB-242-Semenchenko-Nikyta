from topic_06.task1.functions import calculate

def operations_start():
    while True:
        try:
            print("\n--- Калькулятор ---")
            a = float(input("Введіть перше число: "))
            operation = input("Вибери операцію братанчик (+, -, *, /): ")
            b = float(input("Введіть друге число: "))
            
            result = calculate(a, b, operation)
            print("Результат:", result)

        except ValueError:
            print("Введіть цифри, а не літери ")
        except SyntaxError:
            print("Вводь лише те, що тебе просять і не більше 1-го символа ")
        except OverflowError:
            print("занадто велике число для розрахунку")
        except ZeroDivisionError:
            print("Error: ділення на нуль, ну що ти робиш братик?")

            cont = input("Хочеш продовжити? (так/ні): ").strip().lower()
            if cont != "так":
                print("Бувай")
                break