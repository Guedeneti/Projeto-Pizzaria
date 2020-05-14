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
    print('\n Abrindo Pedido')
    opcao = 1
    while opcao != 0:
        try:
            print('\n******************* PEDIDOS *******************')
            print('   [1] - Fazer Pedido')
            print('   [0] - Voltar')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 1:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                Fazer_Pedido()

    library.Pause()

def Abertos ():
    print('\n Pedidos Abertos')
    library.Pause()


def Fazer_Pedido():
    print('\n         ***** Fazendo Pedido *****')
    tel = input('\n    Digite o Telefone Fixo...........: ')
    cliente, pizzas = db_pedido.Select(tel, 'Cliente')

    if cliente != None:
        ID_User = cliente[0]
        if pizzas != None:
            print("Ultimas Pizzas Pedidas: ")
            for pizza in pizzas:
                print('     Id............: ', pizza[0])
                print('     Tipo..........: ', pizza[1])
                print('     Nome..........: ', pizza[2])
                print('     Igredientes...: ', pizza[3])
                print('     Valor Custo...: R$', pizza[4])
        else:
            print("Nenhuma Pizza Encontrada!")
    else:
        print('\nCliente nao encontrado!')
        ID_User = user.Insert()

    pedido = [ID_User]
    pedido.append(library.Datetime_fmt('YYYY-MM-DD'))
    pedido.append(library.Datetime_fmt('HH:MM:SS'))

    ID_Pedido = db_pedido.Insert(pedido)

    print("\n         ***** Selecionar Pizzas *****")
    Tamanho = True
    Quantidade = True
    CodigoPizza = True
    Pedido = True
    options = ["Media", "Grande", "Gigante"]
    while Pedido:
        try:
            while CodigoPizza:
                try:
                    cod_pizza = int(input("\nCodigo da Pizza: "))
                except ValueError as e:
                    print("\n           ***** Valor Inválido *****")
                else:
                    selectpizza = db_pedido.Select(cod_pizza, 'Pizza')
                    CodigoPizza = False

                    pizza = [(cod_pizza)]
                    print('    Pizza...: ' + selectpizza[2])
            while Tamanho:
                try:
                    print('\nEscolha uma opcao: ')
                    print('\n   [1] - ' + options[0])
                    print('   [2] - ' + options[1])
                    print('   [3] - ' + options[2])
                    opcaotamanho = int(input("Numero do tamanho da pizza: "))
                    if not 1 <= opcaotamanho <= 3:
                        raise ValueError("\n           ***** Valor Inválido *****")
                except ValueError as e:
                    print("\n           ***** Valor Inválido *****")
                else:
                    if opcaotamanho in range(1, 4):
                        tamanho = options[opcaotamanho - 1]
                        pizza.append(tamanho)
                        Tamanho = False
                        print('    Tamanho...: ' + tamanho)
            while Quantidade:
                try:
                    quantidade = int(input(f"Quantidade da Pizza {selectpizza[2]}: "))
                except ValueError as e:
                    print("\n           ***** Valor Inválido *****")
                else:
                    pizza.append(quantidade)
                    Quantidade = False
                    print('    Quantidade...: ' + str(quantidade))

            Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanho, float(selectpizza[4].replace(',', '.')), quantidade)
            pizza.append(Valor_Unit)
            pizza.append(Valor_Parcial)
            print('\n    Valor Unitario...: ' + str(Valor_Unit))
            print('    Valor Sub Total..: ' + str(Valor_Parcial))

            print('\n   [0] - Concluir Pedido')
            print('   [1] - Incluir mais Pizzas')
            opcao = int(input("Escolha uma opcao: "))
            if not 0 <= opcao <= 1:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao in range(1, 2):
                if opcao == 1:
                    pass
                elif opcao == 0:
                    #Insert(Pizzas)
                    Pedido = False