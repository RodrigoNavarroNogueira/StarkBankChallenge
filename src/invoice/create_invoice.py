from datetime import datetime, timedelta

import starkbank
import sqlite3

from src.authentication import user
from src.invoice.data_invoice_generator import random_amount, random_name, cpf

starkbank.user = user

base = sqlite3.connect('invoices.db')

cursor = base.cursor()


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
    cursor.execute(f"INSERT INTO invoices VALUES ('{invoices[0].status}', {invoices[0].id}, '{invoices[0].tax_id}', '{invoices[0].name}', {invoices[0].amount}, '{str(invoices[0].created)[:19]}')")
    base.commit()
    return invoices

create_invoice()
