from datetime import datetime
from app.extensions import db


class Lote(db.Model):
    __tablename__ = 'lote'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    activate = db.Column(db.Boolean, nullable=True, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# from flask_marshmallow import Marshmallow
# db.drop_all()
# db.create_all()

# CREATE FIRST ROWS
# lotes = [
#     Lote(name='0011'),
#     Lote(name='0015'),
#     Lote(name='0017'),
#     Lote(name='0012'),
#     Lote(name='0013'),
#     Lote(name='0018'),
#     Lote(name='0019'),
#     Lote(name='0014')
# ]

# db.session.bulk_save_objects(lotes)
# db.session.commit()


# class LoteSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "name", "activate", "created_at")


# lote_schema = LoteSchema()
# lotes_schema = LoteSchema(many=True)
