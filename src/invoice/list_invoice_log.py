from datetime import datetime

import starkbank

from src.authentication import user

starkbank.user = user

logs = starkbank.invoice.log.query(
    after="2020-01-01",
    before=datetime.now(),
    limit=10
)

for log in logs:
    print(log)
