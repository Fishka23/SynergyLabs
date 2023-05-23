with open('flights.txt', 'w') as file:
    file.write('SU101, Москва, 10:00, 12:30, 100\n')
    file.write('SU102, Санкт-Петербург, 11:00, 13:00, 50\n')
    file.write('SU103, Новосибирск, 15:00, 22:00, 75\n')
    file.write('SU104, Краснодар, 12:00, 16:00, 80\n')
    file.write('SU105, Анталия, 14:00, 16:30, 75\n')
    file.write('SU106, Стамбул, 11:50, 14:30, 124\n')
city = input('Введите город: ')
time = input('Введите время: ')

with open('flights.txt', 'r') as file:
    for line in file:
        flight = line.split(', ')
        if flight[1] == city and flight[2] >= time:
            print(f'Рейс {flight[0]} отпправляется в {flight[2]}, доступно {flight[4]} мест')

