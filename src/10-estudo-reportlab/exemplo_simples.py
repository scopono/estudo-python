from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

# Cria um objeto Story para armazenar o conteúdo do PDF
Story = []

# Estilos para o documento
styles = getSampleStyleSheet()

# Adiciona um título ao documento
title = Paragraph("<b>Meu Documento PDF</b>", styles['Title'])
Story.append(title)

# Adiciona alguns parágrafos
parag1 = Paragraph("Este é um exemplo de documento PDF gerado com o ReportLab.", styles['Normal'])
parag2 = Paragraph("Aqui está um parágrafo de texto adicional.", styles['Normal'])
Story.extend([parag1, parag2])

# Adiciona um espaço em branco
Story.append(Spacer(1, 12))

# Dados da tabela
data = [['Nome', 'Idade', 'Cidade'],
        ['João', '30', 'São Paulo'],
        ['Maria', '25', 'Rio de Janeiro'],
        ['Carlos', '35', 'Belo Horizonte']]

# Cria a tabela
table = Table(data)

# Estilo da tabela
table.setStyle([('BACKGROUND', (0, 0), (-1, 0), '#9BC2E6'),
                ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), '#F7F7F7'),
                ('TEXTCOLOR', (0, 1), (-1, -1), '#333333'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
                ('TOPPADDING', (0, 1), (-1, -1), 10),
                ('BOTTOMPADDING', (0, -1), (-1, -1), 12),
                ('GRID', (0, 0), (-1, -1), 1, '#D4D4D4')])

# Adiciona a tabela ao Story
Story.append(table)

# Cria o arquivo PDF
pdf_filename = "meu_documento.pdf"
doc = SimpleDocTemplate(pdf_filename)

# Adiciona o conteúdo ao PDF
doc.build(Story)

print(f"PDF gerado com sucesso: {pdf_filename}")
