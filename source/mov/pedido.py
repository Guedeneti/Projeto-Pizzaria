"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para tratativas em pedidos
Arquivo.....: pedido.py - Controle Principal dos pedidos
Autor.......: Vinicius Guedes
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-11 - [R01] Criação da função Abrir - Versao 1.00
              2020-05-10 - [R02] Criação da função Abertos - Versao 1.00
              ...
"""
from source.lib import library
from source.db import db_pedido
from source import user

def Abrir ():
    opcao = 1
    while opcao != 0:
        try:
            print('\n******************** PEDIDOS *******************')
            print('   [1] - Fazer Pedido')
            print('   [0] - Voltar')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 1:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                Fazer_Pedido(True, None)
                opcao = 0

def Abertos():
    print('\n Pedidos Abertos')
    library.Pause()

def Fazer_Pedido( New, id_pedido):
    if New == True:
        Tel = True
        print('\n           ***** Fazendo Pedido *****')
        while Tel:
            try:
                tel = input('\n    Digite o Telefone Fixo...........: ')
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                cliente, pizzas = db_pedido.Select(tel, 'Cliente')
                Tel = False
                if cliente != None:
                    ID_User = cliente[0]

                    if pizzas != None:
                        print("\nUltimas 3 Pizzas Pedidas:")

                        for pizza in pizzas:
                            print('\n')
                            print('     Nome..........: ', pizza[2])
                            print('     Tipo..........: ', pizza[1])
                            print('     Igredientes...: ', pizza[3])
                            print('     Valor Custo...: R$', pizza[4])
                    else:
                        print("\n           ***** Sem  Historico *****")
                else:
                    print('\n      ***** Nenhum Cadastro Encontrado *****')
                    ID_User = user.Insert()

        pedido = [ID_User]
        pedido.append(library.Datetime_fmt('YYYY-MM-DD'))
        pedido.append(library.Datetime_fmt('HH:MM:SS'))
        ID_Pedido = db_pedido.Insert('Pedido', pedido)
    print("\n         ***** Selecionar  Pizzas *****")
    Tamanho = True
    Quantidade = True
    CodigoPizza = True
    Pedido = True
    options = ["Media", "Grande", "Gigante"]

    while CodigoPizza:
        try:
            cod_pizza = int(input("\nCodigo da Pizza: "))
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            selectpizza = db_pedido.Select(cod_pizza, 'Pizza')
            if selectpizza != 0:
                CodigoPizza = False
                pizza = [(cod_pizza)]
                print('    Pizza...: ' + selectpizza[2])
    while Tamanho:
        try:
            print('\nEscolha uma opcao: ')
            print('\n   [1] - ' + options[0])
            print('   [2] - ' + options[1])
            print('   [3] - ' + options[2])
            opcaotamanho = int(input("Tamanho da pizza: "))
            if not 1 <= opcaotamanho <= 3:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcaotamanho in range(1, 4):
                tamanhopizza = options[opcaotamanho - 1]
                pizza.append(tamanhopizza)
                Tamanho = False
                print('    Tamanho....: ' + tamanhopizza)
    while Quantidade:
        try:
            quantidadepizza = int(input(f"Quantidade da Pizza {selectpizza[2]}: "))
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            pizza.append(quantidadepizza)
            Quantidade = False
            print('    Quantidade.: ' + str(quantidadepizza))

    Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizza[4].replace(',', '.')), quantidadepizza)
    pizza.append(Valor_Unit)
    pizza.append(Valor_Parcial)
    print('\n    Valor Unitario...: ' + str(Valor_Unit))
    print('    Valor Sub Total..: ' + str(Valor_Parcial))
    while Pedido:
        try:
            print('\n   [0] - Concluir Pedido')
            print('   [1] - Incluir mais Pizzas')
            opcao = int(input("Escolha uma opcao: "))
            if not 0 <= opcao <= 1:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao in range(0, 2):
                if New == False:
                    ID_Pedido = id_pedido
                if opcao == 1:
                    pizza.append(ID_Pedido)
                    Pedido = False
                    db_pedido.Insert('Itens', pizza)
                    Fazer_Pedido(False, ID_Pedido)
                else:
                    pizza.append(ID_Pedido)
                    db_pedido.Insert('Itens', pizza)
                    Pedido = False
                    print('\n          ***** Pedido Realizado *****')