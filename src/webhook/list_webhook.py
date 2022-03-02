import starkbank

from src.authentication import user

starkbank.user = user

webhooks = starkbank.webhook.query()

for webhook in webhooks:
    print(webhook)