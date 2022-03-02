import starkbank

from src.authentication import user

starkbank.user = user

log = starkbank.invoice.log.get("5284510723735552")

print(log)
