#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................

gl = {'а': 0, 'о': 0, 'у': 0, 'э': 0, 'и': 0, 'ы': 0, 'е': 0, 'ё': 0, 'ю': 0, 'я': 0}

f = open("message.txt", "r+", encoding='utf-8')
file_list = f.readlines()

for ln in file_list:
    for x in ln:
        if x.lower() in gl:
            gl[x.lower()] +=  1

for key, value in gl.items():
    print(f'Количество букв {key} - {value}')



