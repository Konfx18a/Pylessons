grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stu_sorted = sorted(list(students))
rezult = dict()
for i in range(len(stu_sorted)):
    rezult[stu_sorted[i]] = sum(grades[i])/len(grades[i])
print(rezult)
# Извиняюсь, но не знаю, как не используя знаний из последующих тем решить эту задачу
# Битый час сражался и игрался со срезами, перебрал все аттрибуты списков и кортежей
# Если только в тупую сортировать , методом какого-нибудь пузырька например , но к чему тогда Питон?))