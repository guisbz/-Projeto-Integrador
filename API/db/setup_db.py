from mysql.connector import connect, Error, errorcode
from dotenv import load_dotenv

import pandas as pd
import numpy as np
import unidecode
import os


load_dotenv(override=True)


class Setup_DB:
    def __init__(self, host: str, user: str, password: str, db_name: str):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = "users"

        # self.db_con = self.db_connection()

    def db_connection(self):
        try:
            db_con = connect(
                host=self.host,
                user=self.user,
                password=self.password
            )

            print("Conectado com o Banco MySQL")
            return db_con
        except Error as e:
            print("ERRO:", e)
            exit(1)

    def create_database(self):
        try:
            with connect(host=self.host,user=self.user,password=self.password) as db_con:
                create_db_query = f"CREATE DATABASE {self.db_name}"
                # print(db_con)
                with db_con.cursor() as cursor:
                    cursor.execute(create_db_query)

                print(f"Database {self.db_name} criada")
        except Error as e:
            if e.errno == errorcode.ER_DB_CREATE_EXISTS:
                print(f"Database {self.db_name} já existe")
            else:
                print("Error:", e)
                exit(1)

    def create_tables(self):
        query = f"""
        CREATE TABLE {self.db_name}.`users` (
            `nome` varchar(30) NOT NULL,
            `user` varchar(12) NOT NULL,
            `email` varchar(30) NOT NULL,
            `senha` varchar(12) NOT NULL, 
            `id` int(30) NOT NULL AUTO_INCREMENT,
            PRIMARY KEY (`id`),
            UNIQUE KEY (`user`),
            UNIQUE KEY (`email`)
        ) ENGINE=InnoDB AUTO_INCREMENT=1067 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """        

        try:
            with connect(host=self.host,user=self.user,password=self.password) as db_con:
                # print(db_con)
                with db_con.cursor() as cursor:
                    cursor.execute(query)

                print("A tabela users foi criada")

        except Error as e:
            if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("A tabela users já existe")
            else:
                print("Error:", e)
                exit(1)

                
if __name__ == "__main__":
    host=os.getenv("host")
    user=os.getenv("user")
    password=os.getenv("password")
    db_name=os.getenv("db_name")

    print("host:", host)
    print("user:", user)
    print("password:", password)
    print("db_name:", db_name)

    setup_db_obj = Setup_DB(host=host ,user=user ,password=password ,db_name=db_name)
    setup_db_obj.create_database()
    setup_db_obj.create_tables()

    # with connect(host=host,user=user,password=password) as db_con:
    #     print(db_con)
