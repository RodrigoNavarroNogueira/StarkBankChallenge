import random

import starkbank

from src.authentication import user


def create_external_id():
    starkbank.user = user
    random_list = []

    for num in range(15):
        id = str(random.randrange(10))
        random_list.append(id)
    num = ''
    external_id = num.join(random_list) 
    
    return external_id
