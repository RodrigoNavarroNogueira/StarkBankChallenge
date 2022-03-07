import random

import starkbank

from src.authentication import user

starkbank.user = user

lis = []


def create_external_id():
    for num in range(15):
        id = str(random.randrange(10))
        lis.append(id)
    num = ""
    external_id = num.join(lis) 
    return external_id
