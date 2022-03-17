import os

class Config():
    """
        Classe responsável por retornar para as aplicação as
        configurações necessárias para execução

        @author: Yuri Fialho
        @since: 27/01/2022
    """

    ENV = 'FLASK_ENV'
    API_VERSION = 'API_VERSION'
    TITLE = 'MOTIRO FOREIGN SERVICE'

    API_PREFIX = ''

    HEALTHCHECK_URL = '/healthcheck'
    MOTIRO_AGENT_URL = 'MOTIRO_AGENT_URL'

    DEBUG = 'DEBUG'    

    @staticmethod
    def getEnvVariables(key):
        return os.getenv(key)
