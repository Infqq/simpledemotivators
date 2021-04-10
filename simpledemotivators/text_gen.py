import random

class text_gen:
    def __init__(
            self, text) -> str:
        self._text = text

    def get_text(
            self, min_words=1, max_words=2
    ):
        split_text = self._text.split()

        result = ''

        for i in range(random.randint(min_words, max_words)):
            random_text = random.choice(split_text)
            result += random_text + ' '
            del split_text[split_text.index(random_text)]

        return result.lower()