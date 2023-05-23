import math
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

D = b**2 - 4 * a * c1
print('Дискриминант =  ',D)
if D < 0:
    print("Корней нет")
elif D == 0:
    x = -b / (2*a)
    print("Уравнение имеет один корень: x =", x)
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Уравнение имеет два корня: x1 =", x1, ", x2 =", x2)