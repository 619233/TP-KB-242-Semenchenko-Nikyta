#2x^2 + 7x - 4 = 0
#D = 81

def findD(a, b, c):
    D = b**2 - 4*a*c
    return D

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print(findD(a, b, c))