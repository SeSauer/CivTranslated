import sys
import re

import translators
from random import choice

#good translators: modernMt
#good langs: ['so', 'ydd', 'ht', 'en']

if sys.argv.__len__() > 1:
    PREAC = sys.argv[1] == "PREAC"
else:
    PREAC = False
if PREAC:
    _ = translators.preaccelerate_and_speedtest()

SEQUENCE_OVERRIDE = []
"""Use Sequence Override to force a specific sequence of Languages. If the List is empty, a random sequence will be generated"""

class Translator:
    def translate(self, input_text: str) -> str:
        raise NotImplemented


class BadTranslator(Translator):
    """Translates input text throug multiple Languages"""

    def __init__(self, translations: int, end_lang="en"):
        """Translates input text throug multiple Languages
        :param translations: Number of total translations for each input text
        :param end_lang: the desired language for the final output"""
        self.translations = translations
        self.sequence = []
        if SEQUENCE_OVERRIDE:
            self.sequence = SEQUENCE_OVERRIDE
        else:
            for x in range(self.translations - 1):
                self.sequence.append(choice(list(translators.get_languages("modernMt"))))
            self.sequence.append(end_lang)
        print(self.sequence)

    def translate(self, input_text: str) -> str:
        text = input_text
        last_lang = "en"
        for lang in self.sequence:
            text = translators.translate_text(query_text=text, from_language=last_lang, to_language=lang, translator="modernMt", if_use_preacceleration=PREAC)
            last_lang = lang
            #print(text)
        return text


class ReverseTranslator(Translator):
    """Translator used for testing; Inverts any input text"""
    def translate(self, input_text: str) -> str:
        return input_text[::-1]


class Preprocessor(Translator):
    """Should be run on any text before translation"""
    def translate(self, input_text: str) -> str:
        return re.sub("\{.*?\}", "", input_text)


class Postprocessor(Translator):
    """Should be run on any text after translation for SQL escaping"""
    def translate(self, input_text: str) -> str:
        text = input_text.replace("'", "''")
        return text
