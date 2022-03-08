import logging

import starkbank

from src.authentication import user
from src.utils.constants import WEBHOOK_ID

starkbank.user = user

logging.getLogger().setLevel(logging.INFO)

webhook = starkbank.webhook.delete(WEBHOOK_ID)

logging.info(f'Deleting Webhook...\n{webhook}')
