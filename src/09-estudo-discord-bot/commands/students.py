from discord.ext import commands
import discord
from discord import app_commands
from discord import ui
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table, TableStyle

MY_GUILD = discord.Object(id=1111997040906469426)
lista_prontuarios = []
lista_emails = []

class MeuModal(ui.Modal, title="Informações do aluno"):
    prontuario = ui.TextInput(label="Informe o seu prontuário!", placeholder="Prontuário: ", style=discord.TextStyle.short)
    nome = ui.TextInput(label="Informe o seu nome!", placeholder="Nome: ", style=discord.TextStyle.short)
    email = ui.TextInput(label="Informe o seu email!", placeholder="Email: ", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        representacao_dados = f'{self.prontuario},{self.nome},{self.email}'
        with open("src/09-estudo-discord-bot/alunos.txt", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        if str(self.prontuario) in conteudo: 
            await interaction.response.send_message("Você não pode digitar um prontuário repetido!")
        elif str(self.email) in conteudo:
            await interaction.response.send_message("Você não pode digitar um e-mail repetido!")
        else:
            with open('src/09-estudo-discord-bot/alunos.txt', 'a+', encoding='utf-8') as arquivo:
                arquivo.write(f'{representacao_dados}\n')
            await interaction.response.send_message('Dados cadastrados com sucesso')

class Aluno(commands.Cog):
    """Comandos relacionados a dados de alunos"""
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='cadastrar-aluno', description='Cadastra um aluno no formato "prontuario nome email", com o nome precisando estar entre aspas)')
    async def cadastrar_aluno(self, interaction:discord.Interaction):
        def __eq__(self, value):
            if isinstance(value, self.__class__):
                return self.prontuario == value.prontuario
            return False
        def __hash__(self):
            return hash(self.prontuario)
        
        await interaction.response.send_modal(MeuModal())

    @app_commands.command(name='listar-alunos', description='Lista os alunos em "alunos.txt" e retorna um embed')
    async def listar_alunos(self, interaction: discord.Interaction, formato: str = None):
        
        if formato == 'pdf':
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
            ])
            tabela = Table(dados_tabela)
            tabela.setStyle(estilo_tabela)
            espacamento_tabela = Spacer(1, 15)
            elementos.append(tabela)
            elementos.append(espacamento_tabela)

            quantidade_alunos = Paragraph(f"Total de Alunos: {total_alunos}", estilo_quantidade_alunos)
            elementos.append(quantidade_alunos)

            doc.build(elementos)
            await interaction.response.send_message("Tabela com alunos em PDF formada com sucesso!")
        
        elif formato == None:

            contador = 0
            embed = discord.Embed(
                title = "Alunos Cadastrados",
                description = "Lista de alunos cadastrados do Instituto Federal de São Paulo (IFSP), câmpus São Paulo.",
                color = 0x0000FF
            )

            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
            embed.set_footer(text='Feito por ' + self.bot.user.name, icon_url=self.bot.user.avatar)

            with open('src/09-estudo-discord-bot/alunos.txt', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    contador += 1
                    embed.add_field(name=f'Aluno{contador}', value=linha)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Os únicos formatos suportados são PDF e Embed.")
        
def setup(bot):
    return bot.add_cog(Aluno(bot), guilds=[MY_GUILD])
