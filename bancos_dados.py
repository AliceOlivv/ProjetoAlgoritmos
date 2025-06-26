import sqlite3 as sql
banco = sql.connect('banco_lojaArcanjo.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE loja (Nome_produto text, valor real, estoque integer, codigo integer)")
cursor.execute("INSERT INTO loja VALUES('Pneu traseiro biz',180.00, 5, 1)")

nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
estoque = int(input("Digite a quantidade em estoque: "))
codigo = int(input("Digite o código do produto: "))

cursor.execute("INSERT INTO loja VALUES (?, ?, ?, ?)", (nome, valor, estoque, codigo))

cursor.execute("ALTER TABLE loja ADD COLUMN valor_original real")

id_produto=int(input("Digite o id do produto: "))
valor_original=float(input("Digite o valor original do produto"))

cursor.execute("UPDATE loja SET valor_original = ? WHERE codigo=?",(valor_original,id_produto))
banco.commit()
banco.close()

# Adição da coluna vendidos
cursor.execute("ALTER TABLE loja ADD COLUMN Vendidos INTEGER")
cursor.execute("UPDATE loja SET Vendidos = 0")
banco.commit()
banco.close()

#CRIAÇÃO DO BANCO DE SERVIÇOS

import sqlite3 as sql
banco = sql.connect('banco_lojaArcanjo.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE serviço (Nome_serviço text, valor real, codigo integer)")

serviço = input("Digite o nome do serviço: ")
valor_serviço = float(input("Digite o valor do serviço: "))
codigo_serviço = int(input("Digite o código do serviço: "))

cursor.execute("INSERT INTO serviço VALUES (?, ?, ?)", (serviço, valor_serviço, codigo_serviço))
banco.commit()
banco.close()

#nova coluna:

import sqlite3 as sql
banco = sql.connect('banco_lojaArcanjo.db')
cursor = banco.cursor()

id_produto=int(input("Digite o id do produto: "))
valor_original=float(input("Digite o valor original do produto: "))

cursor.execute("UPDATE loja SET valor_original = ? WHERE codigo=?",(valor_original,id_produto))
cursor.execute("ALTER TABLE serviço ADD COLUMN Efetuados INTEGER DEFAULT 0") #para criar nova coluna p controle de serviços feitos
banco.commit()
banco.close()

#CRIAÇÃO DA TABELA Dados_Salvos

import sqlite3 as sql
banco = sql.connect('banco_lojaArcanjo.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Dados_Salvos (Faturamento real, Gastos_de_Produção real, Despesa_Fixas real, Despesas_Variáveis real, Produtos_Parados text, Data integer)")

cursor.execute("INSERT INTO Dados_Salvos VALUES (?, ?, ?, ?, ?, ?)", (0, 0, 0, 0, "", 20250624)) # Ano / Mês / Dia
cursor.execute("INSERT INTO Dados_Salvos VALUES (?, ?, ?, ?, ?, ?)", (0, 0, 0, 0, "", 0))

banco.commit()
banco.close()