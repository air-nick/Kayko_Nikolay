# 1st programm
print (9**0.5*5)

#2nd programm
print (9.99>9.98 and 1000!=1000.1)

#3rd program
print (2*2+2)
print (2*(2+2))
print ((2*2+2)==(2*(2+2)))

#4th program
print ((int (123.456*10))-int (123.456)*10)

# Исходная строка
input_string = '123.456'

# Разделяем строку на целую и дробную части
integer_part, fractional_part = input_string.split('.')

# Получаем первую цифру после запятой
first_digit_after_dot = fractional_part[0]

# Выводим результат на экран
print(first_digit_after_dot)
