# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.


f = open("message.txt", "r+", encoding='utf-8')

AA = [x for x in range(1040, 1072)]
aa = [x for x in range(1072, 1104)]

AA.insert(6, 1025)
aa.insert(6, 1105)

file_list = f.readlines()

str_ = ''
for key, ln in enumerate(file_list, 1):
    for x in ln:
        if ord(x) in AA:
            str_ += chr(AA[(AA.index(ord(x)) + key) % 33] )
        elif ord(x) in aa:
            str_ += chr(aa[(aa.index(ord(x)) + key) % 33])

        else: str_ += x

print(str_)
f.writelines('\n')
f.writelines('\n')
f.writelines(str_)

# for key, x in enumerate(list(file_list[0])):
#     if ord(x) in AA:
#         print(ord(x), x)
#
#         str_ += chr(ord(x) + 1) #if (ord(x) + 1) > 1071 else chr(ord(x) - 31)
#
#     elif ord(x) in aa:
#         print(ord(x), x)
#
#         str_ += chr(ord(x) + 1) #if (ord(x) + 1) > 1103 else chr(ord(x) - 31)
#
#     else: str_ += x


# print(str_)

# print(file_list)
#
# print(ord('А'))
# print(ord('Я'))
# print(ord('а'))
# print(ord('я'))











