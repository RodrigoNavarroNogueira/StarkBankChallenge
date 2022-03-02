# StarkBankChallenge
A system that issues invoices to random people and sends the received amount to the stark bank account using an automatic transfer


## Requirements:
- Python 3.10.2


## How to start
Clone the repository
```sh
git clone git@github.com:RodrigoNavarroNogueira/StarkBankChallenge.git
```

Update the remote
```sh
git remote set-url origin git@github.com:RodrigoNavarroNogueira/StarkBankChallenge.git
```


Into a virtualenv install the dependencies:
```sh
pip install -r requirements/dev.txt
```

Create the .env based on .env.sample:
```sh
cp contrib/.env.sample .env
```

Run:
```sh
(Start the api)

python -m src.api

(Start the transfer scheduler)

python -m src.scheduler_transfer

(Start the invoice issuer)

python -m src.scheduler_invoice
```
