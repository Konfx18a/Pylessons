def print_params(a = 1, b='строка', c=True):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    # print(d)
def test(*params):
    for i in params:
        print(i)
    print(*params)
value_list = [1, 1.1 , 'a']
value_dict = dict(a = 1, b = 'строка', c = True)
print_params(*value_list)
print_params(**value_dict)
value_list_2 = ['abcd', 55.46]
print_params(*value_list_2,[1,2,3,4,5])
print('---',)
test(value_list)
test(value_list_2)
print('-------')
print_params(1,3, c=[1,2,3])
print('----1---')
print_params(1,b=25)
print('----2---')
print_params(a=[1,2,3])
print('----3---')
print_params(4,'d',False)
print('----4---')
print_params(5,6,7)
print('----5---')
print_params()

