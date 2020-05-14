"""
Data.Criacao: 2020-05-010
Projeto.....: Projeto Pizzaria
Descricao...: Realizar Pequisa no banco de dados com passagem de parametos, minimizando codigo.
Arquivo.....: db_pedido.py - Pesquisa padrão em tabelas no banco de dados
Autor.......: Vinicius Guedes
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              ...
"""

"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto Pizzaria
Descricao...: Realizar inserção no banco de dados com passagem de parametos, minimizando codigo.
Arquivo.....: db_pizza.py - Inserção padrão em tabelas no banco de dados
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


def Insert(Pedido):
    cursor, connection = tables.chamada_db('nao')
    cursor.execute("INSERT INTO pedido(id_user, data_inicio, hora) \
                        values (:id_user, :data_inicio, :hora)", Pedido)
    connection.commit()

    cursor.execute("SELECT * FROM pedido ORDER BY id_pedido DESC LIMIT 1")
    id_pedido = cursor.fetchone()

    connection.close()

    return format(id_pedido[0])

####################################################################################################################################################################################################################################################

def Select(Ref, Pesq):
    if Pesq == 'Cliente':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("SELECT * FROM user where tel_fix = :tel", (Ref,))
        cliente = cursor.fetchone()  # retrieve the first row
        if cliente != None:
            idcliente = cliente[0]
            cursor.execute("SELECT pizza.* FROM pedido \
                            LEFT JOIN inf_pedido ON pedido.id_pedido = inf_pedido.id_pedido \
                            LEFT JOIN pizza ON inf_pedido.id_pizza = pizza.id_pizza \
                            where id_user = :id AND pizza.id_pizza IS NOT NULL", (idcliente,))
            pizzas = cursor.fetchall()  # retrieve the first row
            print(pizzas)

            if not pizzas:
                connection.close()
                return cliente, None
            else:
                connection.close()
                return cliente, pizzas
        elif cliente == None:
            connection.close()
            return None, None

    elif Pesq == 'Pizza':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("SELECT * FROM pizza where id_pizza = :id", (Ref,))
        pizza = cursor.fetchone()  # retrieve the first row
        connection.close()
        return pizza

##################################################################################################################################################################################################################################################


