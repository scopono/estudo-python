from discord.ext import commands
import discord
from discord import app_commands
MY_GUILD = discord.Object(id=1111997040906469426)
lista_prontuarios = []
lista_emails = []

class Aluno(commands.Cog):
    """Comandos relacionados a dados de alunos"""
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='cadastrar-aluno', description='Cadastra um aluno no formato "prontuario nome email", com o nome precisando estar entre aspas)')
    async def cadastrar_aluno(self, interaction:discord.Interaction, prontuario:str, nome:str, email:str):
        def __eq__(self, value):
            if isinstance(value, self.__class__):
                return self.prontuario == value.prontuario
            return False

        def __hash__(self):
            return hash(self.prontuario)
        
        with open('src/09-estudo-discord-bot/alunos.txt', 'a+', encoding='utf-8') as arquivo:
            dados = [prontuario, nome, email]
            dados = ",".join(dados)
            if lista_prontuarios.count(prontuario) >= 2: 
                await interaction.response.send_message("Você não pode digitar um prontuário repetido!")
            elif lista_emails.count(email) >= 2:
                await interaction.response.send_message("Você não pode digitar um e-mail repetido!")
            else:
                lista_emails.append(email)
                lista_prontuarios.append(prontuario)
                arquivo.write(f'{dados}\n')
                await interaction.response.send_message("Seus dados foram cadastrados com sucesso!")
    @app_commands.command(name='listar-alunos', description='Lista os alunos em "alunos.txt" e retorna um embed')
    async def listar_alunos(self, interaction: discord.Interaction):
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
        
def setup(bot):
    return bot.add_cog(Aluno(bot), guilds=[MY_GUILD])
