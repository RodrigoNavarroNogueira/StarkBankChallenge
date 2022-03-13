from abc import abstractmethod

import sqlite3


class AbstractEngine:
    def __init__(self, database_name):
        self.database_name = database_name
        self.database = sqlite3.connect(f'{database_name}.db')
        self.cursor = self.database.cursor()

        self.create()

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def read(self, query):
        pass

    @abstractmethod
    def delete(self, id):
        ...

    @abstractmethod
    def insert(self, query):
        pass
