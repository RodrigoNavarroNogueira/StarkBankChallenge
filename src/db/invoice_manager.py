from src.db.concrete.invoice_engine import InvoiceEngine
from src.utils.raises import EmptyQueryError


class InvoiceManager():
    def __init__(self):
        self.engine = InvoiceEngine()


    def list_invoices(self):
        return self.engine.read('SELECT * FROM invoice')
    

    def get_invoice(self, invoice_id):
        query = f'SELECT * FROM invoice WHERE id = {invoice_id}'
        try:
            return self.engine.read(query)[0]
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
        return [self.engine.delete(invoice_id) for invoice_id in paid_invoices_id]
