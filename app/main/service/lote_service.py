from app.main.models.lote import Lote
from app.extensions import db


class Lotes():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def get():
        return Lote.query.all()

    def post(data):
        lote = Lote.query.filter_by(name=data['name']).first()
        if not lote:
            new_lote = Lote(name=data['name'])
            Lotes.save(new_lote)
            response_object = {
                'status': 'success',
                'message': 'Lote created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Lote already exist'
            }
            return response_object, 409

    def put(data):
        lote = Lote.query.filter_by(id=data['id']).first()
        if not lote:
            response_object = {
                'status': 'fail',
                'message': 'Lote doesnt exist'
            }
            return response_object, 409
        else:
            lote.name = data['name']
            lote.activate = data['activate']
            Lotes.save(lote)
            response_object = {
                'status': 'success',
                'message': 'Lote updated'
            }
            return response_object, 201


class LoteById():
    def delete(id):
        lote = Lote.query.filter_by(id=id).first()
        if not lote:
            response_object = {
                'status': 'fail',
                'message': 'Lote doesnt exist'
            }
            return response_object, 409
        else:
            lote.activate = False
            Lotes.save(lote)
            response_object = {
                'status': 'success',
                'message': 'Lote deleted'
            }
            return response_object, 201

    def get(id):
        return Lote.query.filter_by(id=id).first()
