from src.db.interface import AbstractEngine
import random

class TransferEngine(AbstractEngine):
    def __init__(self):
        super().__init__('starkbank')


    def create(self, transfer_id, status, amount, created_at, scheduled):
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


    def read(self, query):
        result = self.cursor.execute(query)
        result = result.fetchall()
        return result


    def update(self, transfer_id):
        query = f"UPDATE transfer SET status = 'success' WHERE id = {transfer_id}"
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
