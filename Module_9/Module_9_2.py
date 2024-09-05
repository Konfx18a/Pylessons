from pprint import pprint

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_rezult = [len(x) for x in first_strings if len(x) >5]
print(first_rezult)
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)
third_rezult = {x: len(x) for x in second_strings + first_strings if not len(x) % 2}
pprint(third_rezult)