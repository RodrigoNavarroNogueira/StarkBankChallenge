import starkbank

from src.authentication import user

starkbank.user = user

transfer = starkbank.transfer.get("4659866144604160")

print(transfer)
