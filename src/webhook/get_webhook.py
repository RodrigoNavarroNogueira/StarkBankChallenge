import starkbank

from src.authentication import user
from src.utils.constants import WEBHOOK_ID

starkbank.user = user

webhook = starkbank.webhook.get(WEBHOOK_ID)

print(webhook)