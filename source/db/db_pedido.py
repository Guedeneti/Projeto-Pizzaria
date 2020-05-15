"""
Data.Criacao: 2020-05-010
Projeto.....: Projeto Pizzaria
Descricao...: Realizar Pequisa no banco de dados com passagem de parametos, minimizando codigo.
Arquivo.....: db_pedido.py - Pesquisa padrão em tabelas no banco de dados
Autor.......: Vinicius Guedes
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              ...
"""

import os
from source.db.database import tables
from source.lib import library


def Insert(Table, Dados):
    if Table == 'Pedido':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("INSERT INTO pedido(id_user, data_inicio, hora) \
                            values (:id_user, :data_inicio, :hora)", Dados)
        connection.commit()

        cursor.execute("SELECT * FROM pedido ORDER BY id_pedido DESC LIMIT 1")
        pedido = cursor.fetchone()

        connection.close()

        return format(pedido[0])

    elif Table == 'Itens':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("INSERT INTO inf_pedido( id_pizza, tamanho, qtd, valor_unit, sub_total, id_pedido) \
                                    values (:id_pizza, :tamanho, :qtd, :valor_unit, :sub_total, :id_pedido)", Dados)
        connection.commit()

        connection.close()

####################################################################################################################################################################################################################################################

def Select(Ref, Pesq):
    if Pesq == 'Cliente':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("SELECT * FROM user where tel_fix = :tel", (Ref,))
        cliente = cursor.fetchone()  # retrieve the first row
        if cliente != None:
            idcliente = cliente[0]
            cursor.execute("SELECT pizza.*, (select COUNT(inf_pedido.id_item) FROM pedido \
                            LEFT JOIN inf_pedido ON pedido.id_pedido = inf_pedido.id_pedido \
                            WHERE id_user = :id) as qtde FROM pedido \
                            LEFT JOIN inf_pedido ON pedido.id_pedido = inf_pedido.id_pedido \
                            LEFT JOIN pizza ON inf_pedido.id_pizza = pizza.id_pizza \
                            WHERE id_user = :id AND pizza.data_inativacao IS NULL \
                            ORDER BY inf_pedido.id_item DESC LIMIT 3", (idcliente,))
            pizzas = cursor.fetchall()  # retrieve the first row

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

        if not pizza:
            connection.close()
            print("\nCodigo não encontrado")
            return (0)
        else:
            connection.close()
            return pizza

    elif Pesq == 'Valor':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("select inf_pedido.sub_total FROM pedido \
                        LEFT JOIN inf_pedido ON pedido.id_pedido = inf_pedido.id_pedido \
                        where pedido.id_pedido = :id", (Ref,))
        valores = cursor.fetchall()  # retrieve the first row

        if not valores:
            connection.close()
            print("\nValores não encontrados")
            return (0)
        else:
            connection.close()
            return valores

    elif Pesq == 'Hora':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("select hora FROM pedido \
                        where pedido.id_pedido = :id", (Ref,))
        hora = cursor.fetchall()  # retrieve the first row

        if not hora:
            connection.close()
            print("\nValores não encontrados")
            return (0)
        else:
            connection.close()
            return hora

##################################################################################################################################################################################################################################################

def Update( Table, ref, ID_Pedido):
    if Table == 'Hora':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("UPDATE pedido \
                        set hora = ? \
                        where id_pedido = ?",
                        (ref, ID_Pedido))
        connection.commit()
        connection.close()
    elif Table == 'Total':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("UPDATE pedido \
                                set total_pedido = ? \
                                where id_pedido = ?",
                       (ref, ID_Pedido))
        connection.commit()
        connection.close()

    elif Table == 'Troco':
        cursor, connection = tables.chamada_db('nao')
        cursor.execute("UPDATE pedido \
                                set troco_pedido = ? \
                                where id_pedido = ?",
                       (ref, ID_Pedido))
        connection.commit()
        connection.close()


##################################################################################################################################################################################################################################################

