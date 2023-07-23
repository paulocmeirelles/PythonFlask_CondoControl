from datetime import datetime
from app.extensions import db


class Boleto(db.Model):
    __tablename__ = 'boleto'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    lote_id = db.Column(db.String(4), nullable=False)
    month_reference = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float(precision=2), nullable=True)
    bar_code = db.Column(db.String(100), nullable=True)
    activate = db.Column(db.Boolean, nullable=True, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# db.drop_all()
# db.create_all()


# class BoletoSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "name", "id_lote", "value",
#                   "bar_code", "activate", "created_at")


# lote_schema = BoletoSchema()
# lotes_schema = BoletoSchema(many=True)
