from src.db.interface import AbstractEngine


class InvoiceEngine(AbstractEngine):
    def __init__(self):
        super().__init__('starkbank')


    def create(self):
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


    def read(self, query):
        result = self.cursor.execute(query)
        result = result.fetchall()
        return result


    def update(self, invoice_id):
        query = f"UPDATE invoice SET status = 'paid' WHERE id = {invoice_id}"
        self.cursor.execute(query)
        self.database.commit()


    def insert(self, invoice_id, status, tax_id, name, amount, created_at):
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


    def delete(self, invoice_id):
        query = f'''
            DELETE FROM invoice
            WHERE id = {invoice_id}
        '''
        self.cursor.execute(query)
        self.database.commit()
        return invoice_id


    def _check_if_table_not_exists(self):
        query = 'SELECT name FROM sqlite_master WHERE type="table";'
        check_if_exists = self.read(query)

        if len(check_if_exists):
            if 'invoice' in check_if_exists[0]:
                return False
        return True
