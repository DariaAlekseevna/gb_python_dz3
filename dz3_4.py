""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

list = []
ost = 0
number = int(input('enter a number: '))
if number == 0:
    print(f'Decimal number {number} -> Binary number: {number}')
else:
    print(f'Decimal number {number} -> Binary number: ', end='')
    while number > 0:
        ost = number % 2
        list.append(ost)
        number = number // 2
    for i in range(1, len(list)+1):
        print(list[len(list) - i], end='')
        