from DatabaseAccess import CustomDatabaseAccess
from Translator import BadTranslator, Sanitizer, ReverseTranslator, Preprocessor
from WriteFile import WriteSQL

FORBIDDEN_TAGS = ["LOC_CREDITS", "LOC_EXPANSION1_CREDITS","LOC_EXPANSION2_CREDITS", "LOC_FRONTIER_CREDITS", "LOC_LEADERPASS_CREDITS"]

Database = CustomDatabaseAccess("Civ6Texts/Civ6Texts.sqlite", None)
translator = BadTranslator(3)
sanitizer = Sanitizer()
preproc = Preprocessor()
file_out = WriteSQL("Output/Complete3.sql")


i = 0

for (tag, text) in Database:
    if text is None: continue
    if tag in FORBIDDEN_TAGS: continue
    if i < 11031:
        i += 1
        continue
    translated = preproc.translate(text)
    translated = translator.translate(translated)
    translated = sanitizer.translate(translated)
    file_out.writeStatement(tag, translated)
    print(i)
    i += 1
    #if i > 100: break
file_out.finish()
