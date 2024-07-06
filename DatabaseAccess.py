from pathlib import Path
import sqlite3


class BaseDatabaseAccess:
    pass


class DebugDatabaseAccess(BaseDatabaseAccess):
    """Iteratable class for reading entries from Civs Chached DebugLocalization.sqlite database (Does not include DLCs)"""
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.connection = sqlite3.connect(self.filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT Tag, Text FROM LocalizedText WHERE Language = "en_US"')

    def __iter__(self):
        return self

    def __next__(self):
        entry = self.cursor.fetchone()
        if entry is None:
            raise StopIteration
        return entry


class CustomDatabaseAccess(BaseDatabaseAccess):
    """Iteratable class for reading entries from The Complete Database provided via
    https://forums.civfanatics.com/resources/civ6-debuglocalization-sqlite-database-with-all-expansions-and-dlcs-texts.28236/
    (see Civ6Texts/Download.txt for Download link)
    Contains all texts, including DLC
    :param filter: Use to only return entries from a specific expamsion eg: 'Base' 'Expansion2' 'Babylon'"""
    def __init__(self, filepath: str, filter: str | None):
        self.filepath = Path(filepath)
        self.connection = sqlite3.connect(self.filepath)
        self.cursor = self.connection.cursor()
        if filter is not None:
            self.cursor.execute(f'SELECT Tag, en_US FROM LocalizedText WHERE DLC = "{filter}"')
        else:
            self.cursor.execute(f'SELECT Tag, en_US FROM LocalizedText')

    def __iter__(self):
        return self

    def __next__(self):
        entry = self.cursor.fetchone()
        if entry is None:
            raise StopIteration
        return entry