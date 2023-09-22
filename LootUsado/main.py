from flask import Flask, render_template, request, flash, redirect
import json
import os

from flask.json import jsonify


app = Flask(__name__)
app.config['SECRET_KEY']= "PALAVRA-SECRETA"


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        novo_usuario = request.form.get('novo-usuario')
        nova_senha = request.form.get('nova-senha')

        # Valide se o nome de usuário já existe
        with open('usuarios.json', 'r') as usuarios:
            lista = json.load(usuarios)
            for c in lista:
                if novo_usuario == c['nome']:
                    flash('O nome de usuário já existe. Escolha outro.')
                    return redirect("/cadastro")

        # Se o nome de usuário não existe, adicione o novo usuário ao arquivo JSON
        novo_usuario_obj = {
            "nome": novo_usuario,
            "senha": nova_senha
        }
        lista.append(novo_usuario_obj)
        with open('usuarios.json', 'w') as usuarios:
            json.dump(lista, usuarios, indent=4)

        flash('Registro realizado com sucesso. Faça o login.')
       
        return redirect("/")
    
    return render_template("html/cadastro.html")

@app.route('/register', methods=['POST'])
def register():
    novo_usuario = request.form.get('nome')
    nova_senha = request.form.get('senha')

    if not novo_usuario or not nova_senha:
        return jsonify({"error": "Nome de usuário e senha são obrigatórios!"})

    # Ler os usuários existentes do arquivo JSON
    with open('usuarios.json', 'r') as usuarios_file:
        lista = json.load(usuarios_file)

    # Verificar se o nome de usuário já existe
    for usuario in lista:
        if usuario['nome'] == novo_usuario:
            return jsonify({"error": "O nome de usuário já existe. Escolha outro."})

    # Adicionar o novo usuário à lista
    novo_usuario_obj = {
        "nome": novo_usuario,
        "senha": nova_senha
    }
    lista.append(novo_usuario_obj)

    # Salvar a lista atualizada de volta no arquivo JSON com a codificação correta
    with open('usuarios.json', 'w', encoding='utf-8') as usuarios_file:
        json.dump(lista, usuarios_file, ensure_ascii=False, indent=4)

    return jsonify({"message": "Registro realizado com sucesso!"})

@app.route("/")
def home():
    return render_template("html/login.html")

@app.route("/login", methods=['POST'])
def login():
    usuario = request.form.get('nome')
    senha = request.form.get('senha')

    with open('usuarios.json') as usuarios:
        lista = json.load(usuarios)
        cont = 0
        for c in lista:
            cont+=1
            if usuario == c['nome'] and senha == c['senha']:
                return render_template("html/acesso.html", nomeUsuario=c['nome'])
            if cont >= len(lista):
                flash('usuario invalido')
                return redirect("/")
    print(usuario)
    print(senha)

    


if __name__ in '__main__':
    app.run(debug=True)