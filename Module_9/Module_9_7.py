def is_prime(func_sum):
    def wrraper(*el):
        summa = func_sum(*el)
        x = 2
        while summa % x !=0:
            x += 1
        if summa == x:
            return f'Сумма равна {summa} - Простое число'
        else:
            return f'Сумма равна {summa} - Сложноставное число'
    return wrraper

# @is_prime
# def sum_three(elems):
#     return sum(elems)
#
# print(sum_three([1,2,3,5]))
@is_prime
def sum_three(a, b, c):
    return a+b+c

print(sum_three(1,2,3))