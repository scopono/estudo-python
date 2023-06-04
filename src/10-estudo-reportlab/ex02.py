from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm

# Cria o arquivo PDF
pdf_filename = "meu_documento2.pdf"
doc = SimpleDocTemplate(pdf_filename)

# Estilos para o documento
styles = getSampleStyleSheet()

# Adiciona o título com fonte 16pt
title_style = styles["Title"]
title_style.fontSize = 16
title = Paragraph("<b>Título do Documento</b>", title_style)

# Adiciona os parágrafos com fonte 12pt
paragraph_style = styles["Normal"]
paragraph_style.fontSize = 12
paragrafo_diferenciado1 = ParagraphStyle(
    name = 'ParagrafoDiferenciado1',
    fontName = 'Helvetica',
    fontSize = 30,
    leading = 40)

paragrafo_diferenciado2 = ParagraphStyle(
    name = 'ParagrafoDiferenciado2',
    fontName = 'Courier',
    fontSize = 5,
    leading = 10)

paragraph1 = Paragraph("Primeiro parágrafo com texto diferente.", paragraph_style)
paragraph2 = Paragraph("Segundo parágrafo com outro texto.", paragraph_style)
paragrafo3 = Paragraph("Terceiro parágrafo com diferente texto", paragrafo_diferenciado1)
paragrafo4 = Paragraph("Terceiro parágrafo com texto mais diferente ainda", paragrafo_diferenciado2)

# Espaçamentos personalizados
space_20pt = Spacer(1, 20 * mm)  # 20pt de espaço
space_15pt = Spacer(1, 15 * mm)  # 15pt de espaço

# Adiciona o conteúdo ao PDF
content = [title, space_20pt, paragraph1, space_15pt, paragraph2, paragrafo3, paragrafo4]
doc.build(content)

print(f"PDF gerado com sucesso: {pdf_filename}")
