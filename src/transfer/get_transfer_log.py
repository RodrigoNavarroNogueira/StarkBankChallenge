import starkbank

from src.authentication import user

starkbank.user = user

log = starkbank.transfer.log.get("4571465684877312")

print(log)
