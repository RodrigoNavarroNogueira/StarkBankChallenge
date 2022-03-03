import logging
from datetime import timedelta, datetime

from src.db.db import invoices_to_transfer, insert_invoice
from src.transfer.transfer import do_transfer
from src.utils.constants import TRANSFER_DB


def scheduler(function_structure, time_measure='minutes', unit_time=1, function_params=None):
    add_delay = timedelta(**{time_measure: unit_time})
    next_schedule = datetime.now()

    while True:
        if next_schedule <= datetime.now():
            logging.info('Waiting for confirmation of payments...')
            next_schedule = datetime.now() + add_delay
            function_structure(**function_params)


def transfer_schedule(db_name, status):
    to_transfer = invoices_to_transfer(db_name, status)

    for invoice in to_transfer:
        logging.info(
            f'''Transfer performed successfully!
        Transfer info: {do_transfer(invoice)}
        Transferred at {datetime.now()}'''
        )
        insert_invoice(TRANSFER_DB, str(invoice))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
