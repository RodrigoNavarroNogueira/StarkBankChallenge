import logging

import starkbank

from src.authentication import user
from src.utils.constants import TRANSFER_LOG

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

log = starkbank.transfer.log.get(TRANSFER_LOG)

logging.info(f'Looking for transfer with log number...\n{log}')
