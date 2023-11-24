from app.controllers.crud_controllers import Cadastro, Login

def register_resources(db, api):
    api.add_resource(Cadastro, "/cadastro",
                    resource_class_kwargs={"db": db})
    api.add_resource(Login, "/login",
                     resource_class_kwargs={"db": db})
    