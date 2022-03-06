import logging

import starkbank

from src.authentication import user
from src.utils.constants import INVOICE_ID

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

invoice = starkbank.invoice.get(INVOICE_ID)

logging.info(f'Consulting the invoice...\n{invoice}')
