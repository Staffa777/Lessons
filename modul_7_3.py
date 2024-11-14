class WordsFinder:
    def __init__(self , *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name , 'r', encoding='utf-8') as file:
                words = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(i, '')
                all_words[file_name] = words.split()
        return all_words
    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        list_words = {}
        for file_name, words in all_words.items():
            if word in words:
                list_words[file_name] = words.index(word) + 1
        return list_words
    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_counts = {}
        for file_name, words in all_words.items():
            word_counts[file_name] = word.count(word)
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
print()
