import logging
from datetime import datetime

import starkbank

from src.authentication import user

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

logs = starkbank.invoice.log.query(
    after="2020-01-01",
    before=datetime.now(),
    limit=10
)

for log in logs:
    logging.info(f'Consulting invoice\n{log}')
