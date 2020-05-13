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
import sqlite3

#definindo um arquivo para clientes
fileDB = 'C:\\Users\mateu\Documents\Pycharm\database\pizzariadb.sqlite'

#verificando se arquivo de banco de dados existe
print(f'Verificando se arquivo {fileDB} existe.')
if not os.path.exists(fileDB):
    print(f'O arquivo: {fileDB} não existe!')
    exit(-1)
else:
    pass

# Criando a base de dados
connection = sqlite3.connect(fileDB)

# Get a cursor object
cursor = connection.cursor()



def Insert(pizza):

    cursor.execute("INSERT INTO pizza(nome, tipo, data_criacao, ingredientes, valor_custo) \
                        values (:nome, :tipo, :datacriacao, :ingredientes, :valorcusto)", pizza)
    connection.commit()
    return print('\n\n***** Pizza Adicionada *****')

####################################################################################################################################################################################################################################################

def Update(pizzaupdate, inativacao):

    if inativacao == True:
        cursor.execute("UPDATE pizza \
                       set nome = ?, tipo = ?, ingredientes = ?, valor_custo = ?, data_inativacao = ? \
                       where id = ?",
                       (pizzaupdate[0], pizzaupdate[1], pizzaupdate[2], pizzaupdate[3], None, pizzaupdate[4]))
    else:
        cursor.execute("UPDATE pizza \
                       set nome = ?, tipo = ?, ingredientes = ?, valor_custo = ? \
                       where id = ?", (pizzaupdate[0], pizzaupdate[1], pizzaupdate[2], pizzaupdate[3], pizzaupdate[4]))

    connection.commit()

    print('\n\n***** Pizza Alterada *****')

####################################################################################################################################################################################################################################################

def Select(PizzaCodigo, bool, select):
    if select == True:
        cursor.execute("SELECT id, tipo, nome, ingredientes, valor_custo, data_inativacao from pizza where id = ?", (PizzaCodigo,) )
        pizza = cursor.fetchone()  # retrieve the first row
        return pizza
    else:
        if bool == True:
            cursor.execute("SELECT id, tipo, nome, ingredientes, valor_custo, data_criacao from pizza where id = ? and data_inativacao is null", (PizzaCodigo,) )
            pizza = cursor.fetchone()  # retrieve the first row
            print('\nPizza Selecionada\n')
            if pizza == None:
                return print('\nNenhuma pizza encontrada\n')
            else:
                return print('ID:', pizza[0], ';', ' Tipo:', pizza[1], ';', ' Nome:', pizza[2], ';', ' Ingredientes:', pizza[3], ';', ' Valor Custo:', pizza[4], ';', ' Data Criacao:', pizza[5])  # Imprime o primeiro campo
        else:
            cursor.execute("SELECT id, tipo, nome, ingredientes, valor_custo, data_criacao from pizza where data_inativacao is null")
            pizzas = cursor.fetchall()  # retrieve the first row

            print('\nTodas Pizzas\n')
            if pizzas == None:
                return print('\nNenhuma pizza encontrada\n')
            else:
                for pizza in pizzas:
                 pizzas = [print('ID:', pizza[0], ';', ' Tipo:', pizza[1], ';', ' Nome:', pizza[2], ';', ' Ingredientes:', pizza[3],
                          ';', ' Valor Custo:', pizza[4], ';', ' Data Criacao:', pizza[5])]
                return pizzas

##################################################################################################################################################################################################################################################

def Delete(data, PizzaCodigo):
    cursor.execute("UPDATE pizza \
                    set data_inativacao = ? \
                    where id = ?", (data, PizzaCodigo,))
    connection.commit()
    return print('\nPizza Desativada\n')