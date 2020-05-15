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
        id_pedido = cursor.fetchone()

        connection.close()

        return format(id_pedido[0])
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
            cursor.execute("SELECT pizza.* FROM pedido \
                            LEFT JOIN inf_pedido ON pedido.id_pedido = inf_pedido.id_pedido \
                            LEFT JOIN pizza ON inf_pedido.id_pizza = pizza.id_pizza \
                            where id_user = :id AND pizza.id_pizza IS NOT NULL \
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
            print("\n         ***** Codigo não encontrado *****")
            return (0)
        else:
            connection.close()
            return pizza

##################################################################################################################################################################################################################################################


