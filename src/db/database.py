import sqlite3

base = sqlite3.connect('invoices.db')

cursor = base.cursor()

cursor.execute("CREATE TABLE invoices (STATUS VARCHAR, INVOICE_ID INT, CPF CHAR(14), NAME VARCHAR, AMOUNT INT, CREATED DATETIME, PRIMARY KEY (INVOICE_ID, CPF))")

base.commit()
