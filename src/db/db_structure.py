from src.db.interface import AbstractEngine


class DatabaseStructure(AbstractEngine):
    def __init__(self):
        super().__init__('starkbank')


    def create_table_invoice(self):
        if self._check_if_table_not_exists():
            self.cursor.execute(
                '''
                CREATE TABLE invoice(
                    id INT PRIMARY KEY,
                    cpf CHAR(14),
                    status VARCHAR,
                    name VARCHAR,
                    amount INT,
                    created DATETIME
                )
                '''
            )
            self.database.commit()


    def create_table_transfer(self):
        if self._check_if_table_not_exists():
            self.cursor.execute(
                '''
                CREATE TABLE transfer(
                    id INT PRIMARY KEY,
                    status VARCHAR,
                    amount INT,
                    created DATETIME,
                    scheduled DATETIME
                )
                '''
            )
            self.database.commit()


    def _check_if_table_not_exists(self):
        query = 'SELECT name FROM sqlite_master WHERE type="table";'
        check_if_exists = self.read(query)

        if len(check_if_exists):
            if 'invoice' in check_if_exists[0]:
                return False
        return True


    def drop_table_invoice(self):
        query = 'DROP TABLE invoice;'
        self.cursor.execute(query)
        self.database.commit()


    def drop_table_transfer(self):
        query = 'DROP TABLE transfer;'
        self.cursor.execute(query)
        self.database.commit()
