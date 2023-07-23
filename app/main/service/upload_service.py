from app.extensions import db

from ..models.boleto import Boleto
from ..models.lote import Lote


class Lotes():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def bulk_create(data):
        db.session.add_all([Lote(name=row['name']) for row in data])
        # for row in data:
        #     db.add(Lote(name=row['name']))
        db.session.commit()


class Boletos():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def bulk_create(data):
        db.session.add_all([Boleto(name=row['name'], value=row['value'],
                                   lote_id=row['lote_id'], bar_code=row['bar_code']) for row in data])
        # for row in data:
        #     db.session.add(
        #         Boleto(name=row['name'], value=row['value'], lote_id=row['lote_id'],
        #                bar_code=row['bar_code']))
        db.session.commit()
