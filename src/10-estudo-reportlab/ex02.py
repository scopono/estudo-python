from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
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
paragraph1 = Paragraph("Primeiro parágrafo com texto diferente.", paragraph_style)
paragraph2 = Paragraph("Segundo parágrafo com outro texto.", paragraph_style)

# Espaçamentos personalizados
space_20pt = Spacer(1, 20 * mm)  # 20pt de espaço
space_15pt = Spacer(1, 15 * mm)  # 15pt de espaço

# Adiciona o conteúdo ao PDF
content = [title, space_20pt, paragraph1, space_15pt, paragraph2]
doc.build(content)

print(f"PDF gerado com sucesso: {pdf_filename}")
