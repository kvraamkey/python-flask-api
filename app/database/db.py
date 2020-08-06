from elasticsearch import Elasticsearch
from os import environ

def initialize_es(app):
    es = Elasticsearch(
        ['edb.edxi.io/es'],
        http_auth=('edxiuser', 'e3kcfVa3bSnC9c774v6UnSs8HeRtdS'),
        scheme="http",
        port=80,
    )
    return es
