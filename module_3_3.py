# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Примеры вызовов функции с разным количеством аргументов
print_params()                      # Вызов без аргументов
print_params(10)                    # Вызов с одним аргументом
print_params(b=25)                  # Вызов с изменением второго параметра
print_params(c=[1, 2, 3])           # Вызов с изменением третьего параметра

# 2. Распаковка параметров
values_list = [100, 'Пример', False]  # Список с тремя элементами разных типов
values_dict = {'a': 3.14, 'b': 'Текст', 'c': [5, 6, 7]}  # Словарь с тремя ключами

# Передача списка и словаря с использованием распаковки
print_params(*values_list)           # Распаковка списка
print_params(**values_dict)          # Распаковка словаря

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']    # Список с двумя элементами
print_params(*values_list_2, 42)     # Распаковка списка + отдельный параметр


