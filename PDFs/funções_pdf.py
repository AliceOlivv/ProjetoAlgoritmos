parametroParado = 2

def listaParados():
    import sqlite3

    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT codigo FROM loja WHERE Vendidos <= ?", (parametroParado))
    resultado = cursor.fetchall()

    parados = [linha[0] for linha in resultado]

    cursor.execute("UPDATE loja SET Vendidos = 0")

    banco.commit()
    banco.close()
    
    return(parados)

def salvarDados(data, despesas_f, despesas_v):
    import sqlite3

    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    paradosStr = ""
    parados = listaParados()
    for i in parados:
        paradosStr += str(i) + " "

    cursor.execute("UPDATE Dados_Salvos SET Despesa_Fixas = ? WHERE Data = 0", (despesas_f))
    cursor.execute("UPDATE Dados_Salvos SET Despesas_Variáveis = ? WHERE Data = 0", (despesas_v))
    cursor.execute("UPDATE Dados_Salvos SET Produtos_Parados = ? WHERE Data = 0", (paradosStr))
    cursor.execute("UPDATE Dados_Salvos SET Data = ? WHERE Data = 0", (data))

    cursor.execute("INSERT INTO Dados_Salvos VALUES (?, ?, ?, ?, ?, ?)", (0, 0, 0, 0, "", 0))

    banco.commit()
    banco.close()