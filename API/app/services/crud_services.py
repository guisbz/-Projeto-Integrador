from mysql.connector import connect, Error, errorcode
from dotenv import load_dotenv

import pandas as pd
import numpy as np
import unidecode
import os


def existe_nome(db_con, user):
    query = f"SELECT user from users.users"
    
    with db_con.cursor() as cursor:
        try:
            cursor.execute(query)
            users = set(row[0] for row in cursor.fetchall())
            return int(user in users)
        except Exception as e:
            db_con.rollback()
            print("Ocorreu um erro durante a verificação de nomes")
            print(str(e))
            exit(1)


## Wrapped functions

def cadastrar(db_con=None, user=None, senha=None, nome=None, email=None):
    insert_query = f"""
        INSERT INTO users.users (`user`, `senha`, `nome`, `email`)
        VALUES ('{user}', '{senha}', '{nome}', '{email}')    
    """

    if existe_nome(db_con, user):
        return {"status": "0", "message": "Usuário já existente", "error code": 1}
    else:
        try:
            with db_con.cursor() as cursor:
                cursor.execute(insert_query)
                db_con.commit()

                return {"status": "1", "message": "usuário cadastrado", "error code": 0}
        
        except Exception as e:
            db_con.rollback()
            print("Ocorreu um erro durante a inserção de dados")
            print("insert_query:", insert_query)
            print(str(e))
            exit(1)



def login(db_con, user, password):

    login_query = f"""
    SELECT user, senha from users.`users`
    wHERE
        user = "{user}" AND
        senha = "{password}"
    """

    with db_con.cursor() as cursor:
        try:
            cursor.execute(login_query)
            users = [row[0] for row in cursor.fetchall()]
            return bool(len(users))
        
        except Exception as e:
            db_con.rollback()
            print("Ocorreu um erro durante o login")
            print(str(e))
            exit(1)
        
        
    
