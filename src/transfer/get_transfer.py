import logging

import starkbank

from src.authentication import user
from src.utils.constants import TRANSFER_ID

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

transfer = starkbank.transfer.get(TRANSFER_ID)

logging.info(f'Looking for transfer with ID Transfer number...\n{transfer}')
