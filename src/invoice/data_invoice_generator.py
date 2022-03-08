import random

from faker import Faker

fake = Faker()


def cpf():                                                                              
    n = [random.randrange(10) for i in range(9)]
    n.append(_calcula_digito(n))
    n.append(_calcula_digito(n))
    return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)


def _calcula_digito(digs):
    s = 0
    qtd = len(digs)
    for i in range(qtd):
        s += digs[i] * (1+qtd-i)
    res = 11 - s % 11
    if res >= 10: return 0
    return res


def random_name():
    return fake.name()


def random_amount():
    return random.randint(500, 300000)
