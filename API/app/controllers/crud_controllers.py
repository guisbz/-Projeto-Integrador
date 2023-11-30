from flask_restful import Api, Resource, reqparse, abort
from flask_apispec.views import MethodResource
from flask_apispec import use_kwargs
from marshmallow import fields

from app.services.crud_services import cadastrar, login

class Cadastro(MethodResource, Resource):
    def __init__(self, db):
        self.db = db


    @use_kwargs(
        {
         "nome": fields.Str(),
         "senha": fields.Str(),
         "user": fields.Str(),
         "email": fields.Str()
        }
    )
    def post(self, **kwargs):
        nome = kwargs.get("nome")
        senha = kwargs.get("senha")

        nome = kwargs.get("nome")
        senha = kwargs.get("senha")
        user = kwargs.get("user")
        email = kwargs.get("email")




        if user and senha:
            return cadastrar(db_con=self.db, nome=nome,senha=senha,user=user,email=email)
        else:
            return {"status": 0, "message": "Nome e Senha Nula", "error code": 4}
        
    
class Login(MethodResource, Resource):
    def __init__(self, db):
        self.db = db

    @use_kwargs(
        {
         "user": fields.Str(),
         "senha": fields.Str()   
        }
    )
    def post(self, **kwargs):
        user = kwargs.get("user")
        senha = kwargs.get("senha")

        if user and senha:
            return {"status": 1, "value": int(login(self.db, user, senha))}
        else:
            return {"status": 0, "message": "Nome e Senha Nula", "error code": 4}

