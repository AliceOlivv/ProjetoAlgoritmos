from reportlab.pdfgen import canvas # type: ignore


from reportlab.lib.pagesizes import letter, A4
#myCanvas = Canvas('myfile.pdf', pagesize=letter)
#width, height = letter #keep for later


def hello(c):
    c.drawString(100, 150, "Hello World")

c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()

def init(self, filename):
    pagesize = letter,
    bottomup = 1,
    pageCompression = 0,
    encoding = rl_config.defaultEncoding,
    verbosity = 0,
    encrypt = None

init("Meu arquivo")