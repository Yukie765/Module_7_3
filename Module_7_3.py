class WordsFinder:
    file_names = []
    __SIGNS = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        res = {}
        words = []
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read()
                for sign in self.__SIGNS:
                    text = text.replace(sign,'')
                words = text.strip().lower().split()
            res.update({file_name : words})
        return res

    def find(self,word):
        res_dict = {}
        dict = self.get_all_words()
        for name, words in dict.items():
            for i in range(len(words)):
                if words[i] == word.lower():
                    res_dict.update({name: i+1})
                    break
        return res_dict

    def count(self, word):
        res_dict = {}
        dict = self.get_all_words()
        for name, words in dict.items():
            find_count = 0
            for i in words:
                if i == word.lower():
                    find_count +=1
            res_dict.update({name: find_count})
        return res_dict

finder2 = WordsFinder('test73.txt')
print(finder2.get_all_words())
print('find: ', finder2.find('TEXT'))
print('count:', finder2.count('teXT'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))