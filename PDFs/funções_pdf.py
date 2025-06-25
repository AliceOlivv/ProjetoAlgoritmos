parametroParado = 2

def dataNormal(data):
    data_normal = f"{str(data)[6:8]}/{str(data)[4:6]}/{str(data)[0:4]}"
    return(data_normal)

def dataForma1(data): # Se a data tiver na forma 24062025
    dataForma1 = int( str(data)[4:8]+str(data)[2:4]+str(data)[0:2] )
    return(dataForma1)

def dataForma2(data): # Se a data tiver na forma "24/06/2025"
    data = int( str(data)[6:10]+str(data)[3:5]+str(data)[0:2] )
    return(dataForma2)


def listaParados():
    import sqlite3

    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT codigo FROM loja WHERE Vendidos <= ?", (parametroParado,))
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

    cursor.execute("UPDATE Dados_Salvos SET Despesa_Fixas = ? WHERE Data = 0", (despesas_f,))
    cursor.execute("UPDATE Dados_Salvos SET Despesas_Variáveis = ? WHERE Data = 0", (despesas_v,))
    cursor.execute("UPDATE Dados_Salvos SET Produtos_Parados = ? WHERE Data = 0", (paradosStr,))
    cursor.execute("UPDATE Dados_Salvos SET Data = ? WHERE Data = 0", (data,))

    cursor.execute("INSERT INTO Dados_Salvos VALUES (?, ?, ?, ?, ?, ?)", (0, 0, 0, 0, "", 0))

    banco.commit()
    banco.close()

def criarGrafico(data_1, data_2):
    import matplotlib.pyplot as plt
    import sqlite3

    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    categorias = ["Faturamento", "Gastos de Prod.", "Lucro Bruto", "Despesas Fixas", "Despesas Var.", "Lucro Líq."]
    cores = ['#CC4A7F', '#4D70C8', '#F2B628', "#DA2955", '#E24620', '#464BA7']

    cursor.execute("SELECT Faturamento FROM Dados_Salvos WHERE data >= ? AND data <= ?", (data_1, data_2))
    fat = [linha[0] for linha in cursor.fetchall()[1:]]

    cursor.execute("SELECT Gastos_de_Produção FROM Dados_Salvos WHERE data >= ? AND data <= ?", (data_1, data_2))
    gastos = [linha[0] for linha in cursor.fetchall()[1:]]

    cursor.execute("SELECT Despesa_Fixas FROM Dados_Salvos WHERE data >= ? AND data <= ?", (data_1, data_2))
    despesasF = [linha[0] for linha in cursor.fetchall()[1:]]

    cursor.execute("SELECT Despesas_Variáveis FROM Dados_Salvos WHERE data >= ? AND data <= ?", (data_1, data_2))
    despesasV = [linha[0] for linha in cursor.fetchall()[1:]]


    valores = [sum(fat), sum(gastos), ( sum(fat) - sum(gastos)), sum(despesasF), sum(despesasV), ( sum(fat)-sum(gastos)-sum(despesasF)-sum(despesasV) )]

    plt.figure(figsize = (10, 6))  # Largura x Altura
    plt.bar(categorias, valores, color = cores, width = 0.6)

    plt.title("Análises da Loja")

    plt.ylabel("Valores (R$)")

    # Salvar o gráfico como imagem (PNG)
    plt.savefig("Análises.png")
    plt.close()
    banco.close()

def produtos_parados(data_1, data_2):
    import sqlite3

    banco = sqlite3.connect('banco_lojaArcanjo.db')
    cursor = banco.cursor()

    cursor.execute("SELECT Produtos_Parados FROM Dados_Salvos WHERE data >= ? AND data <= ?", (data_1, data_2))
    estoques = [linha[0] for linha in cursor.fetchall()]

    cursor.execute("SELECT Data FROM Dados_Salvos WHERE data >= ? AND data <= ?", (data_1, data_2))
    datas = [linha[0] for linha in cursor.fetchall()]

    listaParagrafosParados = []

    for i in range(1, len(datas)):
        parados = ""

        for j in range(1, len(estoques[i].split())):
            paradosEspecifico = estoques[i].split()

            cursor.execute("SELECT Nome_produto FROM loja WHERE codigo = ?", (int(paradosEspecifico[j]),))
            paradao = cursor.fetchone()[0]

            parados += paradao + ", "

        listaParagrafosParados.append(f"Entre os dias {dataNormal(datas[i-1])} e {dataNormal(datas[i])} os itens que ficaram parados segundo o paramêtro no período foram: {parados[0:-2]}")
    
    banco.close()
        
    return listaParagrafosParados


