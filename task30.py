# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]


su = {'₽': 1, 'USD': 80, '€': 90, '$': 80, '¥': 11, '': 1}


d =[float(''.join([str_ for str_ in x if str_ in '1234567890.'])) for x in prices if any(st.isdigit() for st in x)]
n = [''.join([str_ for str_ in x if str_ not in '1234567890.']) for x in prices if any(st.isdigit() for st in x)]
res = [x * su[y.strip()] for x, y in zip(d, n)]


print(res)








