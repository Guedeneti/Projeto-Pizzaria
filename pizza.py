"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para tratativas em pedidos
Arquivo.....: pizza.py - Funcionalidades para controle das Pizzas
Autor.......: Mateus Pompermayer
Observações.: 2020-05-11 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-11 - [R01] Criação da função Menu_Cadastro - Versao 1.00
              2020-05-11 - [R01] Criação da função Insert - Versao 1.00
              ...
"""
import os
import sqlite3
from source.lib import library

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

    cursor.execute("INSERT INTO pizza(nome, tipo, data_criacao, ingredientes, valor_custo) \
                        values (:nome, :tipo, :datacriacao, :ingredientes, :valorcusto)", pizza,)

    connection.commit()

    print('\n\n***** Pizza Adicionada *****')



def Update():
    print('\nAtualizando')
    PizzaCodigo = input('\n    Digite o Codigo da Pizza...........: ')

def Select():
    print('\nBuscando')


def Delete():
    print('\nDeletando')