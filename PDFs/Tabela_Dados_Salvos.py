import sqlite3 as sql

banco = sql.connect('banco_lojaArcanjo.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Dados_Salvos (Faturamento real, Gastos_de_Produção real, Despesa_Fixas real, Despesas_Variáveis real, Produtos_Parados text, Data integer)")

cursor.execute("INSERT INTO Dados_Salvos VALUES (?, ?, ?, ?, ?, ?)", (0, 0, 0, 0, "", 24062025))
cursor.execute("INSERT INTO Dados_Salvos VALUES (?, ?, ?, ?, ?, ?)", (0, 0, 0, 0, "", 0))
banco.commit()

cursor.execute("SELECT * FROM Dados_Salvos")
print(cursor.fetchall())

banco.close()