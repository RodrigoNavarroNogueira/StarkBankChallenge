from datetime import datetime

import starkbank

from src.authentication import user

starkbank.user = user

boletos = starkbank.boleto.create([
    starkbank.Boleto(
        amount=10000000,
        due=datetime.now(),
        name="Iron Bank S.A.",
        tax_id="20.018.183/0001-80",
        fine=2.5,
        interest=1.3,
        overdue_limit=5,
        street_line_1="Av. Faria Lima, 1844",
        street_line_2="CJ 13",
        district="Itaim Bibi",
        city="São Paulo",
        state_code="SP",
        zip_code="01500-000",
        tags=["War supply", "Invoice #1234"]
    )
])

for boleto in boletos:
    print(boleto)
