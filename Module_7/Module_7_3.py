class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        kill_punct = ',', '.', '=', '!', '?', ';', ':', ' ', ' - '
        for i in self.file_names:
            stroka =''
            with open(i, 'r', encoding='utf-8') as file:
                for line in file:
                    for key in kill_punct:
                        line = line.lower().replace(key, " ")
                    stroka += line
            all_words[i] = stroka.split()
        return all_words

    # def get_all_words(self):
    #     all_words = {}
    #     kill_punct = ''.maketrans(',' '.' '=' '!' '?' ';' ':', ' '*7)
    #     for i in self.file_names:
    #         stroka =''
    #         with open(i, 'r', encoding='utf-8') as file:
    #             for line in file:
    #                  stroka += line.lower().translate(kill_punct).replace(' - ', " ")
    #         all_words[i] = stroka.split()
    #     return all_words

    def find(self, word):
        rez_dict = {}
        for key, value in self.get_all_words().items():
            count = 0
            for i in value:
                if i == word.lower():
                    rez_dict[key] = count + 1
                    break
                else:
                    count += 1
        return rez_dict


    def count(self, word):
        rez_dict = {}
        for key, value in self.get_all_words().items():
            count = 0
            for i in value:
                if i == word.lower():
                    count += 1
            rez_dict[key] = count
        return rez_dict

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
