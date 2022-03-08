import logging

import starkbank

from src.authentication import user

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

webhooks = starkbank.webhook.query()

for webhook in webhooks:
    logging.info(f'Consulting webhook...\n{webhook}')
