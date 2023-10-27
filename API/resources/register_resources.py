from app.controllers.crud_controllers import Cadastro, Login

def register_resources(json_path, api):
    api.add_resource(Cadastro, "/cadastro",
                    resource_class_kwargs={"json_path": json_path})
    api.add_resource(Login, "/login",
                     resource_class_kwargs={"json_path": json_path})
    