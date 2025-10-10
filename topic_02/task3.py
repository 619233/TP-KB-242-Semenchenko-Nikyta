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
    match operation:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multiply(a, b)
        case "/":
            return divide(a, b)

a = float(input("Введіть перше число: "))
operation = input("Вибери операцію братанчик (+, -, *, /): ")
b = float(input("Введіть друге число: "))

result = calculate(a, b, operation)
print("Результат:", result)