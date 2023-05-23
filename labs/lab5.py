n = int(input("Введите натуральное число: "))
dig = int(input("Введите цифру: "))
found = False
while n > 0:
    if n % 10 == dig:
        found = True
        break
    n //= 10
if found:
    print("Цифра", dig, "присутствует в числе")
else:
    print("Цифра", dig, "не присутствует в числе")