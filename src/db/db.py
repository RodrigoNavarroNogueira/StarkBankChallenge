import ast
import os


def insert_invoice(db_name, document):
    db_prefix = _get_db_prefix(db_name)

    if os.path.exists(db_name):
        with open(f'{db_name}.db', 'r') as doc:
            db_file = doc.read()
    else:
        create_database(db_name)
        db_file = db_prefix + ']}'
        
    db_file = db_file[len(db_prefix):-2]
    if db_file:
        db_file += ', '

    db_file += str(_insert_id(document))

    with open(f'{db_name}.db', 'w') as doc:
        doc.write(f"{db_prefix}{db_file}]"+'}')


def create_database(db_name):
    with open(f'{db_name}.db', 'w') as doc:
        doc.write(_get_db_prefix(db_name) + ']}')


def _get_db_prefix(db_name):
    return '{' + f"'{db_name}': ["


def list_invoices(db_name):
    if os.path.exists(f'{db_name}.db'):
        with open(f'{db_name}.db', 'r') as doc:
            documents = doc.read()
        return ast.literal_eval(documents)[db_name]
    else:
        create_database(db_name)
    return []


def get_invoice_id(document):
    try:
        return int(document['event']['log']['invoice']['id'])
    except:
        raise Exception('Invoice doesnt exists')


def _insert_id(document):
    document = ast.literal_eval(document)
    invoice_id = get_invoice_id(document)
    document['invoice_id'] = invoice_id
    return document


def delete_invoice(db_name, invoice_id):
    invoices = list_invoices(db_name)
    invoices_to_save = list()
    invoices_to_drop = list()

    for invoice in invoices:
        if invoice['invoice_id'] != invoice_id:
            invoices_to_save.append(invoice)
        else:
            invoices_to_drop.append(invoice)

    if invoices_to_drop:
        with open(f'{db_name}.db', 'w') as doc:
            doc.write(
                f'{_get_db_prefix(db_name)[:-1]}{str(invoices_to_save)}'+'}'
            )

        return invoices_to_drop[-1]
    else:
        raise Exception(f'Invalid invoice_id')


def select_invoice(db_name, invoice_id):
    invoices = list_invoices(db_name)

    for invoice in invoices:
        if invoice['invoice_id'] == invoice_id:
            return invoice


def _get_invoice_status(document):
    return document['event']['log']['invoice']['status']


def check_invoice_status(db_name, status):
    listed_invoices = list_invoices(db_name)
    invoices_with_status = set()

    for invoice in listed_invoices:
        if _get_invoice_status(invoice) == status:
            invoices_with_status.add(invoice['invoice_id'])
    
    return list(invoices_with_status)


def invoices_to_transfer(db_name, status='paid'):
    ids_to_drop = check_invoice_status(db_name, status)
    return [delete_invoice(db_name, id_to_drop) for id_to_drop in ids_to_drop]
