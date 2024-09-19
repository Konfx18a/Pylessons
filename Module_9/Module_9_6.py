# Вариант с while
def all_variants_with_while(text):
    i = 0
    j = 1
    step = 1
    while (j-i-1) != len(text):
        yield text[i:j]
        if j >= len(text):
            i = 0
            step += 1
            j = step
            continue
        i += 1
        j = i + step
# Вариант с for

def all_variants_with_for(text):
    size = len(text)
    for step in range(1, size+1):
        for cursor in range(size):
            if step+cursor > size:
                break
            yield text[cursor:step+cursor]

obj = all_variants_with_while('abcdefghijk')
obj1 = all_variants_with_for('abcdefghijk')

print('# Вариант с while')
for i in obj:
    print(i)

print('# Вариант с for')
for i in obj1:
    print(i)

    print(i)
