import requests
import time

base = "http://localhost:5000"
user_cadastro = {"user": "marcos_telec", 
        "senha": "6912",
        "email": "marcos_telec@gmail.com",
        "nome": "Marcos Telecki da Silva Costa"}
user_login = {"user": "marcos",
              "senha": "6912",
              }

users_de_teste = [
        {"user": "gui",
              "senha": "123","email": "guilherme1@gmail.com",
        "nome": "guilherme2"
              },
              {"user": "maria",
              "senha": "321","email": "maria@gmail.com",
        "nome": "Mariana S"
              },
              {"user": "eli",
              "senha": "321","email": "eli@gmail.com",
        "nome": "Elias Mota"
              },
              {"user": "teste5",
              "senha": "321","email": "test5@gmail.com",
        "nome": "Telekin"
              },
]
print("\t\t Cadastro")
print(f"Agora estamos cadastrando o usuário {user_cadastro['user']}")
cadastro_response = requests.post(base + "/cadastro", json=user_cadastro)
print(cadastro_response)
print(cadastro_response.json())

print("\t\tLogin")
print("Agora vamos testar para vários usuários")
print("-"*10)
for i in users_de_teste:
        aux = {"user": i["user"], "senha": i["senha"]}
        login_response    = requests.post(base + "/login", json=aux)
        print(login_response.json())
        if login_response.json():
                print(f"\t Usuário {i['user']} Acesso Concedido!")
        else:
                        print(f"\t Usuário {i['user']} Acesso Negado")

print("\t\tOutros Testes")
print("Agora vamos cadastrar todos os outros")
for i in users_de_teste:
        cadastro_response = requests.post(base + "/cadastro", json=i)
print("usuários cadastrados, agora testando o login")
for k, i in enumerate(users_de_teste):
        aux = {"user": i["user"], "senha": i["senha"]}
        print(i)
        login_response    = requests.post(base + "/login", json=aux)
        if login_response.json():
                print(f"\t Usuário {i['user']} Acesso Concedido!")
        else:
                        print(f"\t Usuário {i['user']} Acesso Negado")