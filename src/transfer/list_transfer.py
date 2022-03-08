import logging
from datetime import datetime

import starkbank

from src.authentication import user

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

transfers = starkbank.transfer.query(
    after="2022-03-07",
    before=datetime.now()
)

for transfer in transfers:
    logging.info(f'Consulting transfers...\n{transfer}')
