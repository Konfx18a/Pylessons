def single_root_words(root, *other_words):
    same_words = []
    for i in other_words:
        if i.upper().count(root.upper()) or root.upper().count(i.upper()):
            same_words += [i]
    print ('Коренное слово', root, 'Однокоренные слова', same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')