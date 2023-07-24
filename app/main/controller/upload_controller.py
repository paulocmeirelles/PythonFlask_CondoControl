from ..service import upload_service
from flask import request
from flask_restx import Resource

from ...util.dto import UploadDto

from ..helpers import upload_helper
api = UploadDto.api


@api.route('/')
class Upload(Resource):

    @api.response(201, 'Upload successfully.')
    @api.doc('upload a new file')
    def post(self):
        data = request.files['file']
        if data.mimetype == 'text/csv':
            json = upload_helper.csv_upload(data.read())
            # verify if data already inputed (do it in the future)
            upload_service.Boletos.bulk_create(json)

            return {'status': 'success', 'message': 'csv received and boletos created'}
        elif data.mimetype == 'application/pdf':
            json = upload_helper.pdf_to_dict(data.read())
            # create boletos (do it in the future)
            # upload_service.Boletos(json)
            return {'status': 'success', 'message': 'pdf received'}
