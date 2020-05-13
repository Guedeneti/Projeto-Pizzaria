"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para tratativas em pedidos
Arquivo.....: pizza.py - Funcionalidades para controle das Pizzas
Autor.......: Mateus Pompermayer
Observações.: 2020-05-11 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-11 - [R01] Criação da função Menu_Cadastro - Versao 1.00
              2020-05-12 - [R02] Criação da função Insert - Versao 1.00
              2020-05-13 - [R03] Criação da função Update - Versao 1.00
              2020-05-13 - [R04] Criação da função Select - Versao 1.00
              ...
"""
import os
import sqlite3
from source.lib import library
from source.db import db_pizza

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


def Menu_Cadastro():
    opcao = 1
    while opcao != 0:
        try:
            print('\n******************** PIZZAS ********************')
            print('   [1] - Inserir')
            print('   [2] - Alterar')
            print('   [3] - Consultar')
            print('   [4] - Excluir')
            print('   [5] - Voltar para 15 pizzas')
            print('   [0] - Voltar')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 4:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                Insert()
            elif opcao == 2:
                Update()
            elif opcao == 3:
                Select()
            elif opcao == 4:
                Delete()


def Insert():

    print('\n         ***** Inserindo Pizza *****')
    pizza = [input('\n    Nome da Pizza...........: ')]
    options = ["Salgada", "Doce"]
    type = True
    value = True
    while type:
        try:
            print('\n   [1] - ' + options[0])
            print('   [2] - ' + options[1])
            opcao = int(input("Numero do tipo da pizza: "))
            if not 1 <= opcao <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if opcao in range(1, 3):
                tipo = options[opcao - 1]
                pizza.append(tipo)
                type = False
                print('    Tipo...: ' + tipo)

    pizza.append(library.Datetime_fmt('YYYY-MM-DD HH:MM:SS.MS'))
    pizza.append(input('\n    Ingredientes...: '))

    while value:
        try:
            valor = input('\n    Valor Custo Padrao............: ')
            if not(valor.replace(',','',1).isdigit()):
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if valor.replace(',','',1).isdigit():
                pizza.append(valor)
                value = False

    print('\n ')

    print('Conexão com o banco')
    db_pizza.Insert(pizza)



def Update():
    update = True
    updatebool = True
    typeupdate = True
    valueupdate = True
    inativacao = False
    updateinativacao = False

    print('\nAtualizando')
    while update:
        try:
            PizzaCodigo = int(input('\n    Digite o Codigo da Pizza...........: '))
        except:
            print("\n           ***** Valor Inválido *****")

        else:
            pizza = db_pizza.Select(PizzaCodigo, False, True)
            print('\nPizza Selecionada')
            print(pizza)
            print('ID:', pizza[0], ';', ' Tipo:', pizza[1], ';', ' Nome:', pizza[2], ';', ' Ingredientes:',
                  pizza[3], ';', ' Valor Custo:', pizza[4])
            pizzainativa = pizza[5]
            update = False

    if pizzainativa != None:
        inativacao = True

    while updatebool:
        try:
            print('\n   [1] - Sim')
            print('   [2] - Nao')
            opcaoupdate = int(input("Deseja alterar essa pizza?: "))
            if not 1 <= opcaoupdate <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if opcaoupdate in range(1, 3):
                if(opcaoupdate == 1):
                    pizzaupdate = [input('\n    Nome da Pizza...........: ')]
                    optionsupdate = ["Salgada", "Doce"]
                    updatebool = False

                    while typeupdate:
                        try:
                            print('\n   [1] - ' + optionsupdate[0])
                            print('   [2] - ' + optionsupdate[1])
                            opcaoupdate = int(input("Numero do tipo da pizza: "))
                            if not 1 <= opcaoupdate <= 2:
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")

                        else:
                            if opcaoupdate in range(1, 3):
                                tipoupdate = optionsupdate[opcaoupdate - 1]
                                pizzaupdate.append(tipoupdate)
                                typeupdate = False
                                print('    Tipo...: ' + tipoupdate)

                    pizzaupdate.append(input('\n    Ingredientes...: '))

                    while valueupdate:
                        try:
                            valorupdate = input('\n    Valor Custo Padrao............: ')
                            if not (valorupdate.replace(',', '', 1).isdigit()):
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")

                        else:
                            if valorupdate.replace(',', '', 1).isdigit():
                                pizzaupdate.append(valorupdate)
                                valueupdate = False

                    while inativacao:
                        try:
                            print('\n   [1] - Sim')
                            print('   [2] - Nao')
                            inativacaoupdate = int(input('\n    Deseja reincluir essa pizza............: '))
                            if not 1 <= inativacaoupdate <= 2:
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")


                        else:
                            if inativacaoupdate in range(1, 3):
                                if inativacaoupdate == 1:
                                    updateinativacao = True
                                    inativacao = False
                                else:
                                    updateinativacao = False
                                    inativacao = False


                    pizzaupdate.append(PizzaCodigo)

                    if updateinativacao == True:
                        db_pizza.Update(pizzaupdate, updateinativacao)
                    else:
                        db_pizza.Update(pizzaupdate, updateinativacao)

                else:
                    print('Pizza nao alterada')
                    updatebool = False

def Select():
    Select = True
    print('\nBuscando')
    while Select:
        try:
            print('\n   [1] - Uma Pizza')
            print('   [2] - Todas Pizzas')
            opcaoselect = int(input("Deseja buscar uma ou todas pizzas?: "))
            if not 1 <= opcaoselect <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if opcaoselect in range(1, 3):
                if(opcaoselect == 1):
                    PizzaCodigo = int(input('\n    Digite o Codigo da Pizza...........: '))
                    db_pizza.Select(PizzaCodigo, True, False)
                    Select = False
                else:
                    db_pizza.Select( 0, False, False)
                    Select = False

def Delete():
    Delete = True
    delete = True
    print('\nDeletando')
    while delete:
        try:
            PizzaCodigo = int(input('\n    Digite o Codigo da Pizza...........: '))
        except:
            print("\n           ***** Valor Inválido *****")

        else:
            pizza = db_pizza.Select(PizzaCodigo, False, True)
            print('\nPizza Selecionada')
            print('ID:', pizza[0], ';', ' Tipo:', pizza[1], ';', ' Nome:', pizza[2], ';', ' Ingredientes:',
                  pizza[3], ';', ' Valor Custo:', pizza[4])
            delete = False

    while Delete:
        try:
            print('\n   [1] - Desativar')
            print('   [2] - Cancelar')
            opcaodelete = int(input("Deseja desativar a pizza?: "))
            if not 1 <= opcaodelete <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if opcaodelete in range(1, 3):
                if(opcaodelete == 1):
                    data_inativacao = library.Datetime_fmt('YYYY-MM-DD HH:MM:SS.MS')
                    db_pizza.Delete(data_inativacao, PizzaCodigo)
                    Delete = False
                else:
                    print('\nCancelado\n')
                    Delete = False
