""" Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

int_list = []
fract_list = []

number_list = list(map(float,input('Enter the elements of the list separated by a space: ').split()))
print(f'Entered list: {number_list}')

for i in range(len(number_list)):
    int_list.append(number_list[i]//1)
    fract_list.append(round(number_list[i] - int_list[i], 6))

maxi = 0
mini = 1
diff = 0

for i in range(len(fract_list)):
    if fract_list[i] != 0:
        if fract_list[i] > maxi:
            maxi = fract_list[i]
        if fract_list[i] < mini:
            mini = fract_list[i]

diff = round(maxi - mini, 5)
if diff == -1:
    print('all numbers are integer')   
else:
    print(f'difference between max and min of the fractional part: {diff}')
