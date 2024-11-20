def calculate_structure_sum(data_structure):
    total_sum = 0

    def recursive_sum(item):
        nonlocal total_sum
        # Если элемент - число, добавляем его к сумме
        if isinstance(item, int):
            total_sum += item
        # Если элемент - строка, добавляем длину строки
        elif isinstance(item, str):
            total_sum += len(item)
        # Если элемент - список, кортеж или множество, рекурсивно обрабатываем его элементы
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                recursive_sum(sub_item)
        # Если элемент - словарь, обрабатываем его ключи и значения
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)
                recursive_sum(value)

    # Запускаем рекурсивный подсчёт
    recursive_sum(data_structure)
    return total_sum

# Тестовые данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вычисление суммы
result = calculate_structure_sum(data_structure)
print(result)
