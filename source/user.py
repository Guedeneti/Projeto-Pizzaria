"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para tratativas em pedidos
Arquivo.....: user.py - Funcionalidades para controle dos usuarios
Autor.......: Vinicius Guedes
Observações.: 2020-05-11 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-11 - [R01] Criação da função Menu_Cadastro - Versao 1.00
              2020-05-11 - [R02] Alteração na função Menu_Cadastro - Versao 1.00
              2020-05-11 - [R03] Criação e alteração na função Insert - Versao 1.00
              2020-05-11 - [R03] Criação e alteração na função Update - Versao 1.00
              2020-05-11 - [R03] Criação na função Select - Versao 1.00
              2020-05-11 - [R03] Criação da função Delete - Versao 1.00
              ...
"""

def Menu_Cadastro():
    opcao = 1
    while opcao != 0:
        try:
            print('\n******************* CLIENTES *******************')
            print('   [1] - Inserir')
            print('   [2] - Alterar')
            print('   [3] - Consultar')
            print('   [4] - Excluir')
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

def Insert ():
    print('\n         ***** Inserindo  Cliente *****')
    usuario = [input('\n    Nome...........: ')]
    usuario.append(input('\n    Telefone Fixo..: '))
    usuario.append(input('\n    Telefone Cel...: '))
    usuario.append(input('\n    CEP............: '))
    usuario.append(input('\n    Endereço.......: '))
    usuario.append(input('\n    Complemento....: '))
    usuario.append(input('\n    Bairro.........: '))
    usuario.append(input('\n    Cidade.........: '))
    usuario.append(input('\n    UF.............: '))
    print('\n ')

    print('Conecxão com o banco')

    print('         ***** Usuario adicionado *****')

def Update ():
    opcao = 1
    while opcao != 0:
        try:
            print('\n        ***** Atualizando  Cliente *****')
            print('\n     [1] - Cod do Cliente')
            print('\n     [2] - Numero do Telefone')
            opcao = eval(input('\n    Localizar por: '))
            if not 0 <= opcao <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                ref = eval(input('\n     COD. Cliente: '))
            elif opcao == 2:
                ref = eval(input('\n     Telefone: '))

def Select ():
    print('\n          ***** Buscando Cliente *****')

def Delete ():
    print('\n         ***** Deletando  Cliente *****')
