#import sqlite3

#banco = sqlite3.connect("banco_lojaArcanjo.db")

#cursor = banco.cursor()

#banco.close()

#(Usar esses comandos toda vez q fizer uma função usando o banco)

def CadastrarProdutos(nome, valor, estoque, codigo, valor_original):
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM loja WHERE codigo = ?", (codigo,))
    produto_existente = cursor.fetchone()

    if produto_existente:
        banco.close()
        return "existe" #se n for vazio, pra poder puxar no app

    cursor.execute("INSERT INTO loja VALUES (?, ?, ?, ?, ?, ?)", (nome, valor, estoque, codigo, valor_original, 0)) # se n entra no if, o produto vai ser cadastrado, devido a return
    banco.commit()
    banco.close()
    return "sucesso" #pra puxar aba de sucesso ao atualizar


def CadastrarServiço(nome_servico, valor_servico, codigo_servico):
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM serviço WHERE codigo = ?", (codigo_servico,))
    servico_existente = cursor.fetchone()

    if servico_existente:
        banco.close()
        return "existe"

    cursor.execute("INSERT INTO serviço VALUES (?, ?, ?, ?)", (nome_servico, valor_servico, codigo_servico, 0))
    banco.commit()
    banco.close()
    return "sucesso"


def PesquisaDeProdutos(codigo): #é o parametro pra achar o produto
    import sqlite3

    banco = sqlite3.connect("banco_lojaArcanjo.db")
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM loja WHERE codigo = ?", (codigo,))
    dados = cursor.fetchall() #procura o produto e retorna a tupla dentro da lista
    banco.close()

    if not dados:
        return None  # Produto não encontrado
    return dados[0]  # Retorna a tupla (nome, valor, estoque, codigo, valor original, vendidos)


def AdicionarProdutoAoEstoque(codigo, quantidade):
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT Nome_produto, valor, estoque, codigo, valor_original, Vendidos FROM loja WHERE codigo = ?", (codigo,))
    produto = cursor.fetchone()

    if not produto:#se n encortrar
        banco.close() 
        return None
    
    else:
        nome, valor, estoque_atual, codigo_prod, valor_inicial, _ = produto #separando infos da tupla
        novo_estoque = estoque_atual + quantidade
        cursor.execute("UPDATE loja SET estoque = ? WHERE codigo = ?", (novo_estoque, codigo))

        gastoTotal = valor_inicial * quantidade
        cursor.execute("UPDATE Dados_Salvos SET Gastos_de_Produção = ? WHERE Data = 0", (gastoTotal,))

        banco.commit()
        banco.close()
        return nome, valor, estoque_atual, codigo_prod, novo_estoque
    

def RemoverProdutoAoEstoque(codigo, quantidade):
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM loja WHERE codigo = ?", (codigo,))
    produto = cursor.fetchone()

    if produto is None:
        banco.close()
        return None 

    nome, valor, estoque_atual, codigo_prod, _, vendidos = produto #se fosse em cima do if n daria certo pq nao existiria

    if quantidade > estoque_atual:
        banco.close()
        return "quantidade_maior"  

    novo_estoque = estoque_atual - quantidade
    cursor.execute("UPDATE loja SET estoque = ? WHERE codigo = ?", (novo_estoque, codigo))

    nova_quant = vendidos + quantidade
    cursor.execute("UPDATE loja SET Vendidos = ? WHERE codigo = ?", (nova_quant, codigo))
    
    cursor.execute("SELECT Faturamento FROM Dados_Salvos WHERE Data = 0")
    faturamentoAtual = cursor.fetchone()[0]
    novoFaturamento = faturamentoAtual + (valor * quantidade)
    cursor.execute("UPDATE Dados_Salvos SET Faturamento = ? WHERE Data = 0", (novoFaturamento,))
    
    banco.commit()
    banco.close()

    return nome, valor, estoque_atual, codigo_prod, novo_estoque

def RemoverCadastroProduto(codigo_produto):
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM loja WHERE codigo = ?", (codigo_produto, ))
    dados = cursor.fetchone()

    if dados is None:
        banco.close()
        return None

    else: 
        nome, valor, estoque, codigo, _, _ = dados
        cursor.execute("DELETE from loja WHERE codigo = ?", (codigo_produto, ))
        banco.commit()
        banco.close()
        return nome, valor, estoque, codigo


def RemoverCadastroserviço(codigo_serviço):
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM serviço WHERE codigo = ?", (codigo_serviço, ))
    dados = cursor.fetchone()
    banco.commit()


    if dados is None:
        banco.close()
        return None

    else: 
        nome, valor, codigo, Efetuados = dados
        cursor.execute("DELETE from serviço WHERE codigo = ?", (codigo_serviço, ))
        banco.commit()
        banco.close()
        return nome, valor, codigo
    
def registrar_servico(codigo, quantidade=1):
    import sqlite3
    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT Nome_serviço, valor, codigo, Efetuados FROM serviço WHERE codigo = ?", (codigo,))
    dados = cursor.fetchone()

    if dados is None:
        banco.close()
        return "nao existe"
    
    nome, valor, codigo, efetuados = dados
    efetuados_atuais = efetuados or 0
    nova_quantidade = efetuados_atuais + quantidade
    cursor.execute("UPDATE serviço SET Efetuados = ? WHERE codigo = ?", (nova_quantidade, codigo))

    cursor.execute("SELECT Faturamento FROM Dados_Salvos WHERE Data = 0")
    faturamentoAtual = cursor.fetchone()[0]
    novoFaturamento = faturamentoAtual + (valor * quantidade)
    cursor.execute("UPDATE Dados_Salvos SET Faturamento = ? WHERE Data = 0", (novoFaturamento,))

    banco.commit()

    banco.close()
    return "sucesso"