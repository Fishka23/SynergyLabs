s = str(input('Введите строку для поиска: '))

frag = str(input('Введите фрагмент для поиска: '))
count = s.count(frag)

print(f"Фрагмент '{frag}' входит в строку {count} раз.")