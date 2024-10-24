def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []
    # Внешний цикл по строкам
    for i in range(n):
        # Создаем строку, заполненную значениями value
        row = []
        for j in range(m):
            row.append(value)
        # Добавляем строку в матрицу
        matrix.append(row)
    return matrix
# Пример вызова функции и вывод результата
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
# Пример вывода в виде матрицы
print("В виде матрицы")
for row1 in result1:
    print(row1)
for row2 in result2:
    print(row2)
for row3 in result3:
    print(row3)