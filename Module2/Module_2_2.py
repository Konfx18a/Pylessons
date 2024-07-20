first = input('Введите первое число: ')
secound = input('Введите второе  число: ')
third = input('Введите третье число: ')
if first == secound == third:
    print(3)
elif first == secound or first == third or secound == third:
    print(2)
else:
    print(0)

