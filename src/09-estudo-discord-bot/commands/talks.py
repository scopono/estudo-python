import discord
from discord.ext import commands
from discord import app_commands
MY_GUILD = discord.Object(id=1111997040906469426)

class Talks(commands.Cog):
    """ Talks with user"""
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="oi", description="Envia um Oi (Não requer argumento)") 
    async def send_hello(self, interaction: discord.Interaction): 
        name = interaction.user.name
        response = "Olá, " + name
        await interaction.response.send_message(response)

    @app_commands.command(name="segredo", description="Envia um segredo no privado. Não requer um argumento.")
    async def secret(self, interaction: discord.Interaction):
        try:
            await interaction.response.send_message("nteste")
            await interaction.response.send_message("teste1")
            await interaction.response.send_message("teste2")
        except discord.errors.Forbidden:
            await interaction.response.send_message(
            "Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)"
            )
def setup(bot):
    return bot.add_cog(Talks(bot), guilds=[MY_GUILD])