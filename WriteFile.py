import os
from pathlib import Path


# noinspection SqlNoDataSourceInspection
class WriteSQL:
    def __init__(self, filename: str):
        self.filepath = Path(filename)
        self.writeSqlHeader()

    def writeSqlHeader(self):
        with open(self.filepath, 'w', encoding="utf-8") as f:
            f.write('INSERT OR REPLACE INTO LocalizedText (Language, Tag, Text) VALUES\n')
        self.first_Tuple = True

    def writeStatement(self, key: str, value: str) -> None:
        with open(self.filepath, 'a', encoding="utf-8") as f:
            if self.first_Tuple:
                f.write("\n")
                self.first_Tuple = False
            else:
                f.write(",\n")
            f.write(f"('en_US', '{key}', '{value}')")

    def finish(self):
        with open(self.filepath, 'a', encoding="utf-8") as f:
            f.write(f";")