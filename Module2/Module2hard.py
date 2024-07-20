first_stown = int(input('Число на первом камне?: '))
pswd = []
mas = [i for i in range(1, first_stown)]
while mas != []:
    for j in range(1, len(mas)):
        if not first_stown % mas[0] + mas[j]:
            pswd += [mas[0]] + [mas[j]]
    del mas[0]
print(pswd)
