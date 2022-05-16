"""
ورودی نمونه:

5
hello salam
goodbye khodafez
say goftan
we ma
you shoma
we say goodbye to you tonight


خروجی نمونه:

ma goftan khodafez to shoma tonight
"""
from functools import reduce


class Translator:
    def __init__(self):
        self.dict_len = 0
        self.my_dict = {}
        self.my_sentence = ''

    def _get_len_dict(self) -> None:
        dict_input_len = int(input('Enter the len of a your dictionary: '))
        self.dict_len = dict_input_len

    def _get_words(self) -> None:
        counter = 0
        for number in range(self.dict_len):
            counter += 1
            word = input(f'Enter words {counter}: ')
            first_word = word.split(' ')[0]
            translation = word.split(' ')[1]
            self.my_dict[first_word] = translation

    def _get_sentence(self) -> None:
        result = input('Enter your sentences : ')
        self.my_sentence = result

    def _translate(self, word: str) -> str:
        new_word = self.my_dict.get(word)
        if new_word:
            return new_word
        else:
            return word

    def _process(self) -> None:
        for word in self.my_sentence.split(' '):  # first solution
            if self.my_dict.get(word):
                new_word = self.my_dict[word]
                self.my_sentence = self.my_sentence.replace(word, new_word)
        print(self.my_sentence)

        # print(" ".join(map(self._translate, self.my_sentence.split(' ')))) # second solution

        # def reduceFunction(initialValue, untranslatedWord):   # third solution
        #     initialValue += self._translate(untranslatedWord) + ' '
        #     return initialValue
        # print(reduce(reduceFunction, self.my_sentence.split(' '), ''))

    def __call__(self, *args, **kwargs):
        self._get_len_dict()
        self._get_words()
        self._get_sentence()
        self._process()


if __name__ == "__main__":
    translator = Translator()
    translator()
