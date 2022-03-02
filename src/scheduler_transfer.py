import logging

from src.transfer.scheduler import scheduler, transfer_schedule
from src.utils.constants import STATUS, INVOICE_DB


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    function_params = {
        'db_name': INVOICE_DB,
        'status': STATUS
    }
    logging.info('Started a transfer schedule')
    scheduler(transfer_schedule, 'seconds', 5, function_params=function_params)
