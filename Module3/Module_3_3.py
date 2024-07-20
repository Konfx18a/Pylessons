def print_params(a = 1, b = 'строка', c = True):
    print(a)
    print(b)
    print(c)
value_list = [1, 1.1 , 'a']
value_dict = dict(a = 1, b = 'строка', c = True)
print_params(*value_list)
print_params(**value_dict)
value_list_2 = ['abcd', 55.46]
print_params(*value_list_2,[1,2,3,4,5])

