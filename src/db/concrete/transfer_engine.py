from src.db.interface import AbstractEngine


class TransferEngine(AbstractEngine):
    def __init__(self):
        super().__init__('starkbank')

    def create(self):
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


    def read(self, query):
        result = self.cursor.execute(query)
        result = result.fetchall()
        return result


    def update(self, transfer_id):
        query = f"UPDATE transfer SET status = 'success' WHERE id = {transfer_id}"
        self.cursor.execute(query)
        self.database.commit()


    def insert(self, transfer_id, status, amount, created_at, scheduled):
        query = f'''
            INSERT INTO transfer VALUES(
                {transfer_id},
                '{status}',
                {amount},
                '{created_at}',
                '{scheduled}'
            )
        '''
        self.cursor.execute(query)
        self.database.commit()


    def delete(self, transfer_id):
        query = f'''
            DELETE FROM transfer
            WHERE id = {transfer_id}
        '''
        self.cursor.execute(query)
        self.database.commit()
        return transfer_id


    def _check_if_table_not_exists(self):
        query = 'SELECT name FROM sqlite_master WHERE type="table";'
        check_if_exists = self.read(query)

        if len(check_if_exists):
            if 'invoice' in check_if_exists[0]:
                return False
        return True

    def drop_table(self):
        query = 'DROP TABLE transfer;'
        self.cursor.execute(query)
        self.database.commit()
