# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"



print('''
 Сортировка:
    1. По возрасту
    2. По первой букве
    3. По группе
    ''')

n  = input('выберите пункт меню: ')


match n:
    case '1':
        age = int(input('введите возраст: '))

        age_lst = [x for x in users if x['age'] > age]
        for x in age_lst: print(x)

    case '2':
        first = input('введите первую букву: ')

        first_letter = [x1 for x1 in users if x1['login'][0].lower() == first.lower()]
        for x1 in first_letter: print(x1)

    case '3':
        group = input('введите группу: ')

        group_lst = [x2 for x2 in users if x2['group'].lower() == group.lower()]
        for x2 in group_lst: print(x2)




























