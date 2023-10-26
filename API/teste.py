import requests

base = "http://127.0.0.1:5000"
user = {"nome": "marcos", "senha": "69"}
cadastro_response = requests.post(base + "/cadastro", json=user)
print(cadastro_response.json())
login_response    = requests.post(base + "/login", json=user)
print(login_response.json())