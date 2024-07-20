count=0
def count_call ():
    global count
    count +=1
def string_info(string):
    count_call()
    return len(string), string.upper(), string.lower()
def is_contain(string, string_list):
    count_call()
    for i in string_list:
        if (i.lower() == string.lower()):
            return True
    return False
s = 'asdfg', 'qwerty', 'qwertyasdfgzxcvb'
s1 = 'asdfg', 'zxcv'
for i in s1:
    print(string_info(i))
    print(is_contain(i, s))
print('Количество вызовов count_call = ', count)
