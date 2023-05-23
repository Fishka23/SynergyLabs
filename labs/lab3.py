n = int(input("Введите трехзначное число: "))
if n < 0:
    n = -n
first = n // 100
second = (n // 10) % 10
third = n % 10
if second > third:
    print("Вторая цифра больше последней")
elif third > second:
    print("Последняя цифра больше второй")
else:
    print("Вторая и последняя цифры равны")