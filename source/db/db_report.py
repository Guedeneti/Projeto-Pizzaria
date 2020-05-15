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


def Insert(pizza):
    cursor, connection = tables.chamada_db('nao')
    cursor.execute("INSERT INTO pizza(nome, tipo, data_criacao, ingredientes, valor_custo) \
                        values (:nome, :tipo, :datacriacao, :ingredientes, :valorcusto)", pizza)
    connection.commit()
    connection.close()
    return print('          ***** Pizza  Adicionada *****')

####################################################################################################################################################################################################################################################

def Update(pizzaupdate, inativacao):
    cursor, connection = tables.chamada_db('nao')
    if inativacao == True:
        cursor.execute("UPDATE pizza \
                       set nome = ?, tipo = ?, ingredientes = ?, valor_custo = ?, data_inativacao = ? \
                       where id_pizza = ?",
                       (pizzaupdate[0], pizzaupdate[1], pizzaupdate[2], pizzaupdate[3], None, pizzaupdate[4]))
    else:
        cursor.execute("UPDATE pizza \
                       set nome = ?, tipo = ?, ingredientes = ?, valor_custo = ? \
                       where id_pizza = ?", (pizzaupdate[0], pizzaupdate[1], pizzaupdate[2], pizzaupdate[3], pizzaupdate[4]))

    connection.commit()
    connection.close()

    print('\n          ***** Pizza Alterada *****')

####################################################################################################################################################################################################################################################

def Select(Tabela, Codigo):
    cursor, connection = tables.chamada_db('nao')
    if Tabela == 'Cliente':

        cursor.execute("SELECT id_pizza, tipo, nome, ingredientes, valor_custo, data_inativacao from pizza where id_pizza = ?", (Codigo,) )

        pizza = cursor.fetchone()  # retrieve the first row
        connection.close()

        return pizza

    elif Tabela == 'Pizza':
        cursor.execute("SELECT id_pizza, tipo, nome, ingredientes, valor_custo, data_criacao from pizza where data_inativacao is null")
        pizzas = cursor.fetchall()  # retrieve the first row
        if pizzas == None:
            connection.close()
            return print('\n      ***** Nenhuma pizza encontrada *****')
        else:
            connection.close()
            return pizzas

    elif Tabela == 'Pedido':
        pass


