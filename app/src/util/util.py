import re
from flask import Blueprint
from flask_restx import Api
from datetime import datetime, date
from src.config import app_config
from src.config.config import Config


class ApiUtil():

    _blueprint = Blueprint('api', __name__, url_prefix="/"+Config.API_PREFIX)
    _api = Api(_blueprint, 
            doc='/doc/', authorizations=app_config.authorizations, security='apikey',
            version=Config.getEnvVariables(Config.API_VERSION),
            title=Config.TITLE, description=Config.TITLE,
            default=Config.API_PREFIX, default_label=Config.TITLE,
            contact=app_config.contato, contact_email=app_config.email
            )

    @staticmethod
    def getApi():
        return ApiUtil._api

    @staticmethod
    def getBlueprint():
        return ApiUtil._blueprint

class ValidationUtil():

    @staticmethod
    def validateNumber(number):
        return re.match(r'^([\d]+)$',number)
    
    @staticmethod
    def validarData(value):
        try:
            datetime.strptime(value, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Formato inválido de data")
        
        return value

    @staticmethod
    def validarCodigoSolicitacao(value):
        if(len(str(value)) != 12):
            raise ValueError("Código da solicitacao deve ter 12 caracteres")
        
        return value
        

