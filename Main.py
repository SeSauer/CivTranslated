from DatabaseAccess import CustomDatabaseAccess
from Translator import BadTranslator, Sanitizer, ReverseTranslator
from WriteFile import WriteSQL

FORBIDDEN_TAGS = ["LOC_CREDITS", "LOC_EXPANSION1_CREDITS","LOC_EXPANSION2_CREDITS", "LOC_FRONTIER_CREDITS", "LOC_LEADERPASS_CREDITS"]

Database = CustomDatabaseAccess("Civ6Texts/Civ6Texts.sqlite", "Expansion2")
translator = BadTranslator(3)
sanitizer = Sanitizer()
file_out = WriteSQL("Output/Expansion2.sql")


i = 0

for (tag, text) in Database:
    if text is None: continue
    if tag in FORBIDDEN_TAGS: continue
    translated = translator.translate(text)
    translated = sanitizer.translate(translated)
    file_out.writeStatement(tag, translated)
    print(i)
    i += 1
    #if i > 100: break
file_out.finish()
