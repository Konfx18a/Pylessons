def personal_sum(numbers):
    rezult = 0
    incorrect_data = 0
    for i in numbers:
        try:
            rezult += i
        except TypeError as exte:
            print(f'Не корректный тип данных для подсчета суммы, {i}')
            incorrect_data += 1
    return rezult, incorrect_data

def calculate_average(numbers):
    try:
        summ = personal_sum(numbers)
        return summ[0]/(len(numbers) - summ[1])

    except ZeroDivisionError as exzd:
        return 0

    except TypeError as exte:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 5: {calculate_average("")}') 
