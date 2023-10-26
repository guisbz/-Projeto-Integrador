from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
from flask_apispec import MethodResource

# from controllers import crud_controllers
# from services import crud_service
# from db.setup_db import setup_db

from resources.register_resources import register_resources

from dotenv import load_dotenv
import os

load_dotenv(override=True)

"""
aqui ficam o host, username, e password pro banco
"""

app = Flask(__name__)
api = Api(app)

# db_con = setup_db(host, user, password)
# json_path = os.getenv("json_path")
json_path = r"D:\Pessoal\Aleatorio\Projeto_Waldo\API\teste.json"

register_resources(json_path, api)


if __name__ == "__main__":
    app.run(debug=True)