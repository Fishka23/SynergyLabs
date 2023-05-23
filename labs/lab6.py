vector = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for element in vector:
    if element % 2 == 0:
        result.append(element * 2)
    else:
        result.append(element * 3)

print(result)