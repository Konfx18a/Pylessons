# Да, задача показалась настолько простой, что всего не учел. 
def get_multiplied_digits(number):
    str_number = str(number)
    # Ну или так str_number=str_number.replace('0','1')
    if int(str_number[0])==0:
        str_number='1'+str_number[1:]
    if len(str_number) <= 1:
        return int(str_number[0])
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))
print(get_multiplied_digits(int(input('Введите цело число:'))))

