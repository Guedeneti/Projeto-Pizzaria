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

from source.db import db_report
from source.db import db_pizza
from source import user
from source.db import db_user


def Menu_Relatorio ():
    opcao = 1
    while opcao != 0:
        try:
            print('\n****************** RELATORIOS ******************')
            print('   [1] - Cliente')
            print('   [2] - Cliente Parametrizado')
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
                report_user('padrao')
            elif opcao == 2:
                report_user('parametro')
            elif opcao == 3:
                ()
            elif opcao == 4:
                db_pizza.Select( 0, 'Todas', False)
            elif opcao == 5:
                ReceitaPizza('Maior')
            elif opcao == 6:
                ReceitaPizza('Menor')


def ReceitaPizza(Tamanho):
    pizzas = db_report.Select('Pizza')

    if Tamanho == 'Maior':
        print('\n            ***** Maior  Receita ***** ')

        if pizzas != None:
            num = len(pizzas)

            for i in range(num):
                ref = float(pizzas[i][3].replace(',', '.'))
                if i == 0:
                    maior = ref
                elif ref > maior:
                    maior = ref

            for i in range(num):
                ref = float(pizzas[i][3].replace(',', '.'))
                if ref == maior:
                    print("\n     ID.......:", pizzas[i][0])
                    print("     Nome.....:", pizzas[i][1])
                    print("     Tipo.....:", pizzas[i][2])
                    print("     Valor....:", ref)

        else:
            print('Nenhuma Receita Encontrada!')

    elif Tamanho == 'Menor':
        print('\n            ***** Menor  Receita ***** ')

        if pizzas != None:
            num = len(pizzas)

            for i in range(num):
                ref = float(pizzas[i][3].replace(',', '.'))
                if i == 0:
                    menor = ref
                elif ref < menor:
                    menor = ref

            for i in range(num):
                ref = float(pizzas[i][3].replace(',', '.'))
                if ref == menor:
                    print("\n     ID.......:", pizzas[i][0])
                    print("     Nome.....:", pizzas[i][1])
                    print("     Tipo.....:", pizzas[i][2])
                    print("     Valor....:", ref)

        else:
            print('Nenhuma Receita Encontrada!')

def report_user(ref):
    usuario = db_user.select(4, 'tudo')
    if usuario == []:
        print("\n     ***** Nenhum Cadastro Encontrado *****")
    else:
        if ref == "padrao":
            for row in usuario:
                user.Exibir_Select(row, 1)
        elif ref == "parametro":
            print("\n           ***** Buscando Cliente *****")
            print("\nFormato de pesquisa YYYY-MM-DD")
            inicio = input("     Data Inicio....: ")
            fim = input("     Data Fim.......: ")
            db_report.user_data(inicio, fim)
