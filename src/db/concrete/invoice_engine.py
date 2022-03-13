from src.db.interface import AbstractEngine
from src.utils.raises import EmptyQueryError


class InvoiceEngine(AbstractEngine):
    def __init__(self):
        super().__init__('starkbank')
        self.columns = [
            'status',
            'invoice_id',
            'cpf',
            'name',
            'amount',
            'created',
        ]
    
    def read(self, query):
        result = self.cursor.execute(query)
        result = result.fetchall()
        return result
    
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

    def _check_if_table_not_exists(self):
        query = 'SELECT name FROM sqlite_master WHERE type="table";'
        check_if_exists = self.read(query)

        if len(check_if_exists):
            if 'invoice' in check_if_exists[0]:
                return False
        return True

    def list_invoices(self):
        return self.read('SELECT * FROM invoice')
    
    def get_invoice(self, invoice_id):
        query = f'SELECT * FROM invoice WHERE id = {invoice_id}'
        try:
            return self.read(query)[0]
        except IndexError:
            raise EmptyQueryError('Invalid invoice_id.')

    def get_paid_invoices_id(self):
        invoices = self.list_invoices()
        captured_invoices = set()

        for invoice in invoices:
            if invoice[1] == 'paid':
                captured_invoices.add(invoice[0])
        return list(captured_invoices)

    def invoices_to_transfer(self):
        paid_invoices_id = self.get_paid_invoices_id()
        return [self.delete(invoice_id) for invoice_id in paid_invoices_id]
