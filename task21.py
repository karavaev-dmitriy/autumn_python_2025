#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?

# Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?

# Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?

# Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?


# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True

# Настройки базы данных
# db_host     =  5432
# .....

file = open('config_default.txt', 'r+', encoding='utf-8')
file_list = file.readlines()
file_list = [x.split() for x in file_list]

for y in file_list:
    y[2] = str(config_values[y[0]])

file_str = [' '.join(x1) + '\n' for x1 in file_list]
file.seek(0)
file.writelines(file_str)

print(file_str)
file.close()














