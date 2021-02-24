my_list = []
extra_sum1 = 0
extra_sum2 = 0

for number in range(1, 1000, 2):
    number = number ** 3
    my_list.append(number)
print(my_list)
print("  ")

# Первая часть 1
for number in my_list:

    n = number
    sum_dig = 0

    while n != 0:
        last_digit = n % 10
        sum_dig += last_digit
        n = n // 10

    if sum_dig % 7 == 0:
        extra_sum1 += number

print("Сумма по условию 1 = ", extra_sum1)

# Вторая часть, с + 17 к элементам списка
for number in my_list:

    n = number + 17
    sum_dig = 0

    while n != 0:
        last_digit = n % 10
        sum_dig += last_digit
        n = n // 10

    if sum_dig % 7 == 0:
        extra_sum2 += number + 17
print("Сумма по условию 2 = ", extra_sum2)
