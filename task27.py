#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!


str_int = '8 5 12 12 15'
str_ = 'hello'

str_int2 = '8 5 12 12 15 , 0 23 15 18 12 4 !'
str_2 = 'hello, world!'

def s(str_int, str_):
    return ' '.join([x if y.isdigit() else y for x, y in zip(str_, str_int.split()) ])




print(s(str_int, str_))
print(s(str_int2, str_2))








