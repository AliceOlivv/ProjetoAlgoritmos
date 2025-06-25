import funções_pdf

def criarPDF(data1, data2):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Paragraph, Image, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

    from reportlab.platypus import SimpleDocTemplate

    # Cria o PDF
    pdf = SimpleDocTemplate("Análises.pdf", pagesize = letter)

    styles = getSampleStyleSheet()

    estilo = ParagraphStyle(
       name = "RecuoEsquerdo",
       parent = styles["Normal"],
       firstLineIndent = 20)  # Valor em pontos (pt) do recuo à esquerda

    texto1 = f"Este gráfico apresenta a análise financeira da loja ao longo do período de {str(data1)[6:8]}/{str(data1)[4:6]}/{str(data1)[0:4]} até {str(data2)[6:8]}/{str(data2)[4:6]}/{str(data2)[0:4]}, destacando o faturamento nesse periodo, quanto foi gasto e o lucro obtido."

    # Caso precise, <br/> quebra a linha no meio do texto

    texto2 = "O Lucro Bruto representa a diferença entre o Faturamento e os Gastos de Produção."
    texto3 = "O Lucro Líquido é obtido após a dedução das Despesas Fixas e Variáveis."

    paragrafo1 = Paragraph(texto1, estilo)
    paragrafo2 = Paragraph(texto2, estilo)
    paragrafo3 = Paragraph(texto3, estilo)

    funções_pdf.criarGrafico(data1, data2)
    grafico_img = Image('Análises.png', width = 400, height = 240)

    # Estilo para o título
    estilo_titulo = ParagraphStyle(
        name = "Titulo",
        parent = styles["Heading1"],
        alignment = 1,  # 0 = esquerda, 1 = centralizado, 2 = direita
        fontSize = 18,
        spaceAfter = 20
    )

    # Título do relatório
    titulo_texto = "Análise Financeira da Loja Arcanjo"
    titulo = Paragraph(titulo_texto, estilo_titulo)

    conteudo = [titulo, paragrafo1, paragrafo2, paragrafo3, Spacer(1, 12), grafico_img, Spacer(1, 12)]

    paragrafos = funções_pdf.produtos_parados(data1, data2)
    for frase in paragrafos:
        conteudo.append(Paragraph(frase, estilo))

    pdf.build(conteudo)