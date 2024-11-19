def single_root_words(root_word, *other_words):
    # Приведение корневого слова к нижнему регистру
    root_word = root_word.lower()
    # Создание пустого списка для результата
    same_words = []

    # Перебор всех переданных дополнительных слов
    for word in other_words:
        # Приведение текущего слова к нижнему регистру
        word_lower = word.lower()
        # Проверка на наличие корневого слова в текущем слове или наоборот
        if root_word in word_lower or word_lower in root_word:
            # Добавление оригинального слова в результат
            same_words.append(word)

    # Возврат списка совпадающих слов
    return same_words


# Примеры использования функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов на экран
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
