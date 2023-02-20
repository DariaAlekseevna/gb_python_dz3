""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  """

number = int(input('enter a number: '))

fib1 = fib2 = 1
i = 0
op = 1
pos_list = []
neg_list = []
fin_list = []

for i in 0, 1, 1:
    pos_list.append(i)
while (i < number - 2):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    pos_list.append(fib_sum)

for i in range(1, len(pos_list)):
    neg_list.append(pos_list[i] * op)
    op *= -1

for i in range(1, len(neg_list) + 1):
        fin_list.append(neg_list[len(neg_list)-i])
for j in range(len(pos_list)):
    fin_list.append(pos_list[j])
print(f'list of Fibonacci numbers for positive and negative indices: {fin_list}')
