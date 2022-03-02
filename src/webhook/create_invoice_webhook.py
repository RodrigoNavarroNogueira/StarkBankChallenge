import starkbank

from src.authentication import user
from src.utils.constants import API_URL

starkbank.user = user

webhook_invoice = starkbank.webhook.create(
    url=API_URL,
    subscriptions=[
        "invoice",
    ]
)

print(webhook_invoice)
