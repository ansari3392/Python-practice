import unittest
from unittest.mock import patch
from practice4 import Translator

def get_words():
    return ['hello salam', 'how chetory', 'are hasti', 'you shoma']

def get_inputs():
    return [
        '2',
        'I man',
        'am hastam',
        'I am fatemeh',

    ]



class TranslatorTest(unittest.TestCase):

    @patch('builtins.input')
    def test_get_my_dict_len(self, mock_input):
        mock_input.return_value = '4'
        translator = Translator()
        self.assertEqual(translator.dict_len, 0)
        translator._get_len_dict()
        self.assertEqual(translator.dict_len, 4)

    @patch('builtins.input', side_effect=get_words())
    def test_get_my_dict(self, mock_input):
        translator = Translator()
        translator.dict_len = 3
        self.assertEqual(len(translator.my_dict), 0)
        translator._get_words()
        self.assertEqual(len(translator.my_dict), 3)

    @patch('builtins.input')
    def test_get_sentence(self, mock_input):
        mock_input.return_value = 'hello how are you'
        translator = Translator()
        self.assertEqual(translator.my_sentence, '')
        translator._get_sentence()
        self.assertEqual(translator.my_sentence, 'hello how are you')

    @patch('builtins.input')
    def test_translate(self, mock_input):
        mock_input.return_value = 'hello how are you'
        translator = Translator()
        self.assertEqual(translator.my_sentence, '')
        translator._get_sentence()
        self.assertEqual(translator.my_sentence, 'hello how are you')


    def test_process(self):
        translator = Translator()
        translator.my_dict = {'hello': 'salam', 'how':'chetor', 'are':'hasti', 'you':'shoma'}
        translator.my_sentence = 'hello how are you ?'
        self.assertEqual(translator.my_sentence, 'hello how are you ?')
        translator._process()
        self.assertEqual(translator.my_sentence, 'salam chetor hasti shoma ?')

    @patch('builtins.input', side_effect=get_inputs())
    def test_call(self, mock_input):
        translator = Translator()
        self.assertEqual(translator.dict_len, 0)
        self.assertEqual(translator.my_dict, {})
        self.assertEqual(translator.my_sentence, '')
        translator._get_len_dict()
        translator._get_words()
        translator._get_sentence()
        translator._process()
        self.assertEqual(translator.dict_len, 2)
        self.assertEqual(translator.my_dict, {'I':'man', 'am':'hastam'})
        self.assertEqual(translator.my_sentence, 'man hastam fatemeh')



if __name__ == '__main__':
    unittest.main()
