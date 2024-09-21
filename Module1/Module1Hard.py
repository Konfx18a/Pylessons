grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
rezult = {}
# stu_sorted = sorted(list(students))
# for i in range(len(stu_sorted)):
#     rezult[stu_sorted[i]] = sum(grades[i])/len(grades[i])
# print(rezult)
# Битый час сражался и игрался со срезами, перебрал все аттрибуты списков и кортежей
# Если не использовать функции и тупую сортировать, методом какого-нибудь пузырька или медиан, но к чему тогда Питон?))
# Впрочем ниже этот кадавр без использования функций с методом пузырька
students = list(students)
l = len(students)
# Сортировка методом пузырька
for i in range(l-1):
    for j in range(l-1-i):
        # if students[j] > students[j+1]:
        # Сравнение двух строк (имен студентов)
        # Считаем, что имена заданы в формате первая буква заглавная, остальные строчные
        # Cортировка в обратном порядке,т.к. ord('A') < ord('B')
        flag =True
        for s in range(0, min(len(students[j]), len(students[j + 1]))):
            c1 = students[j][s:s + 1]
            c2 = students[j + 1][s:s + 1]
            if c1 == c2:
                continue
            elif c1 < c2:
                flag = False
                break
            else:
                flag = True
                break

        if flag:
            students[j], students[j+1] = students[j+1], students[j]
print(students)
for i in range(len(students)):
    rezult[students[i]] = sum(grades[i])/len(grades[i])
print(rezult)

