from datetime import datetime

import starkbank

from src.authentication import user

starkbank.user = user

transfers = starkbank.transfer.query(
    after="2020-04-01",
    before=datetime.now()
)

for transfer in transfers:
    print(transfer)
