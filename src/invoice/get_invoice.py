import starkbank

from src.authentication import user

starkbank.user = user

id_invoice = '4659866144604160'
invoice = starkbank.invoice.get(id_invoice)

print(invoice)
