class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Я кіт, мене звати {self.name}"

my_cat = Cat("Мурчик")
print(my_cat) 