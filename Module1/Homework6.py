voc={'A': 0, 'B': 1, 'C': 3, 'D': True}
print(voc)
print(voc['B'])
print(voc.get('E'))
voc.update({'E': 1.1, 'F': 'qwerty'})
print(voc)
print(voc.pop('B'))
print(voc)
my_set={1,1,2,4,'A','a','B','B',True,True}
print(my_set)
my_set.add(1.1)
my_set.update((4.5 , 5.5))
my_set.add((True,5))
print(my_set)