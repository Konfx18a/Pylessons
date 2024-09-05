from functools import reduce

# лябда проверяет на то, что это int/float, а затем левой сверткой получаем по И
# если все элементы числа то True
def check_data(list_d):
    l = lambda x: (isinstance(x, int) or isinstance(x, float))
    if not reduce(lambda x, y: l(x) and l(y), list_d):
        raise TypeError('В списке есть не числовые параметры ')


def apply_all_func(num_list, *functions):
    rezults ={}
    for f in functions:
        rezults[f.__name__] = f(num_list)
    return rezults

list_ = [1, 4, -2, 0, 18, 0.5]
list_of_f = [min, max, sorted, len, sum]
for f in list_of_f:
    check_data(list_)
    print(apply_all_func(list_,f))
