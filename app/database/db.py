from elasticsearch import Elasticsearch


def initialize_es():
    es = Elasticsearch(
        ['edb.edxi.io/es'],
        http_auth=('edxiuser', 'e3kcfVa3bSnC9c774v6UnSs8HeRtdS'),
        scheme="http",
        port=80,
    )
    return es
