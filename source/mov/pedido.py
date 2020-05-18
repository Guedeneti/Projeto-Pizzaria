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
                    if pizzas[0][0] != None:
                        if pizzas[0][13] == 2 and pizzas[0][13] == 3:
                            print(f"\nUltimas {pizzas[0][13]} Pizzas Pedidas:")
                        elif pizzas[0][13] > 3:
                            print(f"\nUltimas 3 Pizzas Pedidas:")
                        elif pizzas[0][13] == 1:
                            print(f"\nUltima Pizza Pedida:")

                        for pizza in pizzas:
                            if pizza[0] != None:
                                if pizza[0] == 'Inteira':
                                    print('\n')
                                    print('     Pizza.........: ', pizza[0])
                                    print('     ID............: ', pizza[1])
                                    print('     Nome..........: ', pizza[2])
                                    print('     Tipo..........: ', pizza[3])
                                    print('     Valor Custo...: R$', pizza[4])
                                elif pizza[0] == 'Meia':
                                    if (float(pizza[8].replace(',', '.')) > float(pizza[12].replace(',', '.'))):
                                        print('\n')
                                        print('     Pizza.........: ', pizza[0])
                                        print('     ID 1/2........: ', pizza[5])
                                        print('     ID 2/2........: ', pizza[9])
                                        print('     Metade 1/2....: ', pizza[6])
                                        print('     Metade 2/2....: ', pizza[10])
                                        print('     Tipo 1/2......: ', pizza[7])
                                        print('     Tipo 2/2......: ', pizza[11])
                                        print('     Valor Custo...: R$', pizza[8])
                                    else:
                                        print('\n')
                                        print('     Pizza.........: ', pizza[0])
                                        print('     ID 1/2........: ', pizza[5])
                                        print('     ID 2/2........: ', pizza[9])
                                        print('     Metade 1/2....: ', pizza[6])
                                        print('     Metade 2/2....: ', pizza[10])
                                        print('     Tipo 1/2......: ', pizza[7])
                                        print('     Tipo 2/2......: ', pizza[11])
                                        print('     Valor Custo...: R$', pizza[12])
                    else:
                        print("\n           ***** Sem  Historico *****")
                else:
                    print('\n     ***** Nenhum Cadastro Encontrado *****')
                    ID_User = user.Insert()

        pedido = [ID_User]
        pedido.append(library.Datetime_fmt('YYYY-MM-DD'))
        pedido.append(library.Datetime_fmt('HH:MM:SS'))
        ID_Pedido = db_pedido.Insert('Pedido', pedido)
    print("\n         ***** Selecionar  Pizzas *****")
    Tamanho = True
    Quantidade = True
    CodigoPizzaInteira = True
    CodigoPizzaMeiaUm = True
    CodigoPizzaMeiaDois = True
    PizzaInteiraMeia = True
    Pedido = True
    options = ["Media", "Grande", "Gigante"]
    optionspizza = ["Inteira", "Meia"]

    while PizzaInteiraMeia:
        try:
            print('\nEscolha uma opcao: ')
            print('\n   [1] - ' + optionspizza[0])
            print('   [2] - ' + optionspizza[1])
            opcaopizza = int(input("Pizza Inteira ou Meia: "))
            if not 1 <= opcaopizza <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcaopizza in range(1, 3):
                pizzainteirameia = optionspizza[opcaopizza - 1]
                PizzaInteiraMeia = False
                pizza = [(pizzainteirameia)]
                print('    Pizza...: ' + pizzainteirameia)

    if pizzainteirameia == 'Inteira':
        while CodigoPizzaInteira:
            try:
                cod_pizza = int(input("\nCodigo da Pizza Inteira: "))
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                selectpizza = db_pedido.Select(cod_pizza, 'Pizza')
                if selectpizza != 0:
                    CodigoPizzaInteira = False
                    pizza.append(cod_pizza)
                    print('    Pizza...: ' + selectpizza[2])
    elif pizzainteirameia == 'Meia':
        while CodigoPizzaMeiaUm:
            try:
                cod_pizza = int(input("\nCodigo da Pizza 1/2: "))
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                selectpizzaMeiaUm = db_pedido.Select(cod_pizza, 'Pizza')
                if selectpizzaMeiaUm != 0:
                    CodigoPizzaMeiaUm = False
                    CodigoMeiaUm = cod_pizza
                    pizza.append(cod_pizza)
                    print('    Pizza 1/2...: ' + selectpizzaMeiaUm[2])
        while CodigoPizzaMeiaDois:
            try:
                cod_pizza = int(input("\nCodigo da Pizza 2/2: "))
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                if cod_pizza != CodigoMeiaUm:
                    selectpizzaMeiaDois = db_pedido.Select(cod_pizza, 'Pizza')
                    if selectpizzaMeiaDois != 0:
                        CodigoPizzaMeiaDois = False
                        pizza.append(cod_pizza)
                        print('    Pizza 2/2...: ' + selectpizzaMeiaDois[2])
                else:
                    print("\n           ***** Valor Inválido *****")
                    print("           **** Valor Indêntico ****")

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
            if pizzainteirameia == 'Inteira':
                quantidadepizza = int(input(f"Quantidade da Pizza {selectpizza[2]}: "))
            elif pizzainteirameia == 'Meia':
                quantidadepizza = int(input(f"Quantidade da Pizza Meia {selectpizzaMeiaUm[2]}, Meia {selectpizzaMeiaDois[2]}: "))
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if quantidadepizza > 0:
                pizza.append(quantidadepizza)
                Quantidade = False
                print('    Quantidade.: ' + str(quantidadepizza))
            else:
                print("\n           ***** Valor Inválido *****")

    if pizzainteirameia == 'Inteira':
        Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizza[4].replace(',', '.')), quantidadepizza)

    elif pizzainteirameia == 'Meia':
        if (float(selectpizzaMeiaUm[4].replace(',', '.')) > float(selectpizzaMeiaDois[4].replace(',', '.'))):
            Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizzaMeiaUm[4].replace(',', '.')),quantidadepizza)
        else:
            Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizzaMeiaDois[4].replace(',', '.')),quantidadepizza)


    pizza.append(Valor_Unit)
    pizza.append(Valor_Parcial)
    print('\n    Valor Unitario...: ' + str(Valor_Unit))
    print('    Valor Sub Total..: ' + str(Valor_Parcial))
    while Pedido:
        try:
            print('\n   [1] - Incluir mais Pizzas')
            print('   [0] - Concluir Pedido')
            opcao = int(input("Escolha uma opcao: "))
            if not 0 <= opcao <= 1:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao in range(0, 2):
                if New == False:
                    db_pedido.Update('Hora', library.Datetime_fmt('HH:MM:SS'), id_pedido)
                    ID_Pedido = id_pedido
                if opcao == 1:
                    pizza.append(ID_Pedido)
                    Pedido = False
                    if pizzainteirameia == 'Inteira':
                        db_pedido.Insert('Inteira', pizza)
                    elif pizzainteirameia == 'Meia':
                        db_pedido.Insert('Meia', pizza)
                    Total_Parcial = library.Valores_Pedido('Total', ID_Pedido, None)
                    print('Valor Total-Parcial do Pedido: R$', Total_Parcial)
                    Fazer_Pedido(False, ID_Pedido)
                else:
                    pizza.append(ID_Pedido)
                    if pizzainteirameia == 'Inteira':
                        db_pedido.Insert('Inteira', pizza)
                    elif pizzainteirameia == 'Meia':
                        db_pedido.Insert('Meia', pizza)
                    Pedido = False
                    Total_Pedido = library.Valores_Pedido('Total', ID_Pedido, None)
                    Troco = True
                    while Troco:
                        try:
                            print('\nValor Total do Pedido: R$', Total_Pedido)
                            print('\n   [1] - Precisa de Troco')
                            print('   [0] - Nao precisa de Troco')
                            opcaotroco = int(input("Escolha uma opcao: "))
                            if not 0 <= opcao <= 1:
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")
                        else:
                            if opcaotroco in range(0, 2):
                                Troco = False
                                if opcaotroco == 1:
                                    Precisa = True
                                    while Precisa:
                                        try:
                                            print('\nValor Total do Pedido: R$', Total_Pedido)

                                            valortroco = input("Troco para quantos R$: ")
                                            if not(valortroco.replace(',','',1).isdigit()):
                                                raise ValueError("\n           ***** Valor Inválido *****")

                                        except ValueError as e:
                                            print("\n           ***** Valor Inválido *****")

                                        else:
                                            if valortroco.replace(',','',1).isdigit():
                                                if (float(valortroco.replace(',', '.')) > float(Total_Pedido.replace(',', '.'))):
                                                    Precisa = False
                                                    db_pedido.Update('Total', Total_Pedido, ID_Pedido)
                                                    valortroco = library.Valores_Pedido('Troco', ID_Pedido, valortroco)
                                                    db_pedido.Update('Troco', valortroco, ID_Pedido)
                                                    print('\nValor Total do Pedido: R$', Total_Pedido)
                                                    print('\nValor do troco a ser levado: R$', valortroco)

                                                    PrevisaoEntrega = db_pedido.Select(ID_Pedido, 'Hora')
                                                    print('\nPrevisao para Entrega: ', PrevisaoEntrega[0][0])

                                                    print('\n          ***** Pedido Realizado *****')
                                                else:
                                                    print('\nValor menor que o total!\n')
                                else:
                                    db_pedido.Update('Total', Total_Pedido, ID_Pedido)
                                    db_pedido.Update('Troco', 0, ID_Pedido)
                                    PrevisaoEntrega = db_pedido.Select(ID_Pedido, 'Hora')
                                    print('\nValor Total do Pedido: R$', Total_Pedido)
                                    print('\nPrevisao para Entrega: ', PrevisaoEntrega[0][0])

                                    print('\n          ***** Pedido Realizado *****')