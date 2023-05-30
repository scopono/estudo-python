import discord
from discord.ext import commands

class Talks(commands.Cog):
    """ Talks with user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi", help="Envia um Oi (Não requer argumento)") 
    async def send_hello(self, ctx): 
        name = ctx.author.name
        response = "Olá, " + name
        await ctx.send(response)

    @commands.command(name="segredo", help="Envia um segredo no privado. Não requer um argumento.")
    async def secret(self, ctx):
        try:
            await ctx.author.send("nteste")
            await ctx.author.send("teste1")
            await ctx.author.send("teste2")
        except discord.errors.Forbidden:
            await ctx.send(
            "Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)"
            )
def setup(bot):
    return bot.add_cog(Talks(bot))