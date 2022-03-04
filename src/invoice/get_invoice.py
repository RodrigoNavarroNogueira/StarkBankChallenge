import starkbank

from src.authentication import user
from src.utils.constants import INVOICE_ID

starkbank.user = user

id_invoice = INVOICE_ID
invoice = starkbank.invoice.get(id_invoice)

print(invoice)
