import os
from pathlib import Path


# noinspection SqlNoDataSourceInspection
class WriteSQL:
    def __init__(self, filename: str):
        """"Used to write translations to a SQL file to be used in a mod"""
        self.filepath = Path(filename)
        self.writeSqlHeader()

    def writeSqlHeader(self):
        with open(self.filepath, 'w', encoding="utf-8") as f:
            f.write('INSERT OR REPLACE INTO LocalizedText (Language, Tag, Text) VALUES\n')
        self.first_Tuple = True

    def writeStatement(self, key: str, value: str) -> None:
        """Used to write translations to the file.
        :param key: the key used to identify text, usually in the form 'LOC_FOO_BAR'
        :param value: the translated text"""
        with open(self.filepath, 'a', encoding="utf-8") as f:
            if self.first_Tuple:
                f.write("\n")
                self.first_Tuple = False
            else:
                f.write(",\n")
            f.write(f"('en_US', '{key}', '{value}')")

    def finish(self):
        """Should be run after writing all statements to the filt to complete sql syntax"""
        with open(self.filepath, 'a', encoding="utf-8") as f:
            f.write(f";")