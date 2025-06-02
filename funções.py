#import sqlite3


#banco = sqlite3.connect("banco_lojaArcanjo.db")


#cursor = banco.cursor()

#import inquirer


def AdicionarServiço(nome,valor,codigo_serviço):
    
    cursor.execute("INSERT INTO serviço VALUES (?, ?, ?)", (serviço, valor_serviço, codigo_serviço))
    banco.commit()
    return print("Adicionado")

def AdicionarProduto()
