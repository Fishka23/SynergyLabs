with open('file1.txt', 'r') as file1:
    count = 0
    for line in file1:
        if line[0] == 'А' or line[0] == 'а':
            count += 1
with open('file2.txt', 'w') as file2:
    file2.write(str(count))  