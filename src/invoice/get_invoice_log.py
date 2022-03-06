import logging
import starkbank

from src.authentication import user
from src.utils.constants import INVOICE_LOG

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

log = starkbank.invoice.log.get(INVOICE_LOG)

logging.info(f'Consulting an invoice...\n{log}')
