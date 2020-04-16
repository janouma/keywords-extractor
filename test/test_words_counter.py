from unittest import TestCase, main
from pathlib import Path as get_path
from lib.words_counter import count_words

text_file_path = get_path(__file__).parent / 'assets/text_en.txt'


class TestWordsCounter(TestCase):

    @classmethod
    def setUpClass(cls):
        with open(text_file_path, 'r') as file:
            cls.test_suite_data = dict(text=file.read())

    def test_count_words(self):
        count = count_words(self.__class__.test_suite_data.get('text'))
        self.assertEqual(count, 3399)

    def test_count_words_trim_text(self):
        count = count_words(
            ' ' + self.__class__.test_suite_data.get('text') + ' ')
        self.assertEqual(count, 3399)


if __name__ == '__main__':
    main()
