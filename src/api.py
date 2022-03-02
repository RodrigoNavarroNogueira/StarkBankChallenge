from flask import Flask, request, Response

from src.utils.constants import DB_NAME
from src.db.db import insert_invoice

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        response = request.get_json()
        response = str(response)
        insert_invoice(DB_NAME, response)
        return Response('OK', status=200)
        

app.run()
