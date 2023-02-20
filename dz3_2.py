""" Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

i = 0
res_list = []
numbers_product = 1
number_list = list(map(int,input('Enter the elements of the list separated by a space: ').split()))
print(f'Entered list: {number_list}')

rev_list = list(reversed(number_list))

while i < len(number_list)/2:
    numbers_product = number_list[i] * rev_list[i]
    res_list.append(numbers_product)
    i += 1
print(f'Product of pairs of numbers: {res_list}')
