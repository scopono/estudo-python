from discord.ext import commands
import discord

lista_prontuarios = []
lista_emails = []
contador = 0

class Aluno(commands.Cog):
    """Comandos relacionados a dados de alunos"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cadastrar-aluno', help='Cadastra um aluno no formato "prontuario nome email", com o nome precisando estar entre aspas)')
    async def cadastrar_aluno(self, ctx, *dados):
        def __eq__(self, value):
            if isinstance(value, self.__class__):
                return self.prontuario == value.prontuario
            return False

        def __hash__(self):
            return hash(self.prontuario)
        
        with open('src/09-estudo-discord-bot/alunos.txt', 'a+', encoding='utf-8') as arquivo:
            dados = ",".join(dados)
            lista_dados = dados.split(sep=",")
            prontuario = lista_dados[0]
            email = lista_dados[-1]
            if len(lista_dados) != 3:
                await ctx.send("Você não digitou três argumentos!")
            elif lista_prontuarios.count(prontuario) >= 2: 
                await ctx.send("Você não pode digitar um prontuário repetido!")
            elif lista_emails.count(email) >= 2:
                await ctx.send("Você não pode digitar um e-mail repetido!")
            else:
                lista_emails.append(email)
                lista_prontuarios.append(prontuario)
                arquivo.write(f'{dados}\n')
                await ctx.send("Seus dados foram escritos com sucesso!")
    @commands.command(name='listar-alunos', help='Lista os alunos em "alunos.txt" e retorna um embed')
    async def listar_alunos(self, ctx):
        global contador
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
        await ctx.send(embed=embed)
        contador = 0
        
def setup(bot):
    return bot.add_cog(Aluno(bot))
