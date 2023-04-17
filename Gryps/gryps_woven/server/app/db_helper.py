# Taken from https://docs.djangoproject.com/en/4.1/topics/db/sql/#executing-custom-sql-directly

from collections import namedtuple


def namedtuplefetchall(cursor, model):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple(model, [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def namedtuplefetchone(cursor, model):
    desc = cursor.description
    nt_result = namedtuple(model, [col[0] for col in desc])
    return nt_result(*cursor.fetchone())


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
