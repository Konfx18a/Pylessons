# import randUnivers as rU
numbers = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numbers = rU.rInt(100 , 20)
prost = []
neprost = []
for i in numbers:
    is_prost = True
    if i == 1:
        neprost += [1]
        continue
    for j in range(2, i):
        if not i % j:
            is_prost = False
    if not is_prost:
        neprost += [i]
    else:
        prost += [i]
print('Последовательность случайных целых чисел:', numbers)
print('Простые числа: ', prost)
print('Не простые числа: ', neprost)
