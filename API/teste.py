import requests
import time

base = "http://localhost:5000"
user_cadastro = {"user": "marcos_telec", 
        "senha": "6912",
        "email": "marcos_telec@gmail.com",
        "nome": "Marcos Telecki da Silva Costa"}
user_login = {"user": "marcos_telec",
              "senha": "6912",
              }
time.sleep(0.01)
cadastro_response = requests.post(base + "/cadastro", json=user_cadastro)
print(cadastro_response)
print(cadastro_response.json())
login_response    = requests.post(base + "/login", json=user_login)
print(login_response)
print(login_response.json())