"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto Pizzaria
Descricao...: Realizar a remoção no banco de dados com passagem de parametos, minimizando codigo.
Arquivo.....: db_user.py - Deletar padrão em tabelas no banco de dados
Autor.......: Vinicius Guedes
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              ...
"""

from source.db.database import tables

def insert (usuario):
    cursor, connection = tables.chamada_db('nao')
    cursor.executemany("INSERT INTO user(nome, tel_fix, tel_cel, cep, endereco, numero, complemento, bairro, cidade, uf) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", usuario)

    connection.commit()

    connection.close()

def select (tipo, ref):
    cursor, connection = tables.chamada_db('nao')
    if 1 <= tipo <=3:
        if tipo == 1:
            cursor.execute("SELECT * from user where id_user = ?", (ref,))
        elif tipo == 2:
            print(type(ref))
            cursor.execute("SELECT * from user where tel_fix = :ref", (ref,))
        elif tipo == 3:
            cursor.execute("SELECT * from user where tel_cel = ?", (ref,))
        aux = cursor.fetchone()
        connection.close()
        return aux

    elif tipo == 4:
        cursor.execute("SELECT * from user")
        aux = cursor.fetchall()
        connection.close()
        return aux
    connection.close()



def update(usuario):
    cursor, connection = tables.chamada_db('nao')

    cursor.executemany("UPDATE user set nome= ?, tel_fix = ?, tel_cel = ?, cep = ?, endereco = ?, numero = ?, complemento = ?, bairro = ?, cidade = ?, uf = ? where id_user = ?", (usuario))
    connection.commit()

    connection.close()

def delete(ref):
    cursor, connection = tables.chamada_db('nao')
    cursor.execute("SELECT * from pedido where id_user = ?", (ref,))
    func = cursor.fetchone()

    if func == None:
        cursor.execute("Delete from user where id_user = ?", (ref,))
        print('            ***** Usuario deletado ***** ')
    else:
        print('      ***** Usuario ja realizou um pedido ***** ')
        print('          ***** Usuario não deletado ***** ')

    connection.close()

def Achar_Id():
    cursor, connection = tables.chamada_db('nao')

    cursor.execute("SELECT id_user from user")
    user = cursor.fetchall()
    if user == None:
        user = 1
    connection.close()
    return len(user) + 1

