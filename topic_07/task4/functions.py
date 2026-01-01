class Calculator:

    def __init__(self):
        self.name = "SuperCalc"
    
    def __str__(self):
        return f"Це об'єкт класу Calculator: {self.name}"

    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b

    def calculate(self, a, b, operation):
        if operation == "+":
            return self.add(a, b)
        elif operation == "-":
            return self.subtract(a, b)
        elif operation == "*":
            return self.multiply(a, b)
        elif operation == "/":
            return self.divide(a, b)