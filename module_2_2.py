first = input('Введите число: ')
second = input('Введите число: ')
third = input('Введите число: ')
if first==second and second==third:
    print('3')
elif first==second or first==third or second==third:
    print('2')
elif first!=second and second!=third and first!=third:
    print('0')