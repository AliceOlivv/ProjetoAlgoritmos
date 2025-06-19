#import sqlite3

#banco = sqlite3.connect("banco_lojaArcanjo.db")

#cursor = banco.cursor()

#banco.close()

#(Usar esses comandos toda vez q fizer uma função usando o banco)

import inquirer


def CadastrarServiço():
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    codigo = int(input("Digite o código do serviço: "))

    cursor.execute("SELECT * FROM serviço WHERE codigo = ?", (codigo,))
    serviço_existente = cursor.fetchone()

    if serviço_existente:
         print("Já existe um serviço com esse código!")
    else:
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

def CadastrarProdutos():
    import sqlite3

    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    codigo = int(input("Digite o código do produto: "))

    cursor.execute("SELECT * FROM loja WHERE codigo = ?", (codigo,))
    produto_existente = cursor.fetchone()

    if produto_existente:
         print("Já existe um produto com esse código!")
    else:     
        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        
        cursor.execute("INSERT INTO loja VALUES (?, ?, ?, ?)", (nome, valor, estoque, codigo))
        banco.commit()
    
        print("Produto cadastrado!")
    banco.close()

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

def AdicionarProdutoAoEstoque():
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    codigo = int(input("Digite o código do produto que deseja adicionar ao estoque: "))

    cursor.execute("SELECT nome, estoque FROM loja WHERE codigo = ?", (codigo,))
    produto = cursor.fetchone()

    if produto:
        nome = produto[0]
        estoque_atual = produto[1]
        print("Produto encontrado:", nome, "- Estoque atual:", estoque_atual)

        quantidade = int(input("Digite a quantidade que deseja adicionar ao estoque: "))

        novo_estoque = estoque_atual + quantidade
        cursor.execute("UPDATE loja SET estoque = ? WHERE codigo = ?", (novo_estoque, codigo))
        banco.commit()
        print("Estoque atualizado com sucesso! Novo estoque:", novo_estoque)
    else:
        print("Produto não encontrado!")

    banco.close()

   

def RemoverProdutoAoEstoque():
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    codigo = int(input("Digite o código do produto que deseja retirar: "))

    cursor.execute("SELECT nome, estoque FROM loja WHERE codigo = ?", (codigo,))
    produto = cursor.fetchone()

    if produto:
        nome = produto[0]
        estoque_atual = produto[1]
        print("Produto encontrado:", nome, "- Estoque atual:", estoque_atual)

        quantidade = int(input("Digite a quantidade que deseja retirar: "))

        if quantidade > estoque_atual:
            print("Quantidade maior que o estoque disponível!")
        else:
            novo_estoque = estoque_atual - quantidade
            cursor.execute("UPDATE loja SET estoque = ? WHERE codigo = ?", (novo_estoque, codigo))
            banco.commit()
            print("Estoque atualizado!")
    else:
        print("Produto não encontrado!")

    banco.close()
