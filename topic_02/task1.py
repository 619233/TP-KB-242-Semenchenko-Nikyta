# x1 = (-b + sqrt(D))/2*a
# x2 = (-b - sqrt(D))/2*a

#2x^2 + 7x - 4 = 0
#D = 81
from math import sqrt

def find_x1_x2(a, b, D):
    if D < 0:
        return None
    else:
        x1 = (-b + sqrt(D))/(2*a)
        x2 = (-b - sqrt(D))/(2*a)
        return x1, x2

a = int(input("a: "))
b = int(input("b: "))
D = int(input("D: "))

print(find_x1_x2(a, b, D))