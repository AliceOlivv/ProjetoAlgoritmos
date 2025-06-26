# import sqlite3 as sql

# banco = sql.connect('banco_lojaArcanjo.db')

# cursor = banco.cursor()


#cursor.execute("CREATE TABLE serviço (Nome_serviço text, valor real, codigo integer)")

#serviço = input("Digite o nome do serviço: ")
#valor_serviço = float(input("Digite o valor do serviço: "))
#codigo_serviço = int(input("Digite o código do serviço: "))

#cursor.execute("INSERT INTO serviço VALUES (?, ?, ?)", (serviço, valor_serviço, #codigo_serviço))
#banco.commit()

#cursor.execute("SELECT * FROM serviço")
#print(cursor.fetchall())


#nova coluna:

#id_produto=int(input("Digite o id do produto: "))
#valor_original=float(input("Digite o valor original do produto: "))

#cursor.execute("UPDATE loja SET valor_original = ? WHERE codigo=?",(valor_original,id_produto))
# cursor.execute("ALTER TABLE serviço ADD COLUMN Efetuados INTEGER DEFAULT 0") #para criar nova coluna p controle de serviços feitos
# banco.commit()

# banco.close()