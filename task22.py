#todo: Модифицировать программу таким образом чтобы она выводила
# приветствие "Hello", которое только что записали в файл text.txt

f = open("text.txt", "w+t")
f.write("Hello\n")
# Ваше решение.

f.seek(0)
file_list = ''.join(f.readlines()).strip()
print(file_list)

f.close()