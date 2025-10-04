# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"

age = int(age)
foo = int(foo[:2])

print(age)
print(foo)

# Преобразуйте переменную age в Boolean
age1 = "123abc"

age1 = bool(age1)

print(age1)

# Преобразуйте переменную flag в Boolean

flag = 1
flag = bool(flag)
print(flag)



# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

str_one = bool(str_one)
str_two = bool(str_two)

print(str_one)
print(str_two)

# Преобразуйте значение 0 и 1 в Boolean

print(bool(0))
print(bool(1))

# Преобразуйте False в строку

print(str(False))