def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: ділення на нуль, ну що ти робиш братик?"
    return a / b

def calculate(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    
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

        cont = input("Хочеш продовжити? (так/ні): ").strip().lower()
        if cont != "так":
            print("Бувай")
            break