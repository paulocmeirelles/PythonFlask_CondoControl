from app.main.models.boleto import Boleto
from app.extensions import db


class Boletos():

    def save(data):
        db.session.add(data)
        db.session.commit()

    def get():
        return Boleto.query.all()

    def post(data):
        boleto = Boleto.query.filter_by(
            month_reference=data['month_reference'], lote_id=data['lote_id']).first()
        if not boleto:
            new_boleto = Boleto(
                name=data['name'], lote_id=data['lote_id'],
                month_reference=data['month_reference'],
                value=data['value'], bar_code=data['bar_code'])
            Boletos.save(new_boleto)
            response_object = {
                'status': 'success',
                'message': 'Boleto created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Boleto already exist'
            }
            return response_object, 409

    def put(data):
        boleto = Boleto.query.filter_by(id=data['id']).first()
        if not boleto:
            response_object = {
                'status': 'fail',
                'message': 'Boleto doesnt exist'
            }
            return response_object, 409
        else:
            boleto.name = data['name']
            boleto.value = data['value']
            boleto.lote_id = data['lote_id']
            boleto.bar_code = data['bar_code']
            boleto.activate = data['activate']
            Boletos.save(boleto)
            response_object = {
                'status': 'success',
                'message': 'Boleto updated'
            }
            return response_object, 201


class BoletoById():
    def delete(id):
        boleto = Boleto.query.filter_by(id=id).first()
        if not boleto:
            response_object = {
                'status': 'fail',
                'message': 'Boleto doesnt exist'
            }
            return response_object, 409
        else:
            boleto.activate = False
            Boletos.save(boleto)
            response_object = {
                'status': 'success',
                'message': 'Boleto deleted'
            }
            return response_object, 201

    def get(id):
        return Boleto.query.filter_by(id=id).first()
