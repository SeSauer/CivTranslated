import sys

import translators
from random import choice

#good translators: modernMt

PREAC = sys.argv[1] == "PREAC"
if PREAC:
    _ = translators.preaccelerate_and_speedtest()

SEQUENCE_OVERRIDE = ["az", "th", "tr", "en"]

class Translator:
    def translate(self, input_text: str) -> str:
        raise NotImplemented


class BadTranslator(Translator):

    def __init__(self, translations: int, end_lang="en"):
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
    def translate(self, input_text: str) -> str:
        return input_text[::-1]


class Sanitizer(Translator):
    def translate(self, input_text: str) -> str:
        text = input_text.replace("'", "''")
        return text


if __name__ == '__main__':
    print(translators.get_languages("argos"))
    translator = BadTranslator(3)
    print(translator.translate("In the beginning, the earth was without form. And void. And then the sun shone upon the sleeping earth. Into this swirling maelstrom of fire air and water, the first stirrings of life appeared."))
