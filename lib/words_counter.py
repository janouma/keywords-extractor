import logging
import re

special_chars_pattern = re.compile(r'\W+')
spaces_pattern = re.compile(r'\s+')

logger = logging.getLogger(__name__)


def count_words(text):
    special_chars_free_text = special_chars_pattern.sub(' ', text)
    words = spaces_pattern.split(special_chars_free_text.strip())

    logger.debug('words:\n %s', '\n'.join(words))

    return len(words)
