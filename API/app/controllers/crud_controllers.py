from flask_restful import Api, Resource, reqparse, abort
from flask_apispec.views import MethodResource
from flask_apispec import use_kwargs
from marshmallow import fields

from app.services.crud_services import cadastrar, login

class Cadastro(MethodResource, Resource):
    def __init__(self, json_path):
        self.json_path = json_path


    @use_kwargs(
        {
         "nome": fields.Str(),
         "senha": fields.Str()   
        }
    )
    def post(self, **kwargs):
        nome = kwargs.get("nome")
        senha = kwargs.get("senha")

        if nome and senha:
            return cadastrar(nome, senha, self.json_path)
        else:
            return {"status": 0, "message": "Nome e Senha Nula", "error code": 4}
        
    
class Login(MethodResource, Resource):
    def __init__(self, json_path):
        self.json_path = json_path

    @use_kwargs(
        {
         "nome": fields.Str(),
         "senha": fields.Str()   
        }
    )
    def post(self, **kwargs):
        nome = kwargs.get("nome")
        senha = kwargs.get("senha")

        if nome and senha:
            return login(nome, senha, self.json_path)
        else:
            return {"status": 0, "message": "Nome e Senha Nula", "error code": 4}

