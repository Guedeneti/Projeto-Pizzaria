"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto Pizzaria
Descricao...: Arquivo main para relatorios.
Arquivo.....: report.py - Arquivo padrão para relatorios
Autor.......: Vinicius Guedes
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-10 - [R01] Criação da função Menu_Relatorio - Versao 1.00
              ...
"""

from source.lib import library
from source.db import db_report


def Menu_Relatorio ():
    opcao = 1
    while opcao != 0:
        try:
            print('\n****************** RELATORIOS ******************')
            print('   [1] - Cliente')
            print('   [2] - Cliente Completo')
            print('   [3] - Pedidos')
            print('   [4] - Pizza')
            print('   [5] - Pizza - Maior receita')
            print('   [6] - Pizza - Menor receita')
            print('   [0] - Voltar')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 6:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                ()
            elif opcao == 2:
                ()
            elif opcao == 3:
                ()
            elif opcao == 4:
                ()
            elif opcao == 5:
                ReceitaPizza('Maior')
            elif opcao == 6:
                ReceitaPizza('Menor')


def ReceitaPizza(Tamanho):
    if Tamanho == 'Maior':
        size = 0
        print('\nMaior Receita: ')
        Pizzas = db_report.Select('Pizza', 0)

        if Pizzas != None:
            for pizza in Pizzas:
                if size < len(pizza[3]):
                    size = len(pizza[3])
                    MaiorReceita = (pizza[0], pizza[1], pizza[2], pizza[3], pizza[4], pizza[5])

            print('\nID.............: ', MaiorReceita[0])
            print('Tipo...........: ', MaiorReceita[1])
            print('Nome...........: ', MaiorReceita[2])
            print('Ingredientes...: ', MaiorReceita[3])
            print('Valor Custo....: R$', MaiorReceita[4])
            print('Data Criacao...: ', MaiorReceita[5])

        else:
            print('Nenhuma Receita Encontrada!')
    elif Tamanho == 'Menor':
        print('\nMenor Receita: ')
        Pizzas = db_report.Select('Pizza', 0)
        size = len(Pizzas[0][3])
        if Pizzas != None:
            for pizza in Pizzas:
                if size > len(pizza[3]):
                    size = len(pizza[3])
                    MaiorReceita = (pizza[0], pizza[1], pizza[2], pizza[3], pizza[4], pizza[5])

            print('\nID.............: ', MaiorReceita[0])
            print('Tipo...........: ', MaiorReceita[1])
            print('Nome...........: ', MaiorReceita[2])
            print('Ingredientes...: ', MaiorReceita[3])
            print('Valor Custo....: R$', MaiorReceita[4])
            print('Data Criacao...: ', MaiorReceita[5])

        else:
            print('Nenhuma Receita Encontrada!')


    elif Tamanho == 'Menor':
        print('Receita Menor')