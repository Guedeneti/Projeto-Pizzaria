"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto03
Descricao...: Arquivo de biblioteca padrão
Arquivo.....: library.py - Função Principal contendo menu para chamada das demais funções
Autor.......: Vinicius Guedes
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-10 - [R01] Criação da função Datetime_fmt - Versao 1.00
              2020-05-10 - [R02] Criação da função Limpar_Tela - Versao 1.00
              2020-05-10 - [R03] Criação da função Cabeçalho_Geral - Versao 1.00
              2020-05-10 - [R04] Criação da função Pause - Versao 1.00
              2020-05-10 - [R05] Criação da função Menu_Inicial - Versao 1.00
              2020-05-10 - [R06] Criação da função Menu_Movimentacao - Versao 1.00
              2020-05-11 - [R07] Tentativa de criação da função Abrir_Banco - Versao 1.00
              2020-05-11 - [R08] Tentativa de criação da função data_entry - Versao 1.00
              ...
"""

import datetime
from source.mov import pedido
from source import user
from source import pizza
from source.report import report
from source.db.database import tables
from source.db import db_pizza


# Retorna somente a data e hora atual,
def Datetime_fmt(formatstring):
    # no formato YYYY-MM-DD HH: MM:SS
    if formatstring == 'YYYY-MM-DD HH:MM:SS.MS':
        return format(datetime.datetime.now())

def Limpar_Tela():
    print('\n' * 40)

def Cabecalho_Geral():
    Limpar_Tela()
    print('\n************************************************')
    print('* BOB´s PIZZARIA - SISTEMA CONTROLE DE PEDIDOS *')
    print('* Desenvolvido por Guedeneti                   *')
    print('* Centro Universiário "Padre Anchieta"         *')
    print('************************************************')

def Pause():
    programPause = input("\nPressione <ENTER> para continuar...")

def Menu_Inicial():
    Cabecalho_Geral()
    opcao = 1
    while opcao != 0:
        try:
            print('\n**************** MENU PRINCIPAL ****************')
            print('   [1] - Abrir Pedido')
            print('   [2] - Pedidos Abertos')
            print('   [3] - Movimentações Cadastrais')
            print('   [4] - Relatórios')
            print('   [0] - Sair')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 4:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                pedido.Abrir()
            elif opcao == 2:
                pedido.Abertos()
            elif opcao == 3:
                Menu_Movimentacao()
            elif opcao == 4:
                report.Menu_Relatorio()

def Menu_Movimentacao():
    opcao = 1;
    while opcao != 0:
        try:
            print('\n************** MENU MOVIMENTAÇÕES **************')
            print('   [1] - Usuarios')
            print('   [2] - Pizzas')
            print('   [9] - Reset de banco')
            print('   [0] - Voltar ao Menu Principal')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 2 and opcao != 9:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                user.Menu_Cadastro()
            elif opcao == 2:
                pizza.Menu_Cadastro()
            elif opcao == 9:
                ref = "BOB"
                while ref != 'BOB-PIZZARIA':
                    print('\n    Você está preste a apagar todos os dados do banco de dados!')
                    print('    Para confirmar digite BOB-PIZZARIA\n'
                          '    Para voltar digite SAIR')
                    ref = input('    Frase: ')
                    if ref == 'BOB-PIZZARIA':
                        tables.create_table()
                        db_pizza.create_db_pizza()
                    elif ref == 'SAIR':
                        ref= 'BOB-PIZZARIA'



    


