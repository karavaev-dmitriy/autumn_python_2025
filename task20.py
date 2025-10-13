#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

file = open('inverted_sort.txt', 'a+', encoding='utf-8')
file.seek(0)
file_list = file.readlines()
file_list.reverse()
file_list[0] = file_list[0] + '\n'
file.writelines(['\n', '\n'])
file.writelines(file_list)

file.close()



