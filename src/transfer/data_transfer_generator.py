import random

import starkbank

from src.authentication import user

starkbank.user = user


def create_external_id():
    for num in range(15):
        print(random.randrange(10), end="")
