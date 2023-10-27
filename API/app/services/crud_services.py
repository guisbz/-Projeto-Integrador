import json

def json_to_dict(json_path: str) -> dict:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

def dict_to_json(json_path: str, data: str) -> None:
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def existe_nome(data, nome):
    for user in data:
        if user["nome"] == nome:
            return 1

    return 0


## Wrapped functions

def cadastrar(nome=None, senha=None, json_path=None):
    data = json_to_dict(json_path)
    if existe_nome(data, nome):
        return {"status": "0", "message": "nome já existente", "error code": 1}
    else:
        new_user = {"nome": nome, "senha": senha}

        data.append(new_user)
        # print(data)
        dict_to_json(json_path, data)


        return {"status": "1", "message": "usuário cadastrado", "error code": 0}

def login(nome=None, senha=None, json_path=None):
    data = json_to_dict(json_path)
    
    for user in data:
        if user["nome"] == nome:
            if user["senha"] == senha:
                return {"status": "1", "message": "usuário validado", "error code": 0}
            else:
                return {"status": "0", "message": "senha inválida", "error code": 2}
    
    return {"status": "0", "message": "usuário não cadastrado", "error code": 3}
        
        
    
