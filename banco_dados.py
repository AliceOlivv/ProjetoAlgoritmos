import sqlite3 as sql

banco = sql.connect('banco_lojaArcanjo.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE loja (Nome_produto text, valor real, estoque integer, codigo integer)")
#cursor.execute("INSERT INTO loja VALUES('Pneu traseiro biz',180.00, 5, 1)")

nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
estoque = int(input("Digite a quantidade em estoque: "))
codigo = int(input("Digite o código do produto: "))

cursor.execute("INSERT INTO loja VALUES (?, ?, ?, ?)", (nome, valor, estoque, codigo))
banco.commit()

cursor.execute("SELECT * FROM loja")
print(cursor.fetchall())

banco.close()