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

def Menu_Relatorio ():
    print('             RELATORIOS')
    print('[1] - Cliente')
    print('[2] - Cliente Completo')
    print('[3] - Pedidos')
    print('[4] - Pizza')
    print('[5] - Pizza - Maior receita')
    print('[6] - Pizza - Menor receita')
    print('[0] - Voltar')
    return int(input('Digite a opção desejada: '))