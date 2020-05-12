"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para criar banco de dados
Arquivo.....: user.py - Funcionalidades para controle dos usuarios
Autor.......: Mateus Pompermayer
Observações.: 2020-05-12 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-12 - [R01] Criação do database pizzaria - Versao 1.00
              2020-05-12 - [R02] Criação da tabela pizza - Versao 1.00
              ...
"""

import os
import sqlite3

#definindo um arquivo para clientes
fileDB = 'C:\\Users\mateu\Documents\Pycharm\database\pizzariadb.sqlite'

#excluindo o arquivo de banco de dados
print('Excluindo o arquivo de banco de dados, caso exista.')
if os.path.exists(fileDB):
    os.remove(fileDB)
else:
    print(f'O arquivo: {fileDB} não existe!')

# Criando a base de dados
print(f'Criando um novo arquivo {fileDB}')
connection = sqlite3.connect(fileDB)

# Get a cursor object
cursor = connection.cursor()

#Criacao de tabelas
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS pizza \
                   (id      integer PRIMARY KEY, \
                    tipo    varchar(40), \
                    data_criacao  data, \
                    data_inativacao  data, \
                    nome  varchar(80), \
                    ingredientes varchar(120), \
                    valor_custo decimal(10,2) )'
                   )
create_table()