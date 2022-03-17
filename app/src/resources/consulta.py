from flask_restx import Resource
from src.util.util import ApiUtil
from src.util.logging import Logger



api = ApiUtil.getApi()

logger = Logger.getLogger(cls=__name__)

@api.route('/sendInform')
class SendInform(Resource):

    def post(self):
        return {"status":"OK"}

@api.route('/getInform')
class GetInform(Resource):

    def get(self):
        return {"status": "OK"}

    


    