a1='A'
a2=5
a3=True
a4=1.2
immutable_var= a1, a2 , a3 , a4
print(immutable_var)
#immutable_var[0]=False
# Traceback (most recent call last):
#   File "/home/and/PycharmProjects/pythonProject/Mod3Exp5.py", line 7, in <module>
#     immutable_var[0]=False
# TypeError: 'tuple' object does not support item assignment
# ТипОшибки: 'кортеж' объект не поддерживающий назначение(измение) элементов
mutable_var = [a1, a2, a3, a4]
print(mutable_var)
mutable_var.insert(2,'qwerty')
print(mutable_var)
mutable_var.remove(True)
print(mutable_var)
