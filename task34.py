# todo: Перепишите игру "Поле чудес" на классах.
import random
import uuid
import datetime
# from lesson_5.code.db import DICT_DEFENITION_WORD
#
#
# class Yakubovich:
#     def __init__(self):
#         pass
#
#     def print_menu(self):
#         pass
#
#     def start_game(self):
#         pass
#
#     def save_game(self):
#         pass
#
#     def end_game(self):
#         pass
#
#     def load_game(self):
#         pass
#
#     def _generate_key(self) -> str:
#         pass
#
#
# game = Yakubovich()
# game.print_menu()



import random
import uuid
import datetime
from db import DICT_DEFENITION_WORD


class Ya_g():
    word = None
    mask_ = []
    session_uuid = None
    name = None

    def __init__(self):
        self.name = input('Введите имя: ')
        self.menu_()


    def menu_(self):
        menu_s = [['1. Начать игру', self.start_game],
                      ['2. Сохранить игру', self.save_game],
                      ['3. Загрузить игру', self.load_game],
                      ['4. Выход из игры', self.end_game]]
        for x in menu_s: print(x[0])

        while True:
            pm = input('Выберите пункт меню ').strip()
            pm = int(pm) if pm.isdigit() else None
            if pm in list(range(1, len(menu_s))):
                menu_s[pm - 1][1]()
                for x in menu_s: print(x[0])

    def start_game(self, str_save=None):
        if not str_save:
            self.word = self._generate_key()
            self.mask_ = ['x'] * len(self.word)
            self.session_uuid = uuid.uuid4()
        else:
            self.mask_ = list(str_save[4].strip())
            self.session_uuid = str_save[1]
            self.word = str_save[3]
            self.name = str_save[2]

        print('Для возврата наберите - меню')
        while 'x' in self.mask_:
            print(self.mask_)
            letter = input('Введите букву ').strip().lower()
            if letter == 'меню':
                self.save_game()
                break
            self.mask_ = [y if y.lower() == letter else x for x, y in zip(self.mask_, self.word)]


    def save_game(self):
        if self.mask_:
            sv = input('Хотите сохранить игру(да/нет)?: ').strip().lower()
            if sv == 'да':
                f = open("ya_save.csv", "at")
                dt = datetime.datetime.now()
                mask_str = ''.join(self.mask_)
                str_save = f'{dt}|{self.session_uuid}|{self.name}|{self.word}|{mask_str}\n'
                f.write(str_save)
                f.close()
                print('Игра сохранена!')
        else: print('Нет игры для сохранения')


    def load_game(self):
        f = open("ya_save.csv", "r+")
        ld_list = f.readlines()
        f.close()

        for key, x in enumerate(ld_list):
            print(key, '.   ', x)
        ld = int(input('Введите номер игры для загрузки: ').strip())
        str_save = ld_list[ld].split('|')
        self.start_game(str_save=str_save)


    def end_game(self):
        print('end_game')
        quit(0)


    def _generate_key(self) -> str:
        keys = list(DICT_DEFENITION_WORD.keys())
        random.shuffle(keys)
        return keys.pop()



if __name__ == '__main__':
    game = Ya_g()













































































