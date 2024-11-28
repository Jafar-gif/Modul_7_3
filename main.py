import string


class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = file_names

    def get_all_words(self):
        """Возвращает словарь с названиями файлов и списками слов из них."""
        all_words = {}


        chars_to_remove = list(string.punctuation + ' -')

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:

                    text = file.read().lower()

                    for char in chars_to_remove:
                        text = text.replace(char, " ")

                    words = text.split()


                    all_words[file_name] = words

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        """Возвращает словарь с позициями первого вхождения слова в каждом файле."""
        word_positions = {}

        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower())
                word_positions[file_name] = position

        return word_positions

    def count(self, word):
        """Возвращает словарь с количеством вхождений слова в каждом файле."""
        word_counts = {}

        for file_name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                word_counts[file_name] = count

        return word_counts



with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("It's a text for task Найти везде. Используйте его для самопроверки. Успехов в решении задачи!\n")
    f.write("text text text\n")


finder2 = WordsFinder('test_file.txt')


print(finder2.get_all_words())


print(finder2.find('TEXT'))



print(finder2.count('teXT'))
