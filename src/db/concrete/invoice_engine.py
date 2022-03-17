from src.db.interface import AbstractEngine
import random

class InvoiceEngine(AbstractEngine):
    def __init__(self):
        super().__init__('starkbank')


    def create(self, invoice_id, status, tax_id, name, amount, created_at):
        query = f'''
            INSERT INTO invoice VALUES(
                {invoice_id},
                '{status}',
                '{tax_id}',
                '{name}',
                {amount},
                '{created_at}'
            )
        '''
        self.cursor.execute(query)
        self.database.commit()


    def read(self, query):
        result = self.cursor.execute(query)
        result = result.fetchall()
        return result


    def update(self, invoice_id):
        query = f"UPDATE invoice SET status = 'paid' WHERE id = {invoice_id}"
        self.cursor.execute(query)
        self.database.commit()


    def delete(self, invoice_id):
        query = f'''
            DELETE FROM invoice
            WHERE id = {invoice_id}
        '''
        self.cursor.execute(query)
        self.database.commit()
        return invoice_id
