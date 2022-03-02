def discount(document):
    return int(document['event']['log']['invoice']['amount'] - (document['event']['log']['invoice']['amount'] * 10 / 100))
 