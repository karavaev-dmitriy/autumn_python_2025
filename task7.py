#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().


a, b, c = map(lambda x: float(x), input('Введите значение точек А B C: ').split())


ac = a - c if a > c else c - a
bc = b - c if b > c else c - b
ac_bc = ac + bc


print('ac: ', ac)
print('bc: ', bc)
print('ac_bc', ac_bc)









