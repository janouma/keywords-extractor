from unittest import TestCase, main
from pathlib import Path as get_path
from lib.keywords_extractor import KeywordsExtractor

text_src_dir = get_path(__file__).parent / 'assets'


class TestKeywordsExtractor(TestCase):

    def test_extract_english_keywords(self):
        with open(text_src_dir / 'text_en.txt', 'r') as file:
            text = file.read()

        extractor = KeywordsExtractor('en')

        extractor.analyze(
            text,
            candidate_pos=['NOUN', 'PROPN', 'VERB'],
            window_size=4,
            lower=True
        )

        self.assertEqual(extractor.get_keywords(
            percent=5, max_keywords=20),
            ['npm',
             'command',
             'tasks',
             'post',
             'task',
             'windows',
             'tools',
             'run',
             'use',
             'commands',
             'grunt',
             'gulp',
             'file',
             'files',
             'example',
             'running',
             'output',
             'build',
             'scripts',
             'package']
        )

    def test_extract_clean_keywords(self):
        with open(text_src_dir / 'text_alt_en.txt', 'r') as file:
            text = file.read()

        extractor = KeywordsExtractor('en')

        extractor.analyze(
            text,
            candidate_pos=['NOUN', 'PROPN', 'VERB'],
            window_size=4,
            lower=True
        )

        self.assertEqual(extractor.get_keywords(
            percent=5, max_keywords=20),
            ['npm',
             'run',
             'scripts',
             'build',
             'command',
             'test',
             'tasks',
             'package',
             'commands',
             'tools',
             'set',
             'task',
             'windows',
             'post',
             'use',
             'output',
             'grunt',
             'config',
             'css',
             'running']
        )


if __name__ == '__main__':
    main()
