import sys

import translators
from random import choice


PREAC = sys.argv[1] == "PREAC"
if PREAC:
    _ = translators.preaccelerate_and_speedtest()

class Translator:
    def translate(self, input_text: str) -> str:
        raise NotImplemented


class BadTranslator(Translator):

    def __init__(self, translations: int, end_lang="en"):
        self.translations = translations
        self.sequence = []

        for _ in range(self.translations - 1):
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
    def translate(self, input_text: str) -> str:
        return input_text[::-1]


class Sanitizer(Translator):
    def translate(self, input_text: str) -> str:
        text = input_text.replace("'", "''")
        return text


if __name__ == '__main__':
    #print(translators.translators_pool)
    translator = BadTranslator(3)
    print(translator.translate("Hallo wir geht es dir?"))
