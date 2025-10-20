#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

ln = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"

aa = [x for x in range(97, 123)]
print('len', len(aa))

for key in range(1, 100):
    str_ = ''
    for x in ln:
        if ord(x) in aa:
            str_ += chr(aa[(aa.index(ord(x)) + key) % 26])
            # print(x, ord(x), aa.index(ord(x)), aa.index(ord(x)) + 1, chr(aa[(aa.index(ord(x)) + 1) % 26]))

        else: str_ += x

    print(key, str_)

 # ответ: сдвиг 46 'although that way may not be obvious at first unless you're dutch'






















