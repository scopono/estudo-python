from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, green, blue

# Cria o arquivo PDF
pdf_filename = "hello_world.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)

# Adiciona o texto "Hello, World!"
c.setFont("Helvetica", 40)
c.drawString(10, 700, "Hello, World!")

# Adiciona formas geométricas
c.setStrokeColor(red)
c.setFillColor(green)
c.rect(100, 650, 200, 100, fill=True)
c.setFillColor(blue)
c.circle(400, 700, 50, fill=True)

# Salva e fecha o arquivo PDF
c.showPage()
c.save()

print(f"PDF gerado com sucesso: {pdf_filename}")
