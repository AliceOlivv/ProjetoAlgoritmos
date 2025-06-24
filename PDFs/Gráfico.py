import matplotlib.pyplot as plt

categorias = ["Faturamento", "Gastos de Prod.", "Lucro Bruto", "Despesas Fixas", "Despesas Var.", "Lucro Líq."]
cores = ['#CC4A7F', '#4D70C8', '#F2B628', "#DA2955", '#E24620', '#464BA7']

valores = [3000, 700, 2300, 300, 200, 1800]

plt.figure(figsize = (10, 6))  # Largura x Altura
plt.bar(categorias, valores, color = cores, width = 0.6)

plt.title("Análises da Loja")

plt.ylabel("Valores (R$)")

# Salvar o gráfico como imagem (PNG)
plt.savefig("Análises.png")
plt.close()