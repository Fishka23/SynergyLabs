my_array = ['a', 'b', 'c', 'a', 'd', 'e']
print(my_array)
s = str(input('Какой символ ищем? '))
for element in my_array:
    count_a = my_array.count(s)
print('Символ',s,'встречатеся', count_a,'раз' )