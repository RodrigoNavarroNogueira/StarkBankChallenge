from datetime import datetime

import starkbank

from src.authentication import user

starkbank.user = user

logs = starkbank.transfer.log.query(
    after="2019-01-01",
    before=datetime.now()
)

for log in logs:
    print(log)
