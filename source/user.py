"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para tratativas em pedidos
Arquivo.....: user.py - Funcionalidades para controle dos usuarios
Autor.......: Vinicius Guedes
Observações.: 2020-05-11 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-11 - [R01] Criação da função Menu_Cadastro - Versao 1.00
              ...
"""

def Menu_Cadastro():
    opcao = 1
    while opcao != 0:
        try:
            print('\n             CLIENTES')
            print('[1] - Inserir')
            print('[2] - Alterar')
            print('[3] - Consultar')
            print('[4] - Excluir')
            print('[0] - Voltar')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 4:
                raise ValueError("\nValor Inválido")
        except ValueError as e:
            print("\nValor Inválido")
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
    print('\n      Inserindo Cliente')
    print('\n Nome...........:')
    print('\n Telefone Fixo..:')
    print('\n Telefone Cel...:')
    print('\n CEP............:')
    print('\n Endereço.......:')
    print('\n ')

def Update ():
    print('\nAtualizando')

def Select ():
    print('\nBuscando')

def Delete ():
    print('\nDeletando')
