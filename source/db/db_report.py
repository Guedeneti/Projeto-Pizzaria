"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto Pizzaria
Descricao...: Realizar inserção no banco de dados com passagem de parametos, minimizando codigo.
Arquivo.....: db_report.py - Inserção padrão em tabelas no banco de dados
Autor.......: Mateus Pompermayer
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-13 - [R00] Criação da funcao Insert - Versao 1.00
              2020-05-13 - [R00] Criação da funcao Update - Versao 1.00
              2020-05-13 - [R00] Criação da funcao Select - Versao 1.00
              2020-05-13 - [R00] Criação da funcao Delete - Versao 1.00
              ...
"""
import os
from source.db.database import tables
from source.lib import library

def Select(Tabela):
    cursor, connection = tables.chamada_db('nao')

    if Tabela == 'Pizza':
        cursor.execute("SELECT id_pizza, tipo, nome, valor_custo from pizza where data_inativacao is null")
        pizzas = cursor.fetchall()  # retrieve the first row
        if pizzas == None:
            connection.close()
            return print('\n      ***** Nenhuma pizza encontrada *****')
        else:
            connection.close()
            return pizzas

def user_data(inicio, fim):
    print('Ola')


