#import sqlite3

#banco = sqlite3.connect("banco_lojaArcanjo.db")

#cursor = banco.cursor()

#banco.close()

#(Usar esses comandos toda vez q fizer uma função usando o banco)

def ValidaString(parametro1):
    if parametro1.isalpha():
        return parametro1
    
    # a função "isalpha" analisa se todos os caracters da string são letras do alfabeto, retorna False se não e True se sim
    # se retornar True retorna a string normalmente, se não pede um novo novo e chama a função novamente para valida-lo
    else:
        novo_valor = input("Nome inválido. Digite novamente: ")
        return ValidaString(novo_valor)

def ValidaInteiro(parametro1):
     
     try:
        parametro1= int(parametro1)
        return parametro1
     #ele tenta converter para inteiro , se der erro, vai para o except

     except ValueError:
        novo_valor=input("Número inválido, digite novamente: ")
        return ValidaInteiro(novo_valor)
     #quando vai para o except, o usuário digita um novo valor e chamamos a função novamente para validá-lo
     
def ValidaFloat(parametro1):
     # a mesma coisa do ValidaInteiro, mudando só a conversão para float
     try:
        parametro1= float(parametro1)
        return parametro1
     

     except ValueError:
        novo_valor=input("Número inválido, digite novamente: ")
        return ValidaFloat(novo_valor)
     
def CadastrarServiço():
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db') #conecta o nosso programa com o arquivo do banco de dados, banco é um objeto em que podemos nos conectar e controlar o banco
    cursor = banco.cursor() # cursor é o objeto em que executamos os comandos de sql

    

    codigo_serviço = (input("Digite o código do serviço: "))
    codigo_serviço = ValidaInteiro(codigo_serviço)

    cursor.execute("SELECT * FROM serviço WHERE codigo = ?", (codigo_serviço,)) #pesquisa, entre todas as colunas, as informações da linha onde o código é igual ao código enviado
    serviço_existente = cursor.fetchone() #cria uma lista de tuplas com os resultados da pesquisa

    if serviço_existente:
         print("Já existe um serviço com esse código!") #se estiver informações na lista, é porque já existe um serviço com o código enviado, se não, não tem.
    else:
        serviço=input("Digite o nome do serviço")

        serviço= ValidaString(serviço)


        valor_serviço=input("Digite o valor do serviço: ")
        
        valor_serviço= ValidaFloat(valor_serviço)
                                                            
        
        cursor.execute("INSERT INTO serviço VALUES (?, ?, ?)", (serviço, valor_serviço, codigo_serviço)) # insere os valores nas colunas
        banco.commit() # confirma que estamos inserindo essas informações no banco
        banco.close() # fecha o banco para não ficar rodando sem precisão
        print("Serviço adicionado!")

def CadastrarProdutos():
    import sqlite3

    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    codigo = (input("Digite o código do produto: "))
    codigo = ValidaInteiro(codigo)

    cursor.execute("SELECT * FROM loja WHERE codigo = ?", (codigo,))
    produto_existente = cursor.fetchone()

    if produto_existente:
         print("Já existe um produto com esse código!")
    else:     
        nome = input("Digite o nome do produto: ")
        nome = ValidaString(nome)
        
        valor = (input("Digite o valor do produto: "))
        valor = ValidaFloat(valor)

        estoque = (input("Digite a quantidade em estoque: "))
        estoque = ValidaInteiro(estoque)

        cursor.execute("INSERT INTO loja VALUES (?, ?, ?, ?)", (nome, valor, estoque, codigo))
        banco.commit()
    
        print("Produto cadastrado!")
    banco.close()

def PesquisaDeProdutos():
    import sqlite3


    banco = sqlite3.connect("banco_lojaArcanjo.db")


    cursor = banco.cursor()

    codigo=(input("Escreva o código do produto que deseja pesquisar: "))
    codigo= ValidaInteiro(codigo)


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

    codigo_q = (input("Digite o código do produto que deseja adicionar ao estoque: "))
    codigo_q = ValidaInteiro(codigo_q)

    cursor.execute("SELECT Nome_produto, estoque FROM loja WHERE codigo = ?", (codigo_q,))
    produto = cursor.fetchone()

    if produto:
        nome = produto[0]
        estoque_atual = produto[1]
        print("Produto encontrado:", nome, "- Estoque atual:", estoque_atual)

        quantidade_q = input("Digite a quantidade que deseja adicionar ao estoque: ")
        quantidade_q = ValidaInteiro(quantidade_q)

        novo_estoque = estoque_atual + quantidade_q
        cursor.execute("UPDATE loja SET estoque = ? WHERE codigo = ?", (novo_estoque, codigo_q))
        banco.commit()
        print("Estoque atualizado com sucesso! Novo estoque:", novo_estoque)
    else:
        print("Produto não encontrado!")

    banco.close()

   

def RemoverProdutoDoEstoque():
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    codigo = (input("Digite o código do produto que deseja retirar: "))
    codigo = ValidaInteiro(codigo)

    cursor.execute("SELECT Nome_produto, estoque FROM loja WHERE codigo = ?", (codigo,))
    produto = cursor.fetchone()

    if produto:
        nome = produto[0]
        estoque_atual = produto[1]
        print("Produto encontrado:", nome, "- Estoque atual:", estoque_atual)

        quantidade = int(input("Digite a quantidade que deseja retirar: "))

        if quantidade > estoque_atual:
            print("Quantidade maior que o estoque disponível!")

            decisao=str(input(f'Deseja digitar um novo valor disponível para retirada de estoque do produto {produto[0]}?'))
            decisao.upper()

            if decisao=='SIM':
                RemoverProdutoDoEstoque(codigo)
          
        else:
            novo_estoque = estoque_atual - quantidade
            cursor.execute("UPDATE loja SET estoque = ? WHERE codigo = ?", (novo_estoque, codigo))
            banco.commit()
            print("Estoque atualizado!")
    else:
        print("Produto não encontrado!")

    banco.close()
