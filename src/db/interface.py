from abc import abstractmethod

import sqlite3


class AbstractEngine:
    def __init__(self, database_name):
        self.database_name = database_name
        self.database = sqlite3.connect(f'{database_name}.db')
        self.cursor = self.database.cursor()


    @abstractmethod
    def create(self):
        ...


    @abstractmethod
    def read(self, query):
        ...


    @abstractmethod
    def update(self, id):
        ...


    @abstractmethod
    def delete(self, id):
        ...
