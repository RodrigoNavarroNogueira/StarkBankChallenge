from datetime import datetime, timedelta
from time import sleep, time
from random import randint
from invoice.create_invoice import create_invoice
import logging


def __get_initial_and_limit_time():
    now = datetime.now()
    return now, now + timedelta(hours=3)


def __roll_invoice_quantity_per_period():
    return randint(8, 12)


def __create_random_time_per_period(min_time, max_time):
    min_timestamp = int(datetime.timestamp(min_time))
    max_timestamp = int(datetime.timestamp(max_time)) - 5   
    random_timestamp = randint(min_timestamp, max_timestamp)
    return random_timestamp


def __create_invoice_time_moments(time_range):
    invoice_qty = __roll_invoice_quantity_per_period()
    moments = [
        __create_random_time_per_period(*time_range)
        for _ in range(invoice_qty) 
    ]
    moments.sort()
    return moments


def __create_invoice(moment):
    create_invoice()
    logging.info(
        f'Invoice {datetime.fromtimestamp(moment)} created at {datetime.now()}'
    )


def run_a_schedule():
    time_range = __get_initial_and_limit_time()
    moments = __create_invoice_time_moments(time_range)

    while datetime.now() <= time_range[1]:
        if moments[-1] > int(time()):
            for moment in moments:
                while int(time()) < moment:
                    logging.info(
                        f'Waiting next invoice...'
                    )
                    sleep(1)

                __create_invoice(moment)
                sleep(1)
                    
        else:
            logging.info('All invoices already issued! Waiting the next schedule')
            sleep(1)


def scheduler():
    end = datetime.now() + timedelta(hours=24)
    logging.info('Started invoice scheduler')

    while datetime.now() < end:
        logging.info('Started new cycle')
        run_a_schedule()
    
    logging.info('End')


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    scheduler()
