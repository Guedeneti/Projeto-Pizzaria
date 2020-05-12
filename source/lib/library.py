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
              ...
"""

import os
import datetime
from source.mov import pedido
from source import user
from source import pizza
from source.report import report

# Retorna somente a data e hora atual,
def Datetime_fmt(formatstring):
    # no formato YYYY-MM-DD HH: MM:SS
    if formatstring == 'YYYY-MM-DD HH:MM:SS.MS':
        return format(datetime.datetime.now())

def Limpar_Tela():
    print('\n' * 40)

def Cabecalho_Geral():
    Limpar_Tela()
    print('\n******************************************')
    print('BOB´s PIZZARIA - SISTEMA CONTROLE DE PEDIDOS')
    print('Desenvolvido por Guedeneti')
    print('Centro Universiário "Padre Anchieta"')
    print('********************************************')

def Pause():
    programPause = input("\nPressione <ENTER> para continuar...")

def Menu_Inicial():
    Cabecalho_Geral()
    opcao = 1
    while opcao != 0:
        try:
            print('\n               MENU PRINCIPAL')
            print('[1] - Abrir Pedido')
            print('[2] - Pedidos Abertos')
            print('[3] - Movimentações Cadastrais')
            print('[4] - Relatórios')
            print('[0] - Sair')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 4:
                raise ValueError("\nValor Inválido")
        except ValueError as e:
            print("\nValor Inválido")
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
            print('\n           MENU MOVIMENTAÇÕES')
            print('[1] - Usuarios')
            print('[2] - Pizzas')
            print('[0] - Voltar ao Menu Principal')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 2:
                raise ValueError("\nValor Inválido")
        except ValueError as e:
            print("\nValor Inválido")
        else:
            if opcao == 1:
                user.Menu_Cadastro()
            elif opcao == 2:
                pizza.Menu_Cadastro()

"""
def Abrir_Banco():
    fileDB = 'C:\\Users\vinip\Documents\Facul\3SEM\Saito\Pyton\Projeto_Pizzaria\source\db\db_pizzaria.sqlite'

    # verificando se arquivo de banco de dados existe
    print(f'Verificando se arquivo {fileDB} existe.')
    if not os.path.exists(fileDB):
        print(f'O arquivo: {fileDB} não existe!')
        exit(-1)
    else:
        pass

    # Criando a base de dados
    connection = sqlite3.connect(fileDB)

    # Retorna a abertura
    return connection.cursor(connection)

def data_entry(connection):
    cursor = Abrir_Banco()
    lista_cli = [(1, 'JOSE DA SILVA', 'JUNDIAI', 1500.55),
                 (2, 'ANA MARIA', 'JUNDIAI', 2300.69),
                 (3, 'MARIA DE SOUZA', 'CAMPINAS', 3547.02)]

    cursor.executemany("INSERT INTO cliente(id, nome, cidade, salario) \
                    values (?, ?, ?, ?)", lista_cli)

    tupla_cli = (4, 'ANTONIO LIMA', 'VARZEA PAULISTA', 1346.22)
    cursor.execute("INSERT INTO cliente(id, nome, cidade, salario) \
                    values (?, ?, ?, ?)", tupla_cli)

    connection.commit()
    print('Dados inseridos com sucesso!')
"""



    


