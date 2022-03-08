import logging
from datetime import datetime

import starkbank

from src.authentication import user

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

logs = starkbank.transfer.log.query(
    after="2022-03-07",
    before=datetime.now()
)

for log in logs:
    logging.info(f'Consulting transfer...\n{log}')
