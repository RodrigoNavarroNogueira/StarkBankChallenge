import logging

import starkbank

from src.authentication import user
from src.utils.constants import API_URL

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

webhook_invoice = starkbank.webhook.create(
    url=API_URL,
    subscriptions=[
        "invoice",
    ]
)

logging.info(f'Creating Webhook...\n{webhook_invoice}')
