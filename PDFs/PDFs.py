from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.platypus import SimpleDocTemplate

# Cria o PDF
pdf = SimpleDocTemplate("Análises.pdf", pagesize = letter)

styles = getSampleStyleSheet()

estilo = ParagraphStyle(
    name = "RecuoEsquerdo",
    parent = styles["Normal"],
    firstLineIndent = 20)  # valor em pontos (pt) do recuo à esquerda

variavelTexto = """Lucas encontrou uma caixa antiga no sótão da casa da avó. Dentro, havia cartas, fotos amareladas e um diário empoeirado. Curioso, começou a ler as memórias de um jovem aventureiro que desbravou terras distantes. Inspirado, decidiu seguir os passos daquele antepassado misterioso, planejando viagens e explorando mapas esquecidos. Cada página revelava segredos de coragem e amizade, e Lucas sentiu uma conexão profunda com aquele passado. Ao fechar o diário, ele sabia que a aventura estava apenas começando — e que ele também escreveria suas próprias histórias para as próximas gerações."""

#Caso precise, <br/> quebra a linha no meio do texto

texto1 = variavelTexto #Só pra testar se funciona com variáveis

texto2 = """Clara adorava observar estrelas. Todas as noites, ela subia no telhado e se perdia no brilho do céu. Certo dia, uma estrela cadente riscou o horizonte, e Clara fez um pedido silencioso: queria entender o universo. Na manhã seguinte, encontrou um pequeno livro sobre astronomia na porta de casa, sem remetente. Animada, começou a estudar com dedicação. Com o tempo, suas perguntas se transformaram em descobertas, e Clara se tornou uma astrônoma respeitada, realizando sonhos que começaram sob o manto das estrelas."""

paragrafo1 = Paragraph(texto1, estilo)

paragrafo2 = Paragraph(texto2, estilo)

# Monta o documento
pdf.build([paragrafo1, Spacer(1, 12), paragrafo2])