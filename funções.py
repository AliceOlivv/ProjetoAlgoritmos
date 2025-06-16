#import sqlite3


#banco = sqlite3.connect("banco_lojaArcanjo.db")


#cursor = banco.cursor()

#import inquirer


def AdicionarServiço(nome,valor,codigo_serviço):
    
    cursor.execute("INSERT INTO serviço VALUES (?, ?, ?)", (serviço, valor_serviço, codigo_serviço))
    banco.commit()
    return print("Adicionado")

def AdicionarEstoquedeProduto()
    

pergunta = [
    inquirer.List(
        'acao',
        message="O que deseja fazer?",
        choices=[
            'Pesquisa de Produto',
            'Serviços disponíveis',
            'Cadastro de produtos e serviços',
            'Gerenciamento de Estoque',
            'Lucro'
        ]
    )
]

resposta = inquirer.prompt(pergunta)

if resposta["acao"]== "Pesquisa de Produto":

    codigo=(input("Escreva o código do produto que deseja pesquisar: "))
    while not codigo.isnumeric():
        print("Erro.Digite um número:")
        codigo=(input(""))

    codigo=int(codigo)
    

    cursor.execute("SELECT * FROM loja WHERE codigo== ? ",(codigo,))
    dados= cursor.fetchall()

    if dados == []:
            print("Não existe dados para esse código")
            print("Deseja")
    else:

        for linha in dados:
            print("Nome:",linha[0])
            print("valor:", linha[1])
            print("Quantidade de itens:", linha[2])

input("")

    
        

    




