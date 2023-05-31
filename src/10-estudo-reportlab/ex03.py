from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table, TableStyle

# Definindo o estilo do título
title_style = getSampleStyleSheet()["Title"]
title_style.fontSize = 16

# Definindo o estilo do parágrafo
paragraph_style = getSampleStyleSheet()["Normal"]
paragraph_style.fontSize = 12

# Dados para a tabela
data = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    ["Dado 1", "Dado 2", "Dado 3", "Dado 4"],
]

# Definindo o estilo da tabela
table_style = TableStyle([
    # Defina os estilos da tabela aqui, se necessário
])

# Criando o documento PDF
doc = SimpleDocTemplate("exemplo.pdf", pagesize=letter)

# Lista para armazenar os elementos do PDF
elements = []

# Título
title = Paragraph("Título do Documento", title_style)
elements.append(title)

# Espaçamento após o título
title_spacing = Spacer(1, 20)
elements.append(title_spacing)

# Parágrafo
paragraph = Paragraph("Texto do parágrafo.", paragraph_style)
elements.append(paragraph)

# Espaçamento após o parágrafo
paragraph_spacing = Spacer(1, 15)
elements.append(paragraph_spacing)

# Tabela
table = Table(data)
table.setStyle(table_style)
elements.append(table)

# Construindo o PDF
doc.build(elements)
