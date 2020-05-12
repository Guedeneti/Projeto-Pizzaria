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
    run = True

    while run:
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
                run = False
                print('    Tipo...: ' + tipo)


    pizza.append(input('\n    Ingredientes...: '))
    pizza.append(input('\n    Valor Custo Padrao............: '))
    print('\n ')

    print('Conexão com o banco')
    print(pizza)
    print('***** Pizza Adicionada *****')


def Update():
    print('\nAtualizando')
    PizzaCodigo = input('\n    Digite o Codigo da Pizza...........: ')

def Select():
    print('\nBuscando')


def Delete():
    print('\nDeletando')