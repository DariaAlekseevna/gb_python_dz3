""" Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

list_new = []
numbers_product = 1
number_list = list(map(float,input('Enter the elements of the list separated by a space: ').split()))
print(f'Entered list: {number_list}')

for i in range (0, len(number_list)):
    list_new.append(number_list[i] % 1)

print(list_new)

max_el = list_new[0]
i = 0
k = 0
min_el = list_new[0]
for j in range(0, len(list_new)):
    while max_el <= list_new[i]:
        max_el = list_new[i]
        i += 1
for j in range(0, len(list_new)):
    while min_el >= list_new[k]:
        min_el = list_new[k]
        k += 1

print(min_el)
print(max_el)

