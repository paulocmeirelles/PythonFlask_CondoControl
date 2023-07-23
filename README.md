# flask_api

rodar flask shell
from app.extensions import db
db.create_all()
lotes = [
Lote(name='0011'),
Lote(name='0015'),
Lote(name='0017'),
Lote(name='0012'),
Lote(name='0013'),
Lote(name='0018'),
Lote(name='0019'),
Lote(name='0014')
]

db.session.bulk_save_objects(lotes)
db.session.commit()
