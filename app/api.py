from flask import Flask, Blueprint, abort, jsonify, request
from flask_restx import Resource, fields, apidoc
from flask.logging import default_handler
from healthcheck import HealthCheck

from src.config.config import Config 
from src.util.util import ApiUtil
from src.util.banner import Banner

from src.resources.projectsecurityissues import ConsultaDados




app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.logger.removeHandler(default_handler)
api = ApiUtil.getApi()
Banner.printBanner()


#HealthCheck Definitions
health = HealthCheck(app, "/"+Config.API_PREFIX+Config.HEALTHCHECK_URL)

@api.documentation
def swagger_ui():
    return apidoc.ui_for(api)

app.register_blueprint(ApiUtil.getBlueprint())

if __name__ == "__main__":
    debugEnabled = Config.getEnvVariables(Config.DEBUG)
    debugEnabled = True if debugEnabled != None else False
    app.run(debug=debugEnabled)
