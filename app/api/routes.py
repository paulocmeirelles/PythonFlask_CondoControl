from flask import render_template, Blueprint, jsonify
from app.extensions import db
from json import dumps
from app.main.models.lote import Lote
from app.main.models.boleto import Boleto

bp = Blueprint('api', __name__)


@bp.route('/lotes')
def lotes():
    all_lotes = Lote.query.all()
    return render_template('index.html')
