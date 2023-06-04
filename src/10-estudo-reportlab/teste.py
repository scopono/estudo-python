from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table, TableStyle

estilo_titulo = ParagraphStyle(
    name = 'Titulo',
    fontSize = 17,
    fontName = 'Helvetica-Bold',
    leftIndent = 15
    
)

estilo_quantidade_alunos = ParagraphStyle(
    name = 'TotalAlunos',
    fontName = 'Helvetica-Bold',
    leftIndent = 15

)
dados_tabela = []
tipos_informacoes = ['Prontuário', 'Nome', 'E-mail']
espacamento = '                                '
for i in range(len(tipos_informacoes)):
    tipos_informacoes[i] = tipos_informacoes[i] + espacamento
dados_tabela.append(tipos_informacoes)
total_alunos = 0
with open('src/09-estudo-discord-bot/alunos.txt', 'r', encoding='utf-8') as arquivo:
    for aluno in arquivo:
        aluno = aluno.split(sep=',')
        for i in range(len(aluno)):
            aluno[i] = aluno[i].strip()
        dados_tabela.append(aluno) 
        total_alunos += 1


doc = SimpleDocTemplate("alunos.pdf")

elementos = []

titulo = Paragraph("Alunos Cadastrados", estilo_titulo)
espacamento_titulo = Spacer(1, 30)
elementos.append(titulo)
elementos.append(espacamento_titulo)

estilo_tabela = TableStyle([
    ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BACKGROUND', (0, 0), (-1, 0), colors.black),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
    ('TOPPADDING', (0, 0), (-1, 0), 4),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    # ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')

])
tabela = Table(dados_tabela)
tabela.setStyle(estilo_tabela)
espacamento_tabela = Spacer(1, 15)
elementos.append(tabela)
elementos.append(espacamento_tabela)

quantidade_alunos = Paragraph(f"Total de Alunos: {total_alunos}", estilo_quantidade_alunos)
elementos.append(quantidade_alunos)

doc.build(elementos)