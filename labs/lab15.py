def hex_add(a, b):
    return hex(int(a, 16) + int(b, 16))[2:]
def hex_subtract(a, b):
    return hex(int(a, 16) - int(b, 16))[2:]
def hex_multiply(a, b):
    return hex(int(a, 16) * int(b, 16))[2:]
def hex_divide(a, b):
    return hex(int(a, 16) // int(b, 16))[2:]
def bin_to_hex(binary):
    return hex(int(binary, 2))[2:]
def hex_to_decimal(hexadecimal):
    return int(hexadecimal, 16)
def is_valid_hex(hexadecimal):
    hex_digits = set("0123456789abcdefABCDEF")
    for char in hexadecimal:
        if char not in hex_digits:
            return False
    return True
a = input("Введите шестнадцатеричное число a: ")
b = input("Введите шестнадцатеричное число b: ")
if not is_valid_hex(a) or not is_valid_hex(b):
    print("Неверный формат введенного числа! Пожалуйста, введите число в шестнадцатеричной форме.")
else:
    print(f"a + b = {hex_add(a, b)}")
    print(f"a - b = {hex_subtract(a, b)}")
    print(f"a * b = {hex_multiply(a, b)}")
    print(f"a // b = {hex_divide(a, b)}")
hexadecimal = input("Введите шестнадцатеричное число для конвертации в десятичную систему: ")
if not is_valid_hex(hexadecimal):
    print("Неверный формат введенного числа! Пожалуйста, введите число в шестнадцатеричной форме.")
else:
    print(f"{hexadecimal} в десятичной системе счисления равно {hex_to_decimal(hexadecimal)}")