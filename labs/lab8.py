text = str(input('Текст, который мы хотим проверить:'))
consonants = set('бвгджзйклмнпрстфхцчшщ')
result = sorted(filter(lambda letter: letter in consonants, text.lower()))

print('Согласные буквы в алфавитном порядке:')
print(*result)