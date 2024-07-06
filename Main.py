from DatabaseAccess import CustomDatabaseAccess
from Translator import BadTranslator, Postprocessor, Preprocessor
from WriteFile import WriteSQL

FORBIDDEN_TAGS = ["LOC_CREDITS", "LOC_EXPANSION1_CREDITS","LOC_EXPANSION2_CREDITS", "LOC_FRONTIER_CREDITS", "LOC_LEADERPASS_CREDITS"]
"""Tags that will not be translated"""

#initialize
database = CustomDatabaseAccess("Civ6Texts/Civ6Texts.sqlite", None)
postproc = Postprocessor()
preproc = Preprocessor()
output_file = WriteSQL("Output/Translated.sql")

#change this to do different translations
translator = BadTranslator(5)

i = 0
for (tag, text) in database:
    if text is None: continue
    if tag in FORBIDDEN_TAGS: continue
    translated = preproc.translate(text)
    translated = translator.translate(translated)
    translated = postproc.translate(translated)
    output_file.writeStatement(tag, translated)
    print(i)
    i += 1
output_file.finish()
