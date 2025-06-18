#import sqlite3

#banco = sqlite3.connect("banco_lojaArcanjo.db")

#cursor = banco.cursor()

#banco.close()

#(Usar esses comandos toda vez q fizer uma função usando o banco)

import inquirer


def CadastrarServiço():
    import sqlite3


    banco = sqlite3.connect("banco_lojaArcanjo.db")


    cursor = banco.cursor()

    serviço=input("Digite o nome do serviço")

    valor_serviço=("Digite o valor do serviço: ")
    while not valor_serviço.isnumeric():
            print("Erro. Digite um número:")
            valor_serviço=(input(""))
    valor_serviço=float(valor_serviço)
                                                         
    codigo_serviço=("Digite o código do serviço: ")
    while not codigo_serviço.isnumeric():
            print("Erro. Digite um número inteiro:")
            codigo_serviço=(input(""))
    codigo_serviço=int(codigo_serviço)
    
    cursor.execute("INSERT INTO serviços VALUES (?, ?, ?)", (serviço, valor_serviço, codigo_serviço))
    banco.commit()
    banco.close()
    print("Adicionado")

#def CadastrarProdutos()

def PesquisaDeProdutos():
    import sqlite3


    banco = sqlite3.connect("banco_lojaArcanjo.db")


    cursor = banco.cursor()

    codigo=(input("Escreva o código do produto que deseja pesquisar: "))
    while not codigo.isnumeric():
        print("Erro. Digite um número:")
        codigo=(input(""))

    codigo=int(codigo)

    cursor.execute("SELECT * FROM loja WHERE codigo== ? ",(codigo,))
    dados= cursor.fetchall()
    banco.close()

    if dados == []:
        print("Não existe dados para esse código")
    else:
        for linha in dados:
            print("Nome:",linha[0])
            print("valor:", linha[1])
            print("Quantidade de itens:", linha[2])

#def AdicionarProdutoAoEstoque()
     
#def RemoverProdutoAoEstoque()

     

    




    




