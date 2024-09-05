# NB!!
def all_variants(text):
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


obj = all_variants('abcdefghijk')

for i in obj:
    print(i)


