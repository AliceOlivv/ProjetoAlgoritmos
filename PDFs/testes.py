import matplotlib.pyplot as plt
import sqlite3

data_1, data_2 = 20250624, 20250625

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

print(sum(fat))