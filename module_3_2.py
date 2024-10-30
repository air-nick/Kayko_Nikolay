def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на корректность e-mail адресов (наличие "@" и допустимое окончание)
    valid_domains = (".com", ".ru", ".net")
    if "@" not in recipient or not recipient.endswith(valid_domains) or "@" not in sender or not sender.endswith(
            valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
# Пример 3: Отправка с адреса по умолчанию
send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
# Пример 4: Отправка с нестандартного адреса
send_email("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.ru", sender="urban.info@gmail.com")
# Пример 1: Некорректный e-mail
send_email("Пожалуйста, исправьте задание", "urban.student@mail.ru", sender="urban.teacher@mail.uk")
# Пример 2: Отправка самому себе
send_email("Напоминаю самому себе о вебинаре", "urban.teacher@mail.ru", sender='urban.teacher@mail.ru')
