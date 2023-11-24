from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
from flask_apispec import MethodResource

from db.setup_db import Setup_DB


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
# json_path = r"D:\Pessoal\Aleatorio\Projeto_Waldo\API\teste.json"

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db_name="users"

db_obj = Setup_DB(host=host,user=user,password=password,db_name=db_name)
db_con = db_obj.db_connection()


register_resources(db_con, api)


if __name__ == "__main__":
    app.run(debug=False)