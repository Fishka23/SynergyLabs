a = int(input("Cторона A : "))
b = int(input("Сторона B : "))

count = 0
while a > 0 and b > 0:
    if a > b:
        count += (a // b)
        a %= b
    else:
        count += (b // a)
        b %= a

print("Максимальное количество квадратов, которые можно отсечь:", count)