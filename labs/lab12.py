def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a*b) // gcd(a,b)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Наибольший общий делитель: ", gcd(num1, num2))
print("Наименьшее общее кратное: ", lcm(num1, num2))