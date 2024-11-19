def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Базовый случай: если длина строки равна 1, возвращаем эту цифру как число
    if len(str_number) == 1:
        return int(str_number)

    # Первая цифра числа
    first = int(str_number[0])

    # Рекурсивно умножаем первую цифру на результат для оставшихся цифр
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Ожидается: 24
