""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""

list = []
sum = 0
n = int(input('Enter the number of elements in the list (n): '))
for i in range (0, n):
    list.append(int(input('Enter list element: ')))
print(f'Entered list: {list}')


for i in range(1, n, 2):
    sum += (list[i])
print(f'Sum of the elements at odd position: {sum}')