# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.

# Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")



class Temperature():

    def __init__(self, temp):
        self._temp = temp

    @property
    def celsius(self):
        return self._temp

    @celsius.setter
    def celsius(self, temp):
        self._temp = temp


    @property
    def fahrenheit(self):
        return (self._temp - 32)/1.8

    @fahrenheit.setter
    def fahrenheit(self, temp):
        self._temp = (temp - 32)/1.8


    @property
    def kelvin(self):
        return self._temp - 273.15

    @kelvin.setter
    def kelvin(self, temp):
        self._temp = temp - 273.15



t = Temperature(25)
print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")

t.fahrenheit = 32
print(f"После установки 32F: {t.celsius}C")






















