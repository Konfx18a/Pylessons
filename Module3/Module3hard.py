def dict_to_list(**dictionary): # преобразуем словарь в список
    new_list = []
    for key, value in dictionary.items():
        new_list.append(value)
        new_list.append(len(key))
    return new_list
def list_to_cyf(list_or_tuple_or_set):
    summa=0
    for i in list_or_tuple_or_set:
        if isinstance(i, dict ):
            summa += list_to_cyf(dict_to_list(**i))
        elif isinstance(i, float) or isinstance(i, int):
            summa += i
        elif  isinstance(i, bool):
            summa += int(i)
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, list) or isinstance(i, tuple ) or isinstance(i, set ):
            summa += list_to_cyf(i)
    return summa
input_data = {'f':"[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8})", 'g':"'Hello', ((), [{(2, 'Urban', ('Urban2', 35))}])"}
# input_data = [[1, 2], {'a': 4, 'b': 5}]
if isinstance(input_data, dict): # Если головой виртуозно во сне набил словарь )))
    print(list_to_cyf(dict_to_list(**input_data)))
else:
    print(list_to_cyf(input_data))