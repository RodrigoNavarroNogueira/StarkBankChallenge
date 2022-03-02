from src.document import discount
from src.transfer.create_transfer import transfer


def do_transfer(document):
    amount = discount(document)
    return transfer(amount)
