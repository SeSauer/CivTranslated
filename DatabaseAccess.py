from pathlib import Path
import sqlite3


class BaseDatabaseAccess:
    pass


class DebugDatabaseAccess(BaseDatabaseAccess):
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
    def __init__(self, filepath: str, filter: str):
        self.filepath = Path(filepath)
        self.connection = sqlite3.connect(self.filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f'SELECT Tag, en_US FROM LocalizedText WHERE DLC = "{filter}"')

    def __iter__(self):
        return self

    def __next__(self):
        entry = self.cursor.fetchone()
        if entry is None:
            raise StopIteration
        return entry