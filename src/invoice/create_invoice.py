from datetime import datetime, timedelta

import starkbank

from src.authentication import user
from src.invoice.data_invoice_generator import random_amount, random_name, cpf


def create_invoice():
    invoices = starkbank.invoice.create([
        starkbank.Invoice(
            amount=random_amount(),
            descriptions=[{'key': 'Arya', 'value': 'Not today'}],
            discounts=[{'percentage': 10, 'due': datetime.now()+timedelta(days=10)}],
            due=datetime.now()+timedelta(days=10),
            expiration=123456789,
            fine=2.5,
            interest=1.3,
            name=random_name(),
            tags=['New sword', 'Invoice #1234'],
            tax_id=cpf()
        )
    ])
    return invoices


starkbank.user = user
