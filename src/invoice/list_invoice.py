from datetime import datetime

import starkbank

from src.authentication import user

starkbank.user = user

invoices = starkbank.invoice.query(
    after="2020-10-18",
    before=datetime.now(),
    limit=10,
)

for invoice in invoices:
    print(invoice)
